"""5 quadros no estilo stickman explainer (referência: Ink Explainer). Roda no venv do OpenMontage."""

import json
import sys
import time
from pathlib import Path

sys.path.insert(0, "D:/programacao/projetos/videos/openmontage")
from tools.tool_registry import registry  # noqa: E402

OUT = Path("C:/ai-local/piloto/identidade/stickman")
OUT.mkdir(parents=True, exist_ok=True)

STYLE = (
    "Simple hand-drawn stickman cartoon illustration for an educational history video. "
    "Characters are stick figures with a large perfectly round white head, thick slightly wobbly black marker outline, "
    "small dot eyes, simple line mouth, expressive eyebrows, thin black line body. "
    "Flat muted colors with a light colored-pencil texture, clean composition, lots of empty space, 16:9 frame."
)

HERO = (
    "The main character is a Roman auxiliary soldier stick figure with short messy dark brown hair, "
    "wearing a simple knee-length red wool tunic with a brown leather belt and a brown wool cloak, bare legs and sandals."
)

FRAMES = {
    "1_pacote": (
        f"{HERO} He sits on a wooden bench inside a plain stone room and opens a small cloth parcel, "
        "pulling out a pair of grey wool socks, with a big delighted smile. A small clay oil lamp glows on a shelf. "
        "Warm cream walls, brown wooden floor."
    ),
    "2_tabua": (
        "Explainer card on a plain white background. In the center, a thin pale wooden writing tablet, "
        "with neat handwritten black ink words on it: \"SOCKS, SANDALS, UNDERPANTS\". "
        "Above it, large hand-lettered black capital text: \"A LETTER FROM HOME\". "
        "Small handwritten caption below: \"VINDOLANDA, ABOUT 100 AD\"."
    ),
    "3_mapa": (
        "Explainer card on a plain white background. A simple flat-colored map of the island of Great Britain in soft green, "
        "surrounded by pale blue sea. A red map pin in the far north of England with the handwritten black label "
        "\"VINDOLANDA\". Large hand-lettered title at the top: \"THE EDGE OF THE EMPIRE\"."
    ),
    "4_voce_ele": (
        "Split screen divided by a vertical black dashed line. Left side labeled \"YOU\" in hand-lettered black capitals: "
        "a plain stick figure with a round white head sits at a modern desk looking at a smartphone, bored face. "
        f"Right side labeled \"HIM\": {HERO} He sits on a wooden stool writing with a reed pen on a thin wooden tablet, "
        "focused face. White background."
    ),
    "5_forte": (
        "Wide scene of a Roman timber fort with a wooden palisade and a gate tower on a cold green hillside under a grey "
        "cloudy sky. In front, three Roman auxiliary soldier stick figures in red tunics and brown cloaks carry bundles of "
        "firewood along a muddy path, tired faces. Soft flat colors: grey-blue sky, muted green grass, brown mud."
    ),
}


def main() -> None:
    registry.discover()
    tool = registry._tools["zimage_image"]
    log = []
    for i, (name, scene) in enumerate(FRAMES.items()):
        out = OUT / f"{name}.png"
        prompt = f"{scene} {STYLE}"
        t0 = time.time()
        r = tool.execute({"prompt": prompt, "seed": 7000 + i, "output_path": str(out)})
        log.append({"file": out.name, "ok": r.success, "error": r.error,
                    "seconds": round(time.time() - t0, 1), "seed": 7000 + i, "prompt": prompt})
        print(out.name, r.success, round(time.time() - t0, 1), r.error or "", flush=True)
    (OUT / "prompts.json").write_text(json.dumps(log, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
