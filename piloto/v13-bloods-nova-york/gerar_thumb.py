"""Miniatura 1280x720: base (thumb/base_gpt.png) + texto amarelo com contorno preto por código, no terço esquerdo.

  python piloto/v13-bloods-nova-york/gerar_thumb.py

O texto é sempre por código (a IA erra letras).
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

AQUI = Path(__file__).resolve().parent
BASE = AQUI / "thumb" / "base_gpt.png"
DESTINO = AQUI / "thumb" / "thumb_1.jpg"
LINHAS = ["ONE YEAR", "IN"]  # não repete o título palavra por palavra
FONTE = "C:/Windows/Fonts/impact.ttf"
LARG_MAX = 600  # o terço esquerdo da base está livre para o texto


def main() -> None:
    img = Image.open(BASE).convert("RGB")
    w, h = img.size
    alvo_h = round(w * 9 / 16)
    if abs(h - alvo_h) > 2:
        top = max((h - alvo_h) // 2, 0)
        img = img.crop((0, top, w, top + alvo_h))
    img = img.resize((1280, 720), Image.LANCZOS)
    d = ImageDraw.Draw(img)
    tam = 170
    fonte = ImageFont.truetype(FONTE, tam)
    while max(d.textlength(l, font=fonte) for l in LINHAS) > LARG_MAX:
        tam -= 6
        fonte = ImageFont.truetype(FONTE, tam)
    y = (720 - len(LINHAS) * tam * 1.05) / 2
    for linha in LINHAS:
        x = 50
        d.text((x + 8, y + 10), linha, font=fonte, fill=(0, 0, 0), stroke_width=12, stroke_fill=(0, 0, 0))
        d.text((x, y), linha, font=fonte, fill=(255, 230, 0), stroke_width=12, stroke_fill=(0, 0, 0))
        y += tam * 1.05
    img.save(DESTINO, quality=95)
    print("ok", DESTINO)


if __name__ == "__main__":
    main()
