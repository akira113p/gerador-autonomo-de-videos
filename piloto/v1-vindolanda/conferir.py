"""Transcreve a voz de cada cena com Whisper e compara com o roteiro (pega palavra pulada ou trocada).
Roda no C:/ai-local/venv-voz.

  C:/ai-local/venv-voz/Scripts/python.exe piloto/v1-vindolanda/conferir.py

DIF por nome próprio ou número escrito diferente é normal; ouça só as cenas com palavra faltando.
"""

import json
import os
import re
from pathlib import Path

import torch

# CTranslate2 carrega cublas64_12.dll pelo PATH; o torch cu124 traz a DLL em torch/lib.
os.environ["PATH"] = str(Path(torch.__file__).parent / "lib") + os.pathsep + os.environ["PATH"]

import librosa  # noqa: E402
from faster_whisper import WhisperModel  # noqa: E402

AQUI = Path(__file__).resolve().parent


def norm(s: str) -> list[str]:
    return re.sub(r"[^a-z0-9 ]", "", s.lower().replace("-", " ")).split()


def main() -> None:
    roteiro = json.loads((AQUI / "roteiro.json").read_text(encoding="utf-8"))
    model = WhisperModel("large-v3-turbo", device="cuda", compute_type="float16")
    for c in roteiro["cenas"]:
        audio = librosa.load(AQUI / f"voz/{c['id']}.wav", sr=16000)[0]
        segs, _ = model.transcribe(audio, language="en")
        texto = " ".join(s.text.strip() for s in segs)
        ok = norm(texto) == norm(c["texto"])
        print(c["id"], "OK " if ok else "DIF", "" if ok else texto)


if __name__ == "__main__":
    main()
