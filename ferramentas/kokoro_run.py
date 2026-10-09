"""Gera narração com Kokoro-82M (Apache 2.0). Roda no venv C:/ai-local/venv-voz.

Uso:
  python kokoro_run.py --text-file roteiro.txt --out narracao.wav [--voice am_michael] [--speed 1.0]

Parágrafos (linhas em branco) viram pausas. Imprime JSON com duração e caminho no fim.
"""

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import soundfile as sf
from kokoro import KPipeline

SAMPLE_RATE = 24000


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--text-file", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--voice", default="am_michael")
    ap.add_argument("--speed", type=float, default=1.0)
    ap.add_argument("--lang", default="a", help="a = inglês americano, b = britânico")
    ap.add_argument("--pause", type=float, default=0.45, help="silêncio entre parágrafos (s)")
    args = ap.parse_args()

    text = Path(args.text_file).read_text(encoding="utf-8").strip()
    pipeline = KPipeline(lang_code=args.lang, repo_id="hexgrad/Kokoro-82M")
    silence = np.zeros(int(SAMPLE_RATE * args.pause), dtype=np.float32)

    chunks = []
    for paragraph in [p.strip() for p in text.split("\n\n") if p.strip()]:
        for _, _, audio in pipeline(paragraph, voice=args.voice, speed=args.speed):
            chunks.append(np.asarray(audio, dtype=np.float32))
        chunks.append(silence)

    if not chunks:
        print(json.dumps({"error": "texto vazio"}))
        return 1

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    wav = np.concatenate(chunks)
    sf.write(out, wav, SAMPLE_RATE)
    print(json.dumps({"output": str(out), "duration_seconds": round(len(wav) / SAMPLE_RATE, 2),
                      "voice": args.voice, "speed": args.speed}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
