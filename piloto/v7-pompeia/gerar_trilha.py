"""Gera uma trilha instrumental por bloco de capítulos com ACE-Step 1.5 turbo (ComfyUI, Apache 2.0 / MIT).
Roda em qualquer Python 3 (só usa a API HTTP do ComfyUI, que precisa estar ligado).

  python piloto/v7-pompeia/gerar_trilha.py [blocos...] [--segundos N]

Sem blocos, gera os que ainda não têm arquivo. A duração de cada bloco vem de voz/duracoes.json (se existir) + folga;
o montar.py repete a trilha com crossfade se o bloco ficar mais longo.
"""

import json
import random
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

AQUI = Path(__file__).resolve().parent
OUT = AQUI / "trilha"
COMFY = "http://127.0.0.1:8188"
COMFY_OUT = Path("C:/ai-local/comfyui/output")
MAX_SEG = 240  # trilhas mais longas que isso ficam repetitivas e pesam na VRAM; o montar.py emenda

# leve e dinâmica, mudando de clima ao longo do vídeo
ESTILOS = {
    'abertura': ('curious light documentary underscore, plucked harp, soft flute, pizzicato strings, playful, mediterranean, instrumental', 100, 'D major'),
    'data': ('quirky investigative underscore, marimba, pizzicato strings, clarinet, curious, bouncy, instrumental', 108, 'G major'),
    'padaria': ('calm warm early morning music, soft acoustic guitar, flute, gentle strings, steady groove, instrumental', 78, 'F major'),
    'paredes': ('lively busy mediterranean street music, mandolin, hand drums, tambourine, bouncy, instrumental', 112, 'A major'),
    'bar': ('warm relaxed mediterranean taverna music, acoustic guitar, accordion, light percussion, instrumental', 96, 'C major'),
    'arena': ('energetic rhythmic documentary music, hand drums, brass stabs, driving strings, exciting, instrumental', 118, 'D minor'),
    'nuvem': ('tense curious suspense underscore, low strings pizzicato, soft timpani, sustained pads, building, continuous pulse, instrumental', 84, 'E minor'),
    'chuva': ('dramatic urgent underscore, driving low strings, timpani, rising tension, continuous groove, instrumental', 96, 'C minor'),
    'noite': ('dark slow somber underscore, low cello, soft piano, sustained strings, solemn, steady pulse, instrumental', 62, 'D minor'),
    'luto': ('respectful quiet elegiac chamber music, solo cello, soft piano, restrained, moving, steady pulse, instrumental', 60, 'A minor'),
    'fecho': ('warm reflective hopeful outro, soft piano, plucked strings, light strings, uplifting, instrumental', 90, 'C major'),
}


def duracao_blocos() -> dict[str, float]:
    cenas = json.loads((AQUI / "roteiro.json").read_text(encoding="utf-8"))["cenas"]
    dur_path = AQUI / "voz/duracoes.json"
    dur = json.loads(dur_path.read_text(encoding="utf-8")) if dur_path.exists() else {}
    seg: dict[str, float] = {}
    for c in cenas:
        d = dur.get(c["id"], len(c["texto"].split()) / 2.9) + 0.45 + (1.6 if c["inicio_capitulo"] else 0)
        seg[c["bloco"]] = seg.get(c["bloco"], 0) + d
    return {b: min(s + 10, MAX_SEG) for b, s in seg.items()}


def workflow(tags: str, bpm: int, tom: str, segundos: float, seed: int, prefixo: str) -> dict:
    return {
        "1": {"class_type": "UNETLoader", "inputs": {"unet_name": "acestep_v1.5_turbo.safetensors",
                                                      "weight_dtype": "default"}},
        "2": {"class_type": "ModelSamplingAuraFlow", "inputs": {"model": ["1", 0], "shift": 3}},
        "3": {"class_type": "DualCLIPLoader", "inputs": {"clip_name1": "qwen_0.6b_ace15.safetensors",
                                                          "clip_name2": "qwen_1.7b_ace15.safetensors",
                                                          "type": "ace", "device": "default"}},
        "4": {"class_type": "VAELoader", "inputs": {"vae_name": "ace_1.5_vae.safetensors"}},
        "5": {"class_type": "TextEncodeAceStepAudio1.5", "inputs": {
            "clip": ["3", 0], "tags": tags, "lyrics": "[Instrumental]", "seed": seed, "bpm": bpm,
            "duration": segundos, "timesignature": "4", "language": "en", "keyscale": tom,
            "generate_audio_codes": True, "cfg_scale": 2.0, "temperature": 0.85, "top_p": 0.9, "top_k": 0,
            "min_p": 0.0}},
        "6": {"class_type": "ConditioningZeroOut", "inputs": {"conditioning": ["5", 0]}},
        "7": {"class_type": "EmptyAceStep1.5LatentAudio", "inputs": {"seconds": segundos, "batch_size": 1}},
        "8": {"class_type": "KSampler", "inputs": {
            "model": ["2", 0], "positive": ["5", 0], "negative": ["6", 0], "latent_image": ["7", 0], "seed": seed,
            "steps": 8, "cfg": 1, "sampler_name": "euler", "scheduler": "simple", "denoise": 1}},
        "9": {"class_type": "VAEDecodeAudio", "inputs": {"samples": ["8", 0], "vae": ["4", 0]}},
        "10": {"class_type": "SaveAudio", "inputs": {"audio": ["9", 0], "filename_prefix": prefixo}},
    }


def rodar(wf: dict) -> Path:
    req = urllib.request.Request(f"{COMFY}/prompt", data=json.dumps({"prompt": wf}).encode(),
                                 headers={"Content-Type": "application/json"})
    pid = json.loads(urllib.request.urlopen(req).read())["prompt_id"]
    while True:
        time.sleep(3)
        hist = json.loads(urllib.request.urlopen(f"{COMFY}/history/{pid}").read())
        if pid in hist:
            h = hist[pid]
            if h.get("status", {}).get("status_str") == "error":
                raise RuntimeError(json.dumps(h["status"])[:2000])
            for saida in h["outputs"].values():
                for a in saida.get("audio", []):
                    return COMFY_OUT / a.get("subfolder", "") / a["filename"]


def main() -> None:
    args = sys.argv[1:]
    segundos_fixos = None
    if "--segundos" in args:
        i = args.index("--segundos")
        segundos_fixos = float(args[i + 1])
        del args[i : i + 2]
    pedidos = set(args)
    OUT.mkdir(parents=True, exist_ok=True)
    dur = duracao_blocos()
    for bloco, (tags, bpm, tom) in ESTILOS.items():
        destino = OUT / f"{bloco}.wav"
        if pedidos and bloco not in pedidos:
            continue
        if not pedidos and destino.exists():
            continue
        seg = segundos_fixos or round(dur[bloco])
        seed = random.randint(0, 2**31)
        t0 = time.time()
        arq = rodar(workflow(tags, bpm, tom, seg, seed, f"v7-trilha/{bloco}"))
        # SaveAudio grava FLAC na pasta de saída do ComfyUI
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(arq), str(destino)], check=True)
        log_path = OUT / "trilhas.json"
        log = json.loads(log_path.read_text(encoding="utf-8")) if log_path.exists() else {}
        log[bloco] = {"seed": seed, "segundos": seg, "tags": tags, "bpm": bpm, "tom": tom}
        log_path.write_text(json.dumps(log, indent=1, ensure_ascii=False), encoding="utf-8")
        print(bloco, seg, "s", round(time.time() - t0, 1), "s de geração", flush=True)


if __name__ == "__main__":
    main()
