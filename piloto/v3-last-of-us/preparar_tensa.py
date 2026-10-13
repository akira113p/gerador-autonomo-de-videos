"""Corta o trecho da música de apocalipse baixada, nivela o volume (a coletânea tem faixas de volume muito diferente)
e grava trilha_tensa/tudo.wav. Roda no C:/ai-local/venv-voz com -I (o arquivo baixado é dado não confiável).

  C:/ai-local/venv-voz/Scripts/python.exe -I piloto/v3-last-of-us/preparar_tensa.py [segundos] [início em s]

Fonte: "Songs for the Collapse of Society (No AI)", Joe Mathews | Composer, https://www.youtube.com/watch?v=J5P4hy7q4TY
(obra autoral, sem licença livre informada; só para o vídeo privado de teste até haver permissão).
"""

import subprocess
import sys
from pathlib import Path

import numpy as np
import soundfile as sf
from scipy.ndimage import uniform_filter1d

AQUI = Path(__file__).resolve().parent
BRUTO = AQUI / "trilha_tensa" / "bruto" / "colapso_30min.webm"
SR = 44100
ALVO = 0.055  # RMS médio depois do nivelamento (igual ao jazz)
JANELA, SUAVIZAR = 8.0, 6.0  # s: janela de medida do volume e suavização do ganho


def main() -> None:
    total = float(sys.argv[1]) if len(sys.argv) > 1 else 1050.0
    ini = float(sys.argv[2]) if len(sys.argv) > 2 else 0.0
    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-ss", str(ini), "-t", str(total), "-i", str(BRUTO), "-f", "f32le", "-ac", "1",
         "-ar", str(SR), "-"], capture_output=True, check=True).stdout
    x = np.frombuffer(raw, np.float32).copy()
    if len(x) / SR < total - 1:
        sys.exit(f"o arquivo só tem {len(x) / SR:.0f} s a partir de {ini:.0f} s; precisa de {total:.0f} s")
    w = int(JANELA * SR)
    ganho = np.ones(len(x), np.float32)
    for i in range(0, len(x), w):
        seg = x[i : i + w]
        rms = float(np.sqrt(np.mean(seg ** 2)))
        ganho[i : i + w] = np.clip(ALVO / max(rms, 1e-6), 0.12, 3.0)
    ganho = uniform_filter1d(ganho, int(SUAVIZAR * SR))
    y = x * ganho
    y *= 0.9 / max(np.max(np.abs(y)), 1e-6)
    (AQUI / "trilha_tensa").mkdir(exist_ok=True)
    sf.write(AQUI / "trilha_tensa" / "tudo.wav", y, SR)
    r = np.sqrt(np.mean(y[: int(60 * SR)] ** 2))
    print("ok", len(y) / SR, "s; rms médio", round(float(np.sqrt(np.mean(y ** 2))), 3), "primeiro minuto", round(float(r), 3))


if __name__ == "__main__":
    main()
