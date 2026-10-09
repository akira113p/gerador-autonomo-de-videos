"""Narração com Qwen3-TTS 1.7B (Apache 2.0). Roda no venv C:/ai-local/venv-qwen.

Modos:
  design: cria uma voz a partir de uma descrição e grava uma amostra curta (vira a referência do narrador).
    python qwen_tts_run.py design --text-file ref.txt --instruct "Male, 50s, deep British..." --out ref.wav
  clone: narra um texto longo com a voz de uma referência (a amostra do design ou uma gravação sua).
    python qwen_tts_run.py clone --text-file roteiro.txt --ref ref.wav --ref-text-file ref.txt --out narracao.wav

Texto longo é dividido em frases; parágrafos (linha em branco) viram pausas. Imprime JSON no fim.
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

import numpy as np
import soundfile as sf
import torch
from qwen_tts import Qwen3TTSModel

# Pastas comuns (sem symlink): o cache do HF falha no Windows sem modo de desenvolvedor.
MODELS_DIR = Path(os.environ.get("QWEN_TTS_DIR", "C:/ai-local/modelos"))
DESIGN_MODEL = str(MODELS_DIR / "Qwen3-TTS-12Hz-1.7B-VoiceDesign")
BASE_MODEL = str(MODELS_DIR / "Qwen3-TTS-12Hz-1.7B-Base")
MAX_CHARS = 300


def load(model_id: str) -> Qwen3TTSModel:
    return Qwen3TTSModel.from_pretrained(
        model_id, device_map="cuda:0", dtype=torch.bfloat16, attn_implementation="sdpa"
    )


def split_sentences(paragraph: str) -> list[str]:
    chunks, cur = [], ""
    for s in re.split(r"(?<=[.!?])\s+", paragraph.strip()):
        if cur and len(cur) + len(s) + 1 > MAX_CHARS:
            chunks.append(cur)
            cur = s
        else:
            cur = f"{cur} {s}".strip()
    if cur:
        chunks.append(cur)
    return chunks


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["design", "clone"])
    ap.add_argument("--text-file", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--language", default="English")
    ap.add_argument("--instruct", default="")
    ap.add_argument("--ref", default=None)
    ap.add_argument("--ref-text-file", default=None)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--pause", type=float, default=0.45)
    ap.add_argument("--sentence-gap", type=float, default=0.15)
    args = ap.parse_args()

    torch.manual_seed(args.seed)
    text = Path(args.text_file).read_text(encoding="utf-8").strip()
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    if args.mode == "design":
        model = load(DESIGN_MODEL)
        wavs, sr = model.generate_voice_design(text=text, language=args.language, instruct=args.instruct)
        wav = np.asarray(wavs[0], dtype=np.float32)
    else:
        model = load(BASE_MODEL)
        ref_text = Path(args.ref_text_file).read_text(encoding="utf-8").strip()
        prompt = model.create_voice_clone_prompt(ref_audio=args.ref, ref_text=ref_text)
        pieces, sr = [], None
        for paragraph in [p for p in text.split("\n\n") if p.strip()]:
            for sentence in split_sentences(paragraph):
                wavs, sr = model.generate_voice_clone(
                    text=sentence, language=args.language, voice_clone_prompt=prompt
                )
                pieces += [np.asarray(wavs[0], dtype=np.float32), np.zeros(int(sr * args.sentence_gap), np.float32)]
            pieces.append(np.zeros(int(sr * args.pause), np.float32))
        wav = np.concatenate(pieces)

    sf.write(out, wav, sr)
    print(json.dumps({"output": str(out), "mode": args.mode, "duration_seconds": round(len(wav) / sr, 2)}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
