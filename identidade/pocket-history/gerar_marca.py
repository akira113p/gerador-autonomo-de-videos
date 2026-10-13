"""Bases de imagem do canal Pocket History: foto de perfil (1024x1024) e monumentos do banner (1344x768).
Roda no venv do OpenMontage, com o ComfyUI ligado. Só gera o que ainda não existe em bases/.

  ../openmontage/.venv/Scripts/python.exe identidade/pocket-history/gerar_marca.py

A composição final (recorte, texto, tamanhos do YouTube, prévias) é do compor_marca.py.
"""

import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, "D:/programacao/projetos/videos/openmontage")
sys.path.insert(0, str(RAIZ / "piloto" / "v2-dia-em-roma"))
from prompts import BASE, BONECO, PERSONAGENS  # noqa: E402

AQUI = Path(__file__).resolve().parent
BASES = AQUI / "bases"

PERFIL = (
    "Square icon illustration, centered with a margin around it: a large mustard-yellow cloth shirt pocket with a brown "
    "stitched edge fills the lower half of the frame, and out of the pocket peeks the big round head of "
    + PERSONAGENS["R"].replace("wearing a short knee-length mustard-yellow wool tunic with a brown belt and brown sandals",
                               "with a green laurel wreath")
    + ", only his head and one small black mitten hand waving above the pocket edge, curious happy smile. "
    "A small rolled papyrus scroll sticks out of the pocket next to him. Plain flat bright turquoise background."
)
MARCOS = (
    "Four small simple landmarks standing side by side in a row on a plain flat pale turquoise background with plenty "
    "of empty space around them: a white Roman temple with columns, an Egyptian sandstone pyramid, a medieval stone "
    "castle tower, a wooden Viking longship with one square sail. All four are about the same height."
)


def main() -> None:
    BASES.mkdir(exist_ok=True)
    from tools.tool_registry import registry

    registry.discover()
    tool = registry._tools["zimage_image"]
    for nome, texto, seeds, w, h in [("perfil", PERFIL, [11, 222, 3333], 1024, 1024), ("marcos", MARCOS, [5, 66], 1344, 768)]:
        for i, seed in enumerate(seeds, 1):
            out = BASES / f"{nome}_{i}.png"
            if out.exists():
                continue
            # monumentos sem o bloco do personagem (senão ganham rosto e braços)
            prompt = f"{texto} {BASE}" if nome == "marcos" else f"{texto} {BONECO} {BASE}"
            r = tool.execute({"prompt": prompt, "seed": seed, "width": w, "height": h,
                              "output_path": str(out)})
            print(nome, i, r.success, r.error or "", flush=True)


if __name__ == "__main__":
    main()
