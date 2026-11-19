"""Gera uma imagem com o FLUX.2 klein 4B (fp8) no ComfyUI local, usando até 4 imagens de referência.

Precisa do ComfyUI ligado (porta 8188) e dos arquivos flux-2-klein-4b-fp8.safetensors (diffusion_models),
qwen_3_4b_fp8_mixed.safetensors (text_encoders) e flux2-vae.safetensors (vae). Roda em qualquer Python 3 (só stdlib).

  python ferramentas/klein_ref.py --prompt "Use image 1 for the character ..." --refs p0.png 003.png --out saida.png
"""

import argparse
import json
import mimetypes
import time
import urllib.request
import uuid
from pathlib import Path

URL = "http://127.0.0.1:8188"


def subir(caminho: Path) -> str:
    """Envia a imagem para a pasta input do ComfyUI e devolve o nome lá dentro."""
    limite = uuid.uuid4().hex
    dados = caminho.read_bytes()
    tipo = mimetypes.guess_type(caminho.name)[0] or "image/png"
    corpo = (f"--{limite}\r\nContent-Disposition: form-data; name=\"image\"; filename=\"{caminho.name}\"\r\n"
             f"Content-Type: {tipo}\r\n\r\n").encode() + dados + (
             f"\r\n--{limite}\r\nContent-Disposition: form-data; name=\"overwrite\"\r\n\r\ntrue\r\n--{limite}--\r\n").encode()
    req = urllib.request.Request(f"{URL}/upload/image", corpo, {"Content-Type": f"multipart/form-data; boundary={limite}"})
    return json.loads(urllib.request.urlopen(req).read())["name"]


def workflow(prompt: str, refs: list[str], w: int, h: int, seed: int, passos: int) -> dict:
    g = {
        "unet": {"class_type": "UNETLoader", "inputs": {"unet_name": "flux-2-klein-4b-fp8.safetensors", "weight_dtype": "default"}},
        "clip": {"class_type": "CLIPLoader", "inputs": {"clip_name": "qwen_3_4b_fp8_mixed.safetensors", "type": "flux2", "device": "default"}},
        "vae": {"class_type": "VAELoader", "inputs": {"vae_name": "flux2-vae.safetensors"}},
        "pos": {"class_type": "CLIPTextEncode", "inputs": {"text": prompt, "clip": ["clip", 0]}},
        "neg": {"class_type": "ConditioningZeroOut", "inputs": {"conditioning": ["pos", 0]}},
    }
    p, n = ["pos", 0], ["neg", 0]
    for i, nome in enumerate(refs):
        g[f"img{i}"] = {"class_type": "LoadImage", "inputs": {"image": nome}}
        g[f"esc{i}"] = {"class_type": "ImageScaleToTotalPixels",
                        "inputs": {"image": [f"img{i}", 0], "upscale_method": "nearest-exact", "megapixels": 1.0, "resolution_steps": 1}}
        g[f"lat{i}"] = {"class_type": "VAEEncode", "inputs": {"pixels": [f"esc{i}", 0], "vae": ["vae", 0]}}
        g[f"rp{i}"] = {"class_type": "ReferenceLatent", "inputs": {"conditioning": p, "latent": [f"lat{i}", 0]}}
        g[f"rn{i}"] = {"class_type": "ReferenceLatent", "inputs": {"conditioning": n, "latent": [f"lat{i}", 0]}}
        p, n = [f"rp{i}", 0], [f"rn{i}", 0]
    g.update({
        "guia": {"class_type": "CFGGuider", "inputs": {"model": ["unet", 0], "positive": p, "negative": n, "cfg": 1.0}},
        "amostra": {"class_type": "KSamplerSelect", "inputs": {"sampler_name": "euler"}},
        "sigmas": {"class_type": "Flux2Scheduler", "inputs": {"steps": passos, "width": w, "height": h}},
        "ruido": {"class_type": "RandomNoise", "inputs": {"noise_seed": seed}},
        "vazio": {"class_type": "EmptyFlux2LatentImage", "inputs": {"width": w, "height": h, "batch_size": 1}},
        "amostrar": {"class_type": "SamplerCustomAdvanced", "inputs": {"noise": ["ruido", 0], "guider": ["guia", 0],
                     "sampler": ["amostra", 0], "sigmas": ["sigmas", 0], "latent_image": ["vazio", 0]}},
        "dec": {"class_type": "VAEDecode", "inputs": {"samples": ["amostrar", 0], "vae": ["vae", 0]}},
        "salvar": {"class_type": "SaveImage", "inputs": {"images": ["dec", 0], "filename_prefix": "klein"}},
    })
    return g


def gerar(prompt: str, refs: list[Path], saida: Path, w: int = 1344, h: int = 768, seed: int = 1, passos: int = 4) -> float:
    nomes = [subir(r) for r in refs]
    corpo = json.dumps({"prompt": workflow(prompt, nomes, w, h, seed, passos), "client_id": uuid.uuid4().hex}).encode()
    pid = json.loads(urllib.request.urlopen(urllib.request.Request(f"{URL}/prompt", corpo, {"Content-Type": "application/json"})).read())["prompt_id"]
    t0 = time.time()
    while True:
        hist = json.loads(urllib.request.urlopen(f"{URL}/history/{pid}").read())
        if pid in hist:
            st = hist[pid].get("status", {})
            if st.get("status_str") == "error":
                raise RuntimeError(json.dumps(st.get("messages"))[:2000])
            img = hist[pid]["outputs"]["salvar"]["images"][0]
            q = f"filename={img['filename']}&subfolder={img['subfolder']}&type={img['type']}"
            saida.parent.mkdir(parents=True, exist_ok=True)
            saida.write_bytes(urllib.request.urlopen(f"{URL}/view?{q}").read())
            return time.time() - t0
        time.sleep(1)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--refs", nargs="*", default=[])
    ap.add_argument("--out", required=True)
    ap.add_argument("--w", type=int, default=1344)
    ap.add_argument("--h", type=int, default=768)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--steps", type=int, default=4)
    a = ap.parse_args()
    s = gerar(a.prompt, [Path(r) for r in a.refs], Path(a.out), a.w, a.h, a.seed, a.steps)
    print(f"ok {a.out} {s:.1f} s")
