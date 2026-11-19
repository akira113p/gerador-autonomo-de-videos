"""Folha de contato: python contato.py saida.png 060 105 116 ... (4 colunas, rótulo com o id)."""
import sys
from pathlib import Path
from PIL import Image, ImageDraw
AQUI = Path(__file__).resolve().parent
ids = sys.argv[2:]
cols, w, h = 4, 480, 270
rows = (len(ids) + cols - 1) // cols
c = Image.new("RGB", (cols * w, rows * h), "white")
d = ImageDraw.Draw(c)
for i, n in enumerate(ids):
    p = AQUI / "imagens" / f"{n}.png"
    if p.exists():
        c.paste(Image.open(p).convert("RGB").resize((w, h)), ((i % cols) * w, (i // cols) * h))
    d.rectangle(((i % cols) * w, (i // cols) * h, (i % cols) * w + 60, (i // cols) * h + 24), fill="black")
    d.text(((i % cols) * w + 6, (i // cols) * h + 6), n, fill="white")
c.save(sys.argv[1])
