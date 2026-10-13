"""Thumbnail 1280x720: base (thumb/base_N.png) + texto amarelo com contorno preto por código.

  ../openmontage/.venv/Scripts/python.exe piloto/v3-last-of-us/gerar_thumb.py [só-texto]

Sem bases em thumb/, gera 3 localmente (Z-Image, ComfyUI ligado). Com bases (do ChatGPT ou locais), só põe o texto.
O texto é sempre por código (a IA erra letras).
"""

import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

AQUI = Path(__file__).resolve().parent
OUT = AQUI / "thumb"
TITULO = "WOULD YOU SURVIVE?"
FONTE = "C:/Windows/Fonts/impact.ttf"

CENA = (
    "YouTube thumbnail. Big close-up of a stick figure man in a blue t-shirt with short messy brown hair in the lower left "
    "of the frame, his head very large and starting at the middle of the frame, with a hugely exaggerated scared face: wide "
    "round eyes, raised eyebrows, mouth wide open, two sweat drops. Behind him on the right, a stick figure whose whole head "
    "is covered by a bumpy orange-tan fungus bloom like a big flower with a dark slit and no eyes, arms stretched forward, "
    "in a ruined city street with broken buildings and a vivid saturated turquoise and orange sky, very bright saturated "
    "colors. The top part of the frame is plain sky with empty space."
)


def texto(base: Path, destino: Path) -> None:
    img = Image.open(base).convert("RGB")
    w, h = img.size
    alvo_h = round(w * 9 / 16)
    if h > alvo_h + 2:
        top = (h - alvo_h) // 2
        img = img.crop((0, top, w, top + alvo_h))
    img = img.resize((1280, 720), Image.LANCZOS)
    d = ImageDraw.Draw(img)
    tam = 150
    fonte = ImageFont.truetype(FONTE, tam)
    while d.textlength(TITULO, font=fonte) > 1180:
        tam -= 6
        fonte = ImageFont.truetype(FONTE, tam)
    larg = d.textlength(TITULO, font=fonte)
    x, y = (1280 - larg) / 2, 18
    d.text((x + 8, y + 10), TITULO, font=fonte, fill=(0, 0, 0), stroke_width=12, stroke_fill=(0, 0, 0))
    d.text((x, y), TITULO, font=fonte, fill=(255, 230, 0), stroke_width=12, stroke_fill=(0, 0, 0))
    img.save(destino, quality=95)


def gerar_bases() -> None:
    sys.path.insert(0, "D:/programacao/projetos/videos/openmontage")
    sys.path.insert(0, str(AQUI.parent / "v2-dia-em-roma"))
    from prompts import BASE, BONECO  # estilo do canal
    from tools.tool_registry import registry

    registry.discover()
    tool = registry._tools["zimage_image"]
    for i, seed in enumerate([501, 777, 1234], 1):
        r = tool.execute({"prompt": f"{CENA} {BONECO} {BASE}", "seed": seed, "output_path": str(OUT / f"base_{i}.png")})
        print("base", i, r.success, r.error or "", flush=True)


def main() -> None:
    OUT.mkdir(exist_ok=True)
    if "só-texto" not in sys.argv and not list(OUT.glob("base_*.png")):
        gerar_bases()
    for base in sorted(OUT.glob("base_*.png")):
        destino = OUT / base.name.replace("base_", "thumb_").replace(".png", ".jpg")
        texto(base, destino)
        print("ok", destino)


if __name__ == "__main__":
    main()
