"""Acha as fronteiras entre as músicas do mix baixado e mede andamento e energia de cada uma.
Roda no C:/ai-local/venv-voz com -I (o arquivo baixado é dado não confiável; o script fica em outra pasta).

  C:/ai-local/venv-voz/Scripts/python.exe -I piloto/v2-dia-em-roma/analisar_jazz.py <arquivo-baixado>

Grava trilha_jazz/faixas.json: lista de faixas com início, fim, andamento (BPM) e RMS médio.
"""

import json
import subprocess
import sys
from pathlib import Path

import librosa
import numpy as np

AQUI = Path(__file__).resolve().parent
SR = 22050


def decodificar(path: Path) -> np.ndarray:
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32)


def main() -> None:
    x = decodificar(Path(sys.argv[1]))
    dur = len(x) / SR
    hop = 512
    rms = librosa.feature.rms(y=x, frame_length=2048, hop_length=hop)[0]
    t = librosa.frames_to_time(np.arange(len(rms)), sr=SR, hop_length=hop)

    # candidatos a fronteira: trechos quase silenciosos (corte entre faixas) e mudanças bruscas de timbre
    limiar = max(np.percentile(rms, 5) * 1.5, 0.003)
    baixo = rms < limiar
    cortes = []
    i = 0
    while i < len(baixo):
        if baixo[i]:
            j = i
            while j < len(baixo) and baixo[j]:
                j += 1
            if t[min(j, len(t) - 1)] - t[i] >= 0.25:
                cortes.append(float(t[(i + j) // 2]))
            i = j
        else:
            i += 1

    mfcc = librosa.feature.mfcc(y=x, sr=SR, n_mfcc=20, hop_length=hop * 8)
    janela = int(8 * SR / (hop * 8))  # 8 s de cada lado
    novidade = []
    for k in range(janela, mfcc.shape[1] - janela):
        a, b = mfcc[:, k - janela : k].mean(1), mfcc[:, k : k + janela].mean(1)
        novidade.append(float(np.linalg.norm(a - b)))
    novidade = np.array(novidade)
    tn = (np.arange(len(novidade)) + janela) * hop * 8 / SR
    picos = [float(tn[k]) for k in range(1, len(novidade) - 1)
             if novidade[k] > novidade[k - 1] and novidade[k] >= novidade[k + 1]
             and novidade[k] > np.percentile(novidade, 97)]

    fronteiras = sorted(set([0.0] + [round(c, 1) for c in cortes] + [round(p, 1) for p in picos] + [dur]))
    # funde fronteiras a menos de 45 s uma da outra (nenhuma música dessas é tão curta)
    f = [fronteiras[0]]
    for b in fronteiras[1:]:
        if b - f[-1] >= 45 or b == dur:
            f.append(b)
    faixas = []
    for a, b in zip(f, f[1:]):
        seg = x[int(a * SR) : int(b * SR)]
        if len(seg) < SR * 10:
            continue
        tempo = float(np.atleast_1d(librosa.beat.beat_track(y=seg, sr=SR)[0])[0])
        faixas.append({"inicio": round(a, 1), "fim": round(b, 1), "duracao": round(b - a, 1),
                       "bpm": round(tempo), "rms": round(float(np.sqrt(np.mean(seg ** 2))), 4),
                       "brilho": round(float(librosa.feature.spectral_centroid(y=seg, sr=SR).mean())), })
    (AQUI / "trilha_jazz" / "faixas.json").write_text(json.dumps(faixas, indent=1), encoding="utf-8")
    print(f"{dur:.0f} s analisados, {len(cortes)} silêncios, {len(picos)} picos de timbre, {len(faixas)} faixas")
    for k, fx in enumerate(faixas):
        print(f"{k:2d} {fx['inicio']:7.1f}-{fx['fim']:7.1f} ({fx['duracao']:5.1f}s) bpm {fx['bpm']:3d} rms {fx['rms']:.3f} "
              f"brilho {fx['brilho']}")


if __name__ == "__main__":
    main()
