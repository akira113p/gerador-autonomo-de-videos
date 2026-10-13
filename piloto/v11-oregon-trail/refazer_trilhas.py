"""Regera trilhas com buraco de silêncio (RMS < 30% da mediana em janela de 2 s, fora dos 4 s finais) até ficarem limpas.
  python refazer_trilhas.py [blocos...]   (precisa de venv com soundfile/numpy: C:/ai-local/venv-voz)"""
import subprocess, sys
from pathlib import Path
import numpy as np, soundfile as sf
A = Path(__file__).resolve().parent
def buracos(f):
    x, sr = sf.read(f, dtype="float32"); x = x.mean(1) if x.ndim > 1 else x
    w = int(sr * 2); r = np.array([np.sqrt(np.mean(x[i:i + w] ** 2)) for i in range(0, len(x) - w, w)])
    med = np.median(r); n = len(r)
    return [i * 2 for i, v in enumerate(r) if v < 0.3 * med and 2 <= i < n - 3]
blocos = sys.argv[1:] or [f.stem for f in sorted((A / "trilha").glob("*.wav"))]
for b in blocos:
    for t in range(6):
        h = buracos(A / "trilha" / f"{b}.wav")
        print(b, "buracos:", h, flush=True)
        if not h: break
        subprocess.run(["C:/ai-local/venv-voz/Scripts/python.exe", str(A / "gerar_trilha.py"), b], check=True)
