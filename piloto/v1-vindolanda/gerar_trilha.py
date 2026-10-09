"""Música e efeitos sintetizados em código (sem licença de terceiros). Roda no C:/ai-local/venv-voz.

  C:/ai-local/venv-voz/Scripts/python.exe piloto/v1-vindolanda/gerar_trilha.py [segundos]

musica.wav: lira dedilhada (Karplus-Strong) em ré menor sobre um bordão grave, com reverb.
vento.wav: ruído marrom filtrado com rajadas lentas. trombone.wav: "wah-wah" triste para piada.
"""

import sys
from pathlib import Path

import numpy as np
import soundfile as sf
from scipy.signal import butter, fftconvolve, sosfilt

SR = 44100
OUT = Path(__file__).resolve().parent / "trilha"
rng = np.random.default_rng(7)


def hz(midi: float) -> float:
    return 440.0 * 2 ** ((midi - 69) / 12)


def pluck(freq: float, dur: float, brilho: float = 0.5) -> np.ndarray:
    """Corda dedilhada (Karplus-Strong)."""
    n = int(SR * dur)
    p = int(SR / freq)
    buf = rng.uniform(-1, 1, p)
    buf = sosfilt(butter(1, 1500 + 4000 * brilho, fs=SR, output="sos"), buf)
    blocos = []
    for _ in range(n // p + 1):  # um período por vez: média de vizinhos amortecida
        blocos.append(buf)
        buf = 0.4985 * (buf + np.roll(buf, -1))
    out = np.concatenate(blocos)[:n]
    return out * np.exp(-np.linspace(0, 3, n))


def reverb(x: np.ndarray, seg: float = 2.8, mix: float = 0.35) -> np.ndarray:
    n = int(SR * seg)
    ir = rng.standard_normal(n) * np.exp(-np.linspace(0, 7, n))
    ir = sosfilt(butter(2, 3500, fs=SR, output="sos"), ir)
    wet = fftconvolve(x, ir)[: len(x)]
    wet /= np.max(np.abs(wet)) + 1e-9
    return (1 - mix) * x / (np.max(np.abs(x)) + 1e-9) + mix * wet


def musica(total: float) -> np.ndarray:
    bpm = 66
    colcheia = 60 / bpm / 2
    # i - VII - VI - VII em ré menor (Dm, C, Bb, C), dois compassos cada
    acordes = [[50, 53, 57, 62, 65], [48, 52, 55, 60, 64], [46, 50, 53, 58, 62], [48, 52, 55, 60, 64]]
    baixos = [38, 36, 34, 36]
    padrao = [0, 2, 1, 3, 2, 4, 3, 1]
    n = int(SR * total)
    x = np.zeros(n + SR * 4)
    t, passo = 0.0, 0
    while t < total:
        bloco = (passo // 16) % 4
        nota = acordes[bloco][padrao[passo % 8]]
        if rng.random() < 0.15 and passo % 8 == 7:
            nota += 12  # ornamento ocasional uma oitava acima
        s = pluck(hz(nota), 2.2, brilho=rng.uniform(0.3, 0.6)) * rng.uniform(0.45, 0.7)
        i = int(t * SR + rng.normal(0, 0.006) * SR)
        i = max(i, 0)
        x[i : i + len(s)] += s
        if passo % 16 == 0:  # bordão no início de cada acorde
            b = pluck(hz(baixos[bloco]), 4.5, brilho=0.2) * 0.9
            x[i : i + len(b)] += b
        t += colcheia
        passo += 1
    x = x[:n]
    tt = np.arange(n) / SR
    drone = 0.06 * (np.sin(2 * np.pi * hz(38) * tt) + 0.5 * np.sin(2 * np.pi * hz(45) * tt))
    drone *= 0.7 + 0.3 * np.sin(2 * np.pi * 0.07 * tt)
    x = reverb(x) + drone
    fade = np.ones(n)
    fi, fo = int(SR * 3), int(SR * 5)
    fade[:fi] = np.linspace(0, 1, fi)
    fade[-fo:] = np.linspace(1, 0, fo)
    x *= fade
    return x / np.max(np.abs(x)) * 0.8


def vento(dur: float = 10.0) -> np.ndarray:
    n = int(SR * dur)
    br = np.cumsum(rng.standard_normal(n))
    x = sosfilt(butter(2, [150, 900], "band", fs=SR, output="sos"), br)
    t = np.arange(n) / SR
    rajada = 0.55 + 0.45 * np.sin(2 * np.pi * 0.13 * t + 1) * np.sin(2 * np.pi * 0.31 * t)
    x *= rajada
    env = np.minimum(1, np.minimum(t / 1.5, (dur - t) / 2.0))
    x *= np.clip(env, 0, 1)
    return x / np.max(np.abs(x)) * 0.8


def trombone() -> np.ndarray:
    partes = []
    for nota, dur in [(58, 0.38), (57, 0.38), (56, 0.38), (55, 1.1)]:
        n = int(SR * dur)
        t = np.arange(n) / SR
        vib = 1 + (0.012 * np.sin(2 * np.pi * 5.5 * t) if dur > 1 else 0)
        fase = 2 * np.pi * np.cumsum(hz(nota - 12) * vib) / SR
        onda = sum(np.sin(k * fase) / k for k in range(1, 12))
        wah = sosfilt(butter(2, 1200, fs=SR, output="sos"), onda)
        env = np.minimum(1, t / 0.04) * np.minimum(1, (dur - t) / 0.08)
        partes.append(wah * env)
    x = reverb(np.concatenate(partes), seg=1.2, mix=0.2)
    return x / np.max(np.abs(x)) * 0.7


def main() -> None:
    total = float(sys.argv[1]) if len(sys.argv) > 1 else 140.0
    OUT.mkdir(parents=True, exist_ok=True)
    sf.write(OUT / "musica.wav", musica(total), SR)
    sf.write(OUT / "vento.wav", vento(), SR)
    sf.write(OUT / "trombone.wav", trombone(), SR)
    print("ok", total)


if __name__ == "__main__":
    main()
