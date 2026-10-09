"""Edição simples: imagem por cena com zoom lento, voz, efeitos e música com ducking. Roda no C:/ai-local/venv-voz.

  C:/ai-local/venv-voz/Scripts/python.exe piloto/v1-vindolanda/montar.py

Precisa de imagens/, voz/ (com duracoes.json) e trilha/ nesta pasta.
Saída: piloto_v1.mp4 (AAC, para publicar) e piloto_v1_vscode.mp4 (Opus, toca no preview do VS Code).
"""

import json
import subprocess
from pathlib import Path

import numpy as np
import soundfile as sf
from scipy.ndimage import uniform_filter1d
from scipy.signal import resample_poly

AQUI = Path(__file__).resolve().parent
BASE = AQUI
SFX_LIB = Path("D:/programacao/projetos/videos/openmontage/.agents/skills/hyperframes-media/assets/sfx")
SR, FPS = 44100, 30
# LEAD: música antes da 1ª fala. GAP: pausa entre cenas; PRE dela fica antes da fala (a imagem entra antes da voz).
LEAD, GAP, PRE, TAIL, PIADA = 1.2, 0.45, 0.25, 3.5, 1.8

# efeito -> (arquivo, ganho)
SFX = {
    "pop": (SFX_LIB / "pop.mp3", 0.35),
    "whoosh": (SFX_LIB / "whoosh-short.mp3", 0.30),
    "sino": (SFX_LIB / "chime.mp3", 0.30),
    "batida": (BASE / "trilha/trombone.wav", 0.40),
    "vento": (BASE / "trilha/vento.wav", 0.22),
}


def ler(path: Path) -> np.ndarray:
    """Lê qualquer áudio como mono float32 em SR (mp3 via ffmpeg)."""
    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", str(path), "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"],
        capture_output=True, check=True,
    ).stdout
    return np.frombuffer(raw, np.float32).copy()


def somar(trilha: np.ndarray, som: np.ndarray, inicio: float, ganho: float = 1.0) -> None:
    i = int(inicio * SR)
    n = min(len(som), len(trilha) - i)
    if n > 0:
        trilha[i : i + n] += som[:n] * ganho


def main() -> None:
    cenas = json.loads((AQUI / "roteiro.json").read_text(encoding="utf-8"))["cenas"]
    dur = json.loads((BASE / "voz/duracoes.json").read_text(encoding="utf-8"))

    # tempo de cada cena em quadros inteiros, para áudio e vídeo baterem
    plano, t = [], 0
    for k, c in enumerate(cenas):
        d = dur[c["id"]] + GAP + (LEAD if k == 0 else 0) + (TAIL if k == len(cenas) - 1 else 0)
        d += PIADA if "batida" in c["sfx"] else 0
        quadros = round(d * FPS)
        plano.append({"cena": c, "inicio": t / FPS, "quadros": quadros, "voz": t / FPS + (LEAD if k == 0 else PRE)})
        t += quadros
    total = t / FPS
    n = int(total * SR)
    print(f"{len(cenas)} cenas, {total:.1f} s")

    voz, efeitos = np.zeros(n, np.float32), np.zeros(n, np.float32)
    for p in plano:
        c = p["cena"]
        w, sr = sf.read(BASE / f"voz/{c['id']}.wav", dtype="float32")
        if w.ndim > 1:
            w = w.mean(axis=1)
        if sr != SR:
            w = resample_poly(w, SR, sr).astype(np.float32)
        somar(voz, w, p["voz"])
        fim_voz = p["voz"] + len(w) / SR
        for nome in c["sfx"]:
            if nome not in SFX:
                continue
            arq, ganho = SFX[nome]
            som = ler(arq)
            if nome == "vento":
                somar(efeitos, som[: p["quadros"] * SR // FPS + SR], p["inicio"], ganho)
            elif nome == "batida":
                somar(efeitos, som, fim_voz + 0.1, ganho)
            else:
                somar(efeitos, som, max(p["inicio"] - 0.05, 0), ganho)

    voz /= max(np.max(np.abs(voz)), 1e-6) / 0.9

    # música: abaixa sob a voz (ducking) e sobe nas pausas e no fim
    musica = ler(BASE / "trilha/musica.wav")
    musica = np.pad(musica, (0, max(0, n - len(musica))))[:n]
    atividade = uniform_filter1d((np.abs(voz) > 0.02).astype(np.float32), int(0.6 * SR))
    ganho = 0.32 - 0.20 * np.clip(atividade * 3, 0, 1)
    ganho = uniform_filter1d(ganho, int(0.3 * SR))
    final_ini = plano[-1]["inicio"]
    ts = np.arange(n) / SR
    ganho = np.where(ts > final_ini + dur[plano[-1]["cena"]["id"]], np.maximum(ganho, 0.45), ganho)
    fade = np.clip((total - ts) / 2.5, 0, 1)
    mix = voz + efeitos + musica * ganho * fade
    mix /= max(np.max(np.abs(mix)), 1e-6) / 0.95
    sf.write(BASE / "audio_mix_bruto.wav", mix, SR)

    # vídeo: um clipe por cena com zoom lento (alterna entrar e sair)
    clipes = BASE / "clipes"
    clipes.mkdir(exist_ok=True)
    lista = []
    for k, p in enumerate(plano):
        cid, q = p["cena"]["id"], p["quadros"]
        z = f"1+0.07*on/{q}" if k % 2 == 0 else f"1.07-0.07*on/{q}"
        vf = (
            f"scale=3840:-2,crop=3840:2160,"
            f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={q}:s=1920x1080:fps={FPS},"
            f"format=yuv420p"
        )
        out = clipes / f"{cid}.mp4"
        subprocess.run(
            ["ffmpeg", "-y", "-v", "error", "-i", str(BASE / f"imagens/{cid}.png"), "-vf", vf,
             "-frames:v", str(q), "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-r", str(FPS), str(out)],
            check=True,
        )
        lista.append(f"file '{out.as_posix()}'")
        print("clipe", cid, q, flush=True)
    (BASE / "lista.txt").write_text("\n".join(lista), encoding="utf-8")

    # mix final em estéreo 48 kHz, normalizado para o YouTube (-14 LUFS)
    subprocess.run(
        ["ffmpeg", "-y", "-v", "error", "-i", str(BASE / "audio_mix_bruto.wav"),
         "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-ac", "2", "-ar", "48000", str(BASE / "audio_mix.wav")],
        check=True,
    )
    # AAC para YouTube e players comuns; Opus para o preview do VS Code, que não decodifica AAC
    for nome, audio in [("piloto_v1.mp4", ["-c:a", "aac", "-b:a", "192k"]),
                        ("piloto_v1_vscode.mp4", ["-c:a", "libopus", "-b:a", "160k"])]:
        subprocess.run(
            ["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(BASE / "lista.txt"),
             "-i", str(BASE / "audio_mix.wav"), "-map", "0:v", "-map", "1:a", "-c:v", "copy", *audio,
             "-movflags", "+faststart", str(BASE / nome)],
            check=True,
        )
        print("ok", BASE / nome)


if __name__ == "__main__":
    main()
