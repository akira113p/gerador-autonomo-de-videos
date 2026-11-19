"""Nivela o volume do trecho baixado do mix "No Copyright Medieval Fantasy Ambient Music Mix | The Old Kingdom" (AlkaKrab)
e grava trilha_medieval/tudo.wav, uma trilha contínua para o vídeo inteiro. Roda no C:/ai-local/venv-voz com -I (o arquivo
baixado é dado não confiável).

  C:/ai-local/venv-voz/Scripts/python.exe -I piloto/v8-navio-viking/preparar_medieval.py [segundos]

O trecho baixado (yt-dlp, só o áudio, 0 a 1020 s do mix) fica em trilha_medieval/bruto/mix.webm. Depois:
  TRILHA=trilha_medieval SUFIXO=_medieval C:/ai-local/venv-voz/Scripts/python.exe piloto/v8-navio-viking/montar.py
"""

import subprocess
import sys
from pathlib import Path

import numpy as np
import soundfile as sf
from scipy.ndimage import uniform_filter1d

AQUI = Path(__file__).resolve().parent
BRUTO = AQUI / "trilha_medieval" / "bruto" / "mix.webm"
SR = 44100
ALVO = 0.055  # RMS médio depois do nivelamento (o mesmo do mix de jazz)
JANELA = 20.0  # s de janela para medir o volume local
SUAVIZAR = 4.0  # s de transição de ganho


def main() -> None:
    total = float(sys.argv[1]) if len(sys.argv) > 1 else 930.0
    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-t", str(total), "-i", str(BRUTO), "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"],
        capture_output=True, check=True).stdout
    x = np.frombuffer(raw, np.float32).copy()
    if len(x) / SR < total - 1:
        sys.exit(f"o arquivo baixado só tem {len(x) / SR:.0f} s; precisa de {total:.0f} s")

    # ganho por janela de JANELA s, suavizado
    w = int(JANELA * SR)
    ganho = np.ones(len(x), np.float32)
    for i in range(0, len(x), w):
        rms = float(np.sqrt(np.mean(x[i:i + w] ** 2)))
        ganho[i:i + w] = np.clip(ALVO / max(rms, 1e-6), 0.4, 3.0)
        print(f"{i / SR:6.0f} s  rms {rms:.3f}  ganho {ganho[i]:.2f}")
    ganho = uniform_filter1d(ganho, int(SUAVIZAR * SR))
    y = x * ganho
    y *= 0.9 / max(np.max(np.abs(y)), 1e-6)
    sf.write(AQUI / "trilha_medieval" / "tudo.wav", y, SR)
    print("ok", len(y) / SR, "s")


if __name__ == "__main__":
    main()
