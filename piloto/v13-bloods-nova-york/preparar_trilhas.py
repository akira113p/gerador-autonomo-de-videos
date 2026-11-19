"""Corta e nivela as três trilhas do vídeo 13  a partir de trilhas/bruto/ e grava trilhas/<nome>.wav.
Roda no C:/ai-local/venv-voz com -I (os arquivos baixados são dados não confiáveis).

  C:/ai-local/venv-voz/Scripts/python.exe -I piloto/v13-bloods-nova-york/preparar_trilhas.py

Fontes e créditos (frases de "no copyright" em trilhas/bruto/*_descricao.txt):
- jazz: "Covert Affair", Kevin MacLeod (incompetech.com), CC BY 3.0, via MrSnooze (iYOvAO1rAM0), 9:11-12:26
- tensa: "Suspenseful", Soundridemusic (8abBSm3LZcs), crédito obrigatório: "Music: Suspenseful by #soundridemusic / Link to Video: https://youtu.be/8abBSm3LZcs"
- piano: "Isolated", via MrSnooze "Sad Piano Background Music" (FubpHGB4iq0), 0:00-3:32, crédito CC conforme a descrição
"""

import subprocess
from pathlib import Path

import numpy as np
import soundfile as sf
from scipy.ndimage import uniform_filter1d

AQUI = Path(__file__).resolve().parent
BRUTO = AQUI / "trilhas" / "bruto"
SR = 44100
ALVO = 0.055  # RMS médio depois do nivelamento (igual ao vídeo 3)
JANELA, SUAVIZAR = 8.0, 6.0
# nome: (arquivo, início s, duração s)
CORTES = {"jazz": ("jazz.webm", 551.0, 195.0), "tensa": ("tensa.webm", 0.0, 153.0), "piano": ("piano.webm", 0.0, 212.0)}


def main() -> None:
    for nome, (arq, ini, dur) in CORTES.items():
        raw = subprocess.run(
            ["ffmpeg", "-v", "error", "-ss", str(ini), "-t", str(dur), "-i", str(BRUTO / arq), "-f", "f32le",
             "-ac", "1", "-ar", str(SR), "-"], capture_output=True, check=True).stdout
        x = np.frombuffer(raw, np.float32).copy()
        w = int(JANELA * SR)
        ganho = np.ones(len(x), np.float32)
        for i in range(0, len(x), w):
            rms = float(np.sqrt(np.mean(x[i : i + w] ** 2)))
            ganho[i : i + w] = np.clip(ALVO / max(rms, 1e-6), 0.12, 3.0)
        y = x * uniform_filter1d(ganho, int(SUAVIZAR * SR))
        y *= 0.9 / max(np.max(np.abs(y)), 1e-6)
        sf.write(AQUI / "trilhas" / f"{nome}.wav", y, SR)
        print(nome, round(len(y) / SR, 1), "s")


if __name__ == "__main__":
    main()
