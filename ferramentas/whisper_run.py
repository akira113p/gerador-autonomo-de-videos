"""Transcreve áudio com faster-whisper e grava JSON com tempo por palavra e um .srt.
Roda no venv C:/ai-local/venv-voz.

Uso:
  python whisper_run.py --audio narracao.wav --out-json palavras.json [--out-srt legendas.srt]
      [--model large-v3-turbo]

Serve para: legendas, sincronizar cortes com a fala e conferir se a voz sintética pulou palavras.
"""

import argparse
import json
import os
import sys
from pathlib import Path

import torch

# CTranslate2 carrega cublas64_12.dll pelo PATH; o torch cu124 traz a DLL em torch/lib.
os.environ["PATH"] = str(Path(torch.__file__).parent / "lib") + os.pathsep + os.environ["PATH"]

import librosa  # noqa: E402
from faster_whisper import WhisperModel  # noqa: E402


def srt_time(t: float) -> str:
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--audio", required=True)
    ap.add_argument("--out-json", required=True)
    ap.add_argument("--out-srt", default=None)
    ap.add_argument("--model", default="large-v3-turbo")
    ap.add_argument("--language", default="en")
    args = ap.parse_args()

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = WhisperModel(args.model, device=device, compute_type="float16" if device == "cuda" else "int8")
    # faster-whisper decodifica com PyAV; a versão instalada é incompatível, então carrego com librosa.
    audio, _ = librosa.load(args.audio, sr=16000)
    segments, _ = model.transcribe(audio, language=args.language, word_timestamps=True)

    segs = []
    for s in segments:
        segs.append({
            "start": round(s.start, 3), "end": round(s.end, 3), "text": s.text.strip(),
            "words": [{"start": round(w.start, 3), "end": round(w.end, 3), "word": w.word.strip()}
                      for w in (s.words or [])],
        })

    out = Path(args.out_json)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"segments": segs}, ensure_ascii=False, indent=1), encoding="utf-8")

    if args.out_srt:
        lines = []
        for i, s in enumerate(segs, 1):
            lines += [str(i), f"{srt_time(s['start'])} --> {srt_time(s['end'])}", s["text"], ""]
        Path(args.out_srt).write_text("\n".join(lines), encoding="utf-8")

    print(json.dumps({"output": str(out), "segments": len(segs),
                      "text": " ".join(s["text"] for s in segs)}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
