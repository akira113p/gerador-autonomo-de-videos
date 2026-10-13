"""Monta folhas de contato (3x2) das imagens para revisar: python folha.py 2 7 -> folhas/folha_002.png"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw
A = Path(__file__).resolve().parent
ini, fim = int(sys.argv[1]), int(sys.argv[2])
(A / "folhas").mkdir(exist_ok=True)
W, H = 480, 270
ids = [n for n in range(ini, fim + 1) if (A / "imagens" / f"{n:03d}.png").exists()]
for k in range(0, len(ids), 12):
    grupo = ids[k:k + 12]
    f = Image.new("RGB", (W * 4, H * 3), "white")
    for i, n in enumerate(grupo):
        im = Image.open(A / "imagens" / f"{n:03d}.png").convert("RGB").resize((W, H))
        ImageDraw.Draw(im).text((8, 6), f"{n:03d}", fill="red")
        f.paste(im, ((i % 4) * W, (i // 4) * H))
    f.save(A / "folhas" / f"folha_{grupo[0]:03d}.png")
    print(A / "folhas" / f"folha_{grupo[0]:03d}.png")
