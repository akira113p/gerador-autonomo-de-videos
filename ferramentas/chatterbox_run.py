"""Gera narração com Chatterbox (Resemble AI, MIT). Roda no venv C:/ai-local/venv-voz.

Uso:
  python chatterbox_run.py --text-file roteiro.txt --out narracao.wav [--ref voz_ref.wav]
      [--exaggeration 0.5] [--cfg 0.5] [--seed 42]

--ref clona o timbre de uma amostra de 5 a 15 s (ex.: a sua voz). Sem --ref usa a voz padrão.
Texto é dividido em frases (o modelo degrada em trechos longos). Parágrafos viram pausas.
"""

import argparse
import json
import re
import sys
from pathlib import Path

import torch
import torchaudio as ta
from chatterbox.tts import ChatterboxTTS

MAX_CHARS = 280


def split_sentences(paragraph: str) -> list[str]:
    sentences = re.split(r"(?<=[.!?])\s+", paragraph.strip())
    chunks, cur = [], ""
    for s in sentences:
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
    ap.add_argument("--text-file", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--ref", default=None)
    ap.add_argument("--exaggeration", type=float, default=0.5)
    ap.add_argument("--cfg", type=float, default=0.5)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--pause", type=float, default=0.45)
    ap.add_argument("--sentence-gap", type=float, default=0.12)
    args = ap.parse_args()

    torch.manual_seed(args.seed)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = ChatterboxTTS.from_pretrained(device=device)
    sr = model.sr

    text = Path(args.text_file).read_text(encoding="utf-8").strip()
    gap = torch.zeros(1, int(sr * args.sentence_gap))
    para_gap = torch.zeros(1, int(sr * args.pause))

    pieces = []
    for paragraph in [p for p in text.split("\n\n") if p.strip()]:
        for sentence in split_sentences(paragraph):
            wav = model.generate(
                sentence,
                audio_prompt_path=args.ref,
                exaggeration=args.exaggeration,
                cfg_weight=args.cfg,
            )
            pieces += [wav.cpu(), gap]
        pieces.append(para_gap)

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    full = torch.cat(pieces, dim=1)
    ta.save(str(out), full, sr)
    print(json.dumps({"output": str(out), "duration_seconds": round(full.shape[1] / sr, 2),
                      "ref": args.ref, "exaggeration": args.exaggeration, "cfg": args.cfg}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
