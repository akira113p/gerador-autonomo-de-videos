"""Narra cada cena do roteiro com o clone do professor idoso (Qwen3-TTS Base). Roda no C:/ai-local/venv-qwen.

  C:/ai-local/venv-qwen/Scripts/python.exe piloto/v1-vindolanda/gerar_voz.py [ids...]

Grava um WAV por cena e duracoes.json (a duração de cada cena manda no tempo da imagem).
"""

import json
import sys
from pathlib import Path

import numpy as np
import soundfile as sf
import torch

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[1]
sys.path.insert(0, str(RAIZ / "ferramentas"))
from qwen_tts_run import BASE_MODEL, load  # noqa: E402

OUT = AQUI / "voz"
VOZ = RAIZ / "identidade" / "narrador-professor"


def main() -> None:
    roteiro = json.loads((AQUI / "roteiro.json").read_text(encoding="utf-8"))
    pedidos = set(sys.argv[1:])
    OUT.mkdir(parents=True, exist_ok=True)
    dur_path = OUT / "duracoes.json"
    duracoes = json.loads(dur_path.read_text(encoding="utf-8")) if dur_path.exists() else {}

    model = load(BASE_MODEL)
    ref_text = (VOZ / "narrador_ref.txt").read_text(encoding="utf-8").strip()
    prompt = model.create_voice_clone_prompt(ref_audio=str(VOZ / "narrador_ref.wav"), ref_text=ref_text)
    for cena in roteiro["cenas"]:
        cid = cena["id"]
        if pedidos and cid not in pedidos:
            continue
        torch.manual_seed(42 + int(cid) + (100 if pedidos else 0))
        wavs, sr = model.generate_voice_clone(text=cena["texto"], language="English", voice_clone_prompt=prompt)
        wav = np.asarray(wavs[0], dtype=np.float32)
        sf.write(OUT / f"{cid}.wav", wav, sr)
        duracoes[cid] = round(len(wav) / sr, 3)
        dur_path.write_text(json.dumps(duracoes, indent=1), encoding="utf-8")
        print(cid, duracoes[cid], flush=True)
    print("total", round(sum(duracoes.values()), 1))


if __name__ == "__main__":
    main()
