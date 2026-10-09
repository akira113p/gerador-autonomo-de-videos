"""Gera a grade de identidade visual: 3 estilos x 3 cenas, seeds fixas. Roda no venv do OpenMontage."""

import json
import sys
import time
from pathlib import Path

sys.path.insert(0, "D:/programacao/projetos/videos/openmontage")
from tools.tool_registry import registry  # noqa: E402

OUT = Path("C:/ai-local/piloto/identidade")

STYLES = {
    "A_oleo": (
        "Oil painting in the manner of a 17th-century Dutch genre scene. Muted earth palette of ochre, umber, "
        "deep green and bone white, soft chiaroscuro, visible brushstrokes, fine canvas texture, quiet and intimate mood."
    ),
    "B_gravura": (
        "Hand-colored woodcut engraving like an illustration from an old printed chronicle. Bold black ink linework, "
        "cross-hatching, limited palette of faded ochre, brick red and indigo, printed on aged cream paper with "
        "slight ink bleed and paper grain."
    ),
    "C_guache": (
        "Museum archaeological reconstruction illustration in gouache and watercolor. Calm natural daylight, "
        "accurate period detail, muted desaturated colors, soft paper texture, documentary and informative mood."
    ),
}

ACCURACY = (
    "Historically accurate Roman Britain around 100 AD: soldiers in plain wool tunics and cloaks, no armor indoors, "
    "no medieval helmets, no plate armor, no sails, no modern objects. No text, no letters, no watermark."
)

SCENES = {
    "1_carta": "A Roman auxiliary soldier sits on a wooden bench inside a stone barracks room at night, reading a thin "
               "wooden leaf tablet by the light of a small clay oil lamp, a woolen cloak over his shoulders.",
    "2_forte": "Wide view of a Roman timber and stone fort on a cold green hillside in northern Britain at dawn, "
               "thin smoke rising from roofs, low grey clouds, a muddy road leading to the gate.",
    "3_maos": "Close-up of a hand writing with a reed pen and black ink on a very thin pale wooden writing tablet, "
              "a small ink pot beside it on a rough wooden table.",
}

SEEDS = {"1_carta": 1101, "2_forte": 2202, "3_maos": 3303}


def main() -> None:
    registry.discover()
    tool = registry._tools["zimage_image"]
    log = []
    for style, style_block in STYLES.items():
        for scene, scene_text in SCENES.items():
            out = OUT / f"{style}_{scene}.png"
            prompt = f"{scene_text} {style_block} {ACCURACY}"
            t0 = time.time()
            r = tool.execute({"prompt": prompt, "seed": SEEDS[scene], "output_path": str(out)})
            log.append({"file": out.name, "ok": r.success, "error": r.error,
                        "seconds": round(time.time() - t0, 1), "prompt": prompt})
            print(out.name, r.success, round(time.time() - t0, 1), r.error or "")
    (OUT / "prompts.json").write_text(json.dumps(log, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
