"""Corta um trecho do mix de jazz (o mesmo do vídeo 2), nivela o volume entre as faixas e grava trilha_jazz/tudo.wav.
Roda no C:/ai-local/venv-voz com -I (o arquivo baixado é dado não confiável).

  C:/ai-local/venv-voz/Scripts/python.exe -I piloto/v3-last-of-us/preparar_jazz.py [segundos] [faixa inicial 0-5]

O mix de 12 h repete a mesma sequência de 6 faixas (~1000 s). Cada vídeo começa numa faixa diferente (FAIXA) para a
música não ser igual entre os vídeos; a sequência segue a ordem original, inclusive a volta ao começo.
Fronteiras medidas por analisar_jazz.py (vídeo 2).
"""

import subprocess
import sys
from pathlib import Path

import numpy as np
import soundfile as sf
from scipy.ndimage import uniform_filter1d

AQUI = Path(__file__).resolve().parent
BRUTO = AQUI.parent / "v2-dia-em-roma" / "trilha_jazz" / "bruto" / "hora1.webm"
(AQUI / "trilha_jazz").mkdir(exist_ok=True)
SR = 44100
INICIO, CICLO = 992.1, 999.8  # início do 2º ciclo no arquivo baixado e período de repetição
FRONTEIRAS = [0.0, 138.2, 254.8, 439.7, 625.4, 906.9, CICLO]
ALVO = 0.055  # RMS médio de cada faixa depois do nivelamento
SUAVIZAR = 4.0  # s de transição de ganho entre faixas


def main() -> None:
    total = float(sys.argv[1]) if len(sys.argv) > 1 else 1100.0
    faixa = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    ini = INICIO + FRONTEIRAS[faixa]
    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-ss", str(ini), "-t", str(total), "-i", str(BRUTO), "-f", "f32le", "-ac", "1",
         "-ar", str(SR), "-"], capture_output=True, check=True).stdout
    x = np.frombuffer(raw, np.float32).copy()
    if len(x) / SR < total - 1:
        sys.exit(f"o arquivo só tem {len(x) / SR:.0f} s a partir da faixa {faixa}; precisa de {total:.0f} s")

    # fronteiras das faixas relativas ao início do recorte, seguindo a sequência ciclica
    limites, t = [], 0.0
    k = faixa
    while t < total:
        dur = FRONTEIRAS[k + 1] - FRONTEIRAS[k]
        limites.append((t, t + dur))
        t += dur
        k = (k + 1) % 6
    ganho = np.ones(len(x), np.float32)
    for a, b in limites:
        i0, i1 = int(a * SR), min(int(b * SR), len(x))
        if i0 >= len(x):
            break
        rms = float(np.sqrt(np.mean(x[i0:i1] ** 2)))
        ganho[i0:i1] = np.clip(ALVO / max(rms, 1e-6), 0.4, 3.0)
        print(f"{a:7.1f}-{b:7.1f} s  rms {rms:.3f}  ganho {ganho[i0]:.2f}")
    ganho = uniform_filter1d(ganho, int(SUAVIZAR * SR))
    y = x * ganho
    y *= 0.9 / max(np.max(np.abs(y)), 1e-6)
    sf.write(AQUI / "trilha_jazz" / "tudo.wav", y, SR)
    print("ok", len(y) / SR, "s, começando na faixa", faixa + 1)


if __name__ == "__main__":
    main()
