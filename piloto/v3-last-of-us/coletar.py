"""Extrai as imagens baixadas do ChatGPT (Downloads/v3_lote*.tar, ou v3_NNN.png soltas) para imagens/NNN.png em 16:9.

  python piloto/v3-last-of-us/coletar.py

Guarda o original em imagens_gpt_original/ e lista as cenas que ainda faltam. Imagem nova da mesma cena sobrescreve.
"""

import io
import json
import shutil
import tarfile
from pathlib import Path

from PIL import Image

AQUI = Path(__file__).resolve().parent
DOWNLOADS = Path.home() / "Downloads"
OUT = AQUI / "imagens"
ORIG = AQUI / "imagens_gpt_original"


def salvar(nome: str, dados: bytes) -> None:
    cid = nome.replace("v3_", "").replace(".png", "")
    (ORIG / f"{cid}.png").write_bytes(dados)
    img = Image.open(io.BytesIO(dados)).convert("RGB")
    w, h = img.size
    alvo_h = round(w * 9 / 16)
    if h > alvo_h + 2:  # corta o excesso para 16:9, centrado
        top = (h - alvo_h) // 2
        img = img.crop((0, top, w, top + alvo_h))
    img.save(OUT / f"{cid}.png")


def main() -> None:
    OUT.mkdir(exist_ok=True)
    ORIG.mkdir(exist_ok=True)
    n = 0
    for t in sorted(DOWNLOADS.glob("v3_lote*.tar")):
        with tarfile.open(t) as tf:
            for m in tf.getmembers():
                if m.isfile() and m.name.endswith(".png"):
                    salvar(m.name, tf.extractfile(m).read())
                    n += 1
        shutil.move(str(t), str(ORIG / t.name))
    for f in sorted(DOWNLOADS.glob("v3_[0-9][0-9][0-9].png")):
        salvar(f.name, f.read_bytes())
        f.unlink()
        n += 1
    cenas = json.loads((AQUI / "roteiro.json").read_text(encoding="utf-8"))["cenas"]
    faltam = [c["id"] for c in cenas if not (OUT / f"{c['id']}.png").exists()]
    print(f"{n} coletadas; {len(cenas) - len(faltam)}/{len(cenas)} prontas; faltam: {' '.join(faltam) if len(faltam) < 40 else str(len(faltam)) + ' cenas'}")


if __name__ == "__main__":
    main()
