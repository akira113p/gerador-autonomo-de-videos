"""Edição do vídeo 8: imagem parada por cena (sem zoom, corte seco), voz, efeitos e uma trilha por bloco de capítulos,
com crossfade entre blocos e ducking sob a voz. Roda no C:/ai-local/venv-voz.

  C:/ai-local/venv-voz/Scripts/python.exe piloto/v8-navio-viking/montar.py

Precisa de roteiro.json, imagens/, voz/ (com duracoes.json) e trilha/<bloco>.wav.
Saída: video_v8.mp4 (AAC, para publicar), video_v8_vscode.mp4 (Opus, toca no preview do VS Code),
legendas_en.srt (para subir no YouTube) e tempos.json (início de cada cena e capítulo, para a descrição).
"""

import json
import os
import subprocess
from pathlib import Path

import numpy as np
import soundfile as sf
from scipy.ndimage import uniform_filter1d
from scipy.signal import resample_poly

AQUI = Path(__file__).resolve().parent
# TRILHA=trilha_jazz SUFIXO=_jazz: usa outra pasta de músicas (com tudo.wav = uma trilha contínua) e outros nomes de saída
TRILHA = AQUI / os.environ.get("TRILHA", "trilha")
SUFIXO = os.environ.get("SUFIXO", "")
SFX_LIB = Path("D:/programacao/projetos/videos/openmontage/.agents/skills/hyperframes-media/assets/sfx")
SR, FPS = 44100, 30
# LEAD: música antes da 1ª fala. GAP: pausa entre cenas; PRE dela fica antes da fala (a imagem entra antes da voz).
# CAP: respiro só de música no começo de cada capítulo. XFADE: troca de trilha entre blocos.
LEAD, GAP, PRE, CAP, TAIL, XFADE = 2.0, 0.45, 0.25, 1.6, 4.0, 3.0
# tela final: só música, fundo para os elementos finais do YouTube (o Studio aceita 5 a 20 s no fim)
TELA_FINAL = AQUI.parents[1] / "identidade" / "pocket-history" / "tela_final.png"
SEG_TELA_FINAL = 15.0

