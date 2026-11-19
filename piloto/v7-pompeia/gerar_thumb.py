"""Thumbnail 1280x720: imagem Z-Image (personagem em close à esquerda, cena saturada) + texto amarelo com contorno preto.
Roda no venv do OpenMontage, com o ComfyUI ligado.

  ../openmontage/.venv/Scripts/python.exe piloto/v7-pompeia/gerar_thumb.py [só-texto]

Gera 3 variações (seeds diferentes) em thumb/. Com "só-texto", refaz só o texto sobre as bases já geradas.
"""

import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, "D:/programacao/projetos/videos/openmontage")
sys.path.insert(0, str(Path(__file__).resolve().parent))
from prompts import BASE, BONECO, T  # noqa: E402

AQUI = Path(__file__).resolve().parent
OUT = AQUI / "thumb"
TITULO = "LAST DAY OF POMPEII"
FONTE = "C:/Windows/Fonts/impact.ttf"

CENA = (
    "YouTube thumbnail. Big close-up of " + T["C"] + " in the lower left of the frame, his head very large "
    "and starting at the middle of the frame, with a hugely exaggerated shocked face: wide round eyes, raised eyebrows, "
    "mouth wide open, two sweat drops. He holds a round loaf of bread in one hand and points with the other at a big "
    "grey volcano cloud shaped like a pine tree rising on the right side behind a small Roman town of white walls and "
    "red-tiled roofs, a vivid saturated orange and turquoise sky, very bright saturated colors. "
    "The top part of the frame is plain sky with empty space."
)


def texto(base: Path, destino: Path) -> None:
    img = Image.open(base).convert("RGB").resize((1280, 720), Image.LANCZOS)
    d = ImageDraw.Draw(img)
    tam = 150
    fonte = ImageFont.truetype(FONTE, tam)
    while d.textlength(TITULO, font=fonte) > 1180:
        tam -= 6
        fonte = ImageFont.truetype(FONTE, tam)
    larg = d.textlength(TITULO, font=fonte)
    x, y = (1280 - larg) / 2, 18
    # sombra dura + contorno grosso, como nas thumbs de referência
    d.text((x + 8, y + 10), TITULO, font=fonte, fill=(0, 0, 0), stroke_width=12, stroke_fill=(0, 0, 0))
    d.text((x, y), TITULO, font=fonte, fill=(255, 230, 0), stroke_width=12, stroke_fill=(0, 0, 0))
    img.save(destino, quality=95)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    if "só-texto" not in sys.argv:
        from tools.tool_registry import registry

        registry.discover()
        tool = registry._tools["zimage_image"]
        for i, seed in enumerate([501, 777, 1234], 1):
            r = tool.execute({"prompt": f"{CENA} {BONECO} {BASE}", "seed": seed,
                              "output_path": str(OUT / f"base_{i}.png")})
            print("base", i, r.success, r.error or "", flush=True)
    for base in sorted(OUT.glob("base_*.png")):
        destino = OUT / base.name.replace("base_", "thumb_").replace(".png", ".jpg")
        texto(base, destino)
        print("ok", destino)


if __name__ == "__main__":
    main()
