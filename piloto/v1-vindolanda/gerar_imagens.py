"""Gera uma imagem por cena do roteiro com Z-Image (ComfyUI). Roda no venv do OpenMontage.

  ../openmontage/.venv/Scripts/python.exe piloto/v1-vindolanda/gerar_imagens.py [ids...]

Sem ids, gera as cenas que ainda não têm imagem. Com ids, regera só essas (seed +100 a cada nova tentativa).
"""

import json
import sys
import time
from pathlib import Path

sys.path.insert(0, "D:/programacao/projetos/videos/openmontage")
from tools.tool_registry import registry  # noqa: E402

AQUI = Path(__file__).resolve().parent
OUT = AQUI / "imagens"

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


def main() -> None:
    roteiro = json.loads((AQUI / "roteiro.json").read_text(encoding="utf-8"))
    pedidos = set(sys.argv[1:])
    OUT.mkdir(parents=True, exist_ok=True)
    log_path = OUT / "prompts.json"
    log = json.loads(log_path.read_text(encoding="utf-8")) if log_path.exists() else {}

    registry.discover()
    tool = registry._tools["zimage_image"]
    for cena in roteiro["cenas"]:
        cid = cena["id"]
        out = OUT / f"{cid}.png"
        if pedidos and cid not in pedidos:
            continue
        if not pedidos and out.exists():
            continue
        seed = log.get(cid, {}).get("seed", 8000 + int(cid) - 100) + 100
        prompt = f"{cena['imagem'].replace('{HERO}', HERO)} {STYLE}"
        t0 = time.time()
        r = tool.execute({"prompt": prompt, "seed": seed, "output_path": str(out)})
        log[cid] = {"seed": seed, "ok": r.success, "error": r.error, "prompt": prompt}
        log_path.write_text(json.dumps(log, indent=1), encoding="utf-8")
        print(cid, r.success, round(time.time() - t0, 1), r.error or "", flush=True)


if __name__ == "__main__":
    main()