SFX = {
    "pop": (SFX_LIB / "pop.mp3", 0.22),  # cartões explicativos
    "whoosh": (SFX_LIB / "whoosh-short.mp3", 0.25),  # virada de capítulo
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


def esticar(musica: np.ndarray, n: int) -> np.ndarray:
    """Repete a trilha com crossfade até ter n amostras (para bloco mais longo que a música gerada)."""
    x = int(XFADE * SR)
    out = musica.copy()
    while len(out) < n:
        rampa = np.linspace(0, 1, x, dtype=np.float32)
        out[-x:] = out[-x:] * (1 - rampa) + musica[:x] * rampa
        out = np.concatenate([out, musica[x:]])
    return out[:n]


def saida(nome: str) -> Path:
    base, ext = os.path.splitext(nome)
    return AQUI / f"{base}{SUFIXO}{ext}"


def srt_tempo(s: float) -> str:
    ms = int(round(s * 1000))
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


def main() -> None:
    cenas = json.loads((AQUI / "roteiro.json").read_text(encoding="utf-8"))["cenas"]
    dur = json.loads((AQUI / "voz/duracoes.json").read_text(encoding="utf-8"))

    # tempo de cada cena em quadros inteiros, para áudio e vídeo baterem
    plano, t = [], 0
    for k, c in enumerate(cenas):
        antes = LEAD if k == 0 else (CAP if c["inicio_capitulo"] else PRE)
        d = antes + dur[c["id"]] + GAP - PRE + (TAIL if k == len(cenas) - 1 else 0)
        quadros = round(d * FPS)
        plano.append({"cena": c, "inicio": t / FPS, "quadros": quadros, "voz": t / FPS + antes})
        t += quadros
    quadros_fim = round(SEG_TELA_FINAL * FPS) if TELA_FINAL.exists() else 0
    t += quadros_fim
    total = t / FPS
    n = int(total * SR)
    print(f"{len(cenas)} cenas, {total / 60:.1f} min")

    voz, efeitos = np.zeros(n, np.float32), np.zeros(n, np.float32)
    srt = []
    for i, p in enumerate(plano):
        c = p["cena"]
        w, sr = sf.read(AQUI / f"voz/{c['id']}.wav", dtype="float32")
        if w.ndim > 1:
            w = w.mean(axis=1)
        if sr != SR:
            w = resample_poly(w, SR, sr).astype(np.float32)
        somar(voz, w, p["voz"])
        srt.append(f"{i + 1}\n{srt_tempo(p['voz'])} --> {srt_tempo(p['voz'] + len(w) / SR)}\n{c['texto']}\n")
        if c["cartao"]:
            arq, g = SFX["pop"]
            somar(efeitos, ler(arq), max(p["inicio"] - 0.05, 0), g)
        if c["inicio_capitulo"] and i > 0:
            arq, g = SFX["whoosh"]
            somar(efeitos, ler(arq), max(p["inicio"] - 0.15, 0), g)
    saida("legendas_en.srt").write_text("\n".join(srt), encoding="utf-8")
    voz /= max(np.max(np.abs(voz)), 1e-6) / 0.9

    # música: um trecho por bloco, entrando XFADE antes da virada e com fade cruzado
    blocos = []
    if (TRILHA / "tudo.wav").exists():  # uma trilha contínua para o vídeo inteiro (nivelada em preparar_jazz.py)
        blocos = [{"nome": "tudo", "inicio": 0.0}]
        plano_blocos = []
    else:
        plano_blocos = plano
    for p in plano_blocos:
        b = p["cena"]["bloco"]
        if not blocos or blocos[-1]["nome"] != b:
            blocos.append({"nome": b, "inicio": p["inicio"]})
    for a, b in zip(blocos, blocos[1:] + [{"inicio": total}]):
        a["fim"] = b["inicio"]
    musica = np.zeros(n, np.float32)
    xf = int(XFADE * SR)
    for k, b in enumerate(blocos):
        i0 = max(int(b["inicio"] * SR) - (xf if k else 0), 0)
        i1 = min(int(b["fim"] * SR) + (xf if k < len(blocos) - 1 else 0), n)
        trecho = ler(TRILHA / f"{b['nome']}.wav")
        trecho = esticar(trecho / max(np.max(np.abs(trecho)), 1e-6), i1 - i0)
        env = np.ones(i1 - i0, np.float32)
        if k:
            env[:xf] = np.linspace(0, 1, xf)
        if k < len(blocos) - 1:
            env[-xf:] = np.linspace(1, 0, xf)
        musica[i0:i1] += trecho * env
        print("trilha", b["nome"], f"{b['inicio']:.0f}-{b['fim']:.0f} s")

    # ducking: abaixa sob a voz e sobe nas pausas, nos respiros de capítulo e no fim
    atividade = uniform_filter1d((np.abs(voz) > 0.02).astype(np.float32), int(0.6 * SR))
    ganho = 0.34 - 0.22 * np.clip(atividade * 3, 0, 1)
    ganho = uniform_filter1d(ganho, int(0.3 * SR))
    ts = np.arange(n) / SR
    fim_voz = plano[-1]["voz"] + dur[plano[-1]["cena"]["id"]]
    ganho = np.where(ts > fim_voz, np.maximum(ganho, 0.45), ganho)
    fade = np.clip((total - ts) / 3.0, 0, 1) * np.clip(ts / 1.0, 0, 1)
    mix = voz + efeitos + musica * ganho * fade
    mix /= max(np.max(np.abs(mix)), 1e-6) / 0.95
    sf.write(saida("audio_mix_bruto.wav"), mix, SR)

    # vídeo: imagens paradas via concat (duração exata em quadros), escaladas para 1080p, um único encode
    linhas = []
    for p in plano:
        linhas += [f"file '{(AQUI / 'imagens' / (p['cena']['id'] + '.png')).as_posix()}'",
                   f"duration {p['quadros'] / FPS:.6f}"]
    if quadros_fim:
        linhas += [f"file '{TELA_FINAL.as_posix()}'", f"duration {quadros_fim / FPS:.6f}"]
    linhas.append(linhas[-2])  # o concat ignora a duração do último arquivo se ele não se repetir
    saida("lista.txt").write_text("\n".join(linhas), encoding="utf-8")
    subprocess.run(
        ["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(saida("lista.txt")),
         "-vf", f"scale=1920:1080:flags=lanczos,fps={FPS},format=yuv420p", "-frames:v", str(t),
         "-c:v", "libx264", "-preset", "medium", "-tune", "stillimage", "-crf", "18", str(saida("video_mudo.mp4"))],
        check=True,
    )

    # mix final em estéreo 48 kHz, normalizado para o YouTube (-14 LUFS)
    subprocess.run(
        ["ffmpeg", "-y", "-v", "error", "-i", str(saida("audio_mix_bruto.wav")),
         "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-ac", "2", "-ar", "48000", str(saida("audio_mix.wav"))],
        check=True,
    )
    for nome, audio in [(saida("video_v8.mp4"), ["-c:a", "aac", "-b:a", "192k"]),
                        (saida("video_v8_vscode.mp4"), ["-c:a", "libopus", "-b:a", "160k"])]:
        subprocess.run(
            ["ffmpeg", "-y", "-v", "error", "-i", str(saida("video_mudo.mp4")), "-i", str(saida("audio_mix.wav")),
             "-map", "0:v", "-map", "1:a", "-c:v", "copy", *audio, "-shortest", "-movflags", "+faststart",
             str(nome)],
            check=True,
        )
        print("ok", nome)

    tempos = {
        "cenas": {p["cena"]["id"]: round(p["inicio"], 2) for p in plano},
        "capitulos": [{"capitulo": p["cena"]["nome_capitulo"], "inicio": round(p["inicio"], 2)}
                      for p in plano if p["cena"]["inicio_capitulo"]],
        "blocos": [{k: (round(v, 2) if isinstance(v, float) else v) for k, v in b.items()} for b in blocos],
    }
    saida("tempos.json").write_text(json.dumps(tempos, indent=1, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
