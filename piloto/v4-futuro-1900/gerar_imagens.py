"""Gera uma imagem por cena (prompts.py) com Z-Image (ComfyUI). Roda no venv do OpenMontage, com o ComfyUI ligado.

  ../openmontage/.venv/Scripts/python.exe piloto/v4-futuro-1900/gerar_imagens.py [números...]

Sem números, gera as cenas que ainda não têm imagem. Com números, regera só essas (seed +100 a cada tentativa).
Feche Chrome e Opera antes: com pouca RAM livre o ComfyUI relê o modelo do disco e cada imagem leva minutos.
"""

import json
import sys
import time
from pathlib import Path

sys.path.insert(0, "D:/programacao/projetos/videos/openmontage")
sys.path.insert(0, str(Path(__file__).resolve().parent))
from prompts import P, prompt  # noqa: E402
from tools.tool_registry import registry  # noqa: E402

AQUI = Path(__file__).resolve().parent
OUT = AQUI / "imagens"


def main() -> None:
    pedidos = {int(a) for a in sys.argv[1:]}
    OUT.mkdir(parents=True, exist_ok=True)
    log_path = OUT / "prompts.json"
    log = json.loads(log_path.read_text(encoding="utf-8")) if log_path.exists() else {}

    registry.discover()
    tool = registry._tools["zimage_image"]
    for n in sorted(P):
        cid = f"{n:03d}"
        out = OUT / f"{cid}.png"
        if pedidos and n not in pedidos:
            continue
        if not pedidos and out.exists():
            continue
        seed = log.get(cid, {}).get("seed", 9000 + n - 100) + 100
        t0 = time.time()
        r = tool.execute({"prompt": prompt(n), "seed": seed, "output_path": str(out)})
        log[cid] = {"seed": seed, "ok": r.success, "error": r.error, "prompt": prompt(n)}
        log_path.write_text(json.dumps(log, indent=1, ensure_ascii=False), encoding="utf-8")
        print(cid, r.success, round(time.time() - t0, 1), r.error or "", flush=True)


if __name__ == "__main__":
    main()
