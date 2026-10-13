"""Recorta o ciclo de músicas do mix baixado, nivela o volume entre as faixas e grava trilha_jazz/tudo.wav.
Roda no C:/ai-local/venv-voz com -I (o arquivo baixado é dado não confiável).

  C:/ai-local/venv-voz/Scripts/python.exe -I piloto/v5-revolucao-francesa/preparar_jazz.py [segundos]

O mix de 12 h repete a mesma sequência de ~1000 s. O recorte começa no início de um ciclo (INICIO) e segue pela
sequência original, inclusive a volta ao começo, até cobrir o vídeo. Faixas (fronteiras medidas por analisar_jazz.py):
"""

import subprocess
import sys
from pathlib import Path

import numpy as np
import soundfile as sf
from scipy.ndimage import uniform_filter1d

AQUI = Path(__file__).resolve().parent
BRUTO = AQUI / "trilha_jazz" / "bruto" / "hora1.webm"
SR = 44100
INICIO, CICLO = 992.1, 999.8  # início do 2º ciclo no arquivo baixado e período de repetição
FRONTEIRAS = [0.0, 138.2, 254.8, 439.7, 625.4, 906.9, CICLO]  # dentro de um ciclo, a partir de INICIO
ALVO = 0.055  # RMS médio de cada faixa depois do nivelamento
SUAVIZAR = 4.0  # s de transição de ganho entre faixas


def main() -> None:
    total = float(sys.argv[1]) if len(sys.argv) > 1 else 1160.0
    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-ss", str(INICIO), "-t", str(total), "-i", str(BRUTO), "-f", "f32le", "-ac", "1",
         "-ar", str(SR), "-"], capture_output=True, check=True).stdout
    x = np.frombuffer(raw, np.float32).copy()
    if len(x) / SR < total - 1:
        sys.exit(f"o arquivo baixado só tem {len(x) / SR:.0f} s depois do início do ciclo; precisa de {total:.0f} s")

    ganho = np.ones(len(x), np.float32)
    ciclo = 0
    while ciclo * CICLO < total:
        for a, b in zip(FRONTEIRAS, FRONTEIRAS[1:]):
            i0, i1 = int((ciclo * CICLO + a) * SR), min(int((ciclo * CICLO + b) * SR), len(x))
            if i0 >= len(x):
                break
            rms = float(np.sqrt(np.mean(x[i0:i1] ** 2)))
            ganho[i0:i1] = np.clip(ALVO / max(rms, 1e-6), 0.4, 3.0)
            print(f"ciclo {ciclo} {a:6.1f}-{b:6.1f} s  rms {rms:.3f}  ganho {ganho[i0]:.2f}")
        ciclo += 1
    ganho = uniform_filter1d(ganho, int(SUAVIZAR * SR))
    y = x * ganho
    y *= 0.9 / max(np.max(np.abs(y)), 1e-6)
    sf.write(AQUI / "trilha_jazz" / "tudo.wav", y, SR)
    print("ok", len(y) / SR, "s")


if __name__ == "__main__":
    main()
