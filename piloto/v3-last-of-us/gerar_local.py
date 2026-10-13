"""Plano B: gera localmente (Z-Image, ComfyUI ligado) as cenas que ainda faltam em imagens/. Roda no venv do OpenMontage.

  ../openmontage/.venv/Scripts/python.exe piloto/v3-last-of-us/gerar_local.py [números...]

Grava em imagens_local/NNN.png (não sobrescreve imagens/). Sem números, faz todas as que faltam em imagens/.
Cartões com texto (CARD) saem piores no Z-Image; ficam por último.
"""

import json
import sys
import time
from pathlib import Path

sys.path.insert(0, "D:/programacao/projetos/videos/openmontage")
sys.path.insert(0, "D:/programacao/projetos/videos/v1 geracao de videos/piloto/v2-dia-em-roma")
from prompts import BASE, BONECO  # noqa: E402  (estilo do canal, igual ao vídeo 2)

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import importlib.util  # noqa: E402

spec = importlib.util.spec_from_file_location("p3", AQUI / "prompts.py")
p3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p3)
from tools.tool_registry import registry  # noqa: E402

OUT = AQUI / "imagens_local"


def main() -> None:
    OUT.mkdir(exist_ok=True)
    pedidos = [int(a) for a in sys.argv[1:]]
    if not pedidos:
        pedidos = [n for n in range(1, 206) if not (AQUI / "imagens" / f"{n:03d}.png").exists()]
        pedidos.sort(key=lambda n: p3.cartao(n))  # cartões por último
    registry.discover()
    tool = registry._tools["zimage_image"]
    log_path = OUT / "log.json"
    log = json.loads(log_path.read_text(encoding="utf-8")) if log_path.exists() else {}
    for n in pedidos:
        out = OUT / f"{n:03d}.png"
        if out.exists():
            continue
        if (AQUI / "imagens" / f"{n:03d}.png").exists():  # já veio do ChatGPT/Gemini
            continue
        texto = p3.prompt(n)
        prompt = f"{texto} {BASE}" if p3.cartao(n) else f"{texto} {BONECO} {BASE}"
        t0 = time.time()
        r = tool.execute({"prompt": prompt, "seed": 9000 + n, "output_path": str(out)})
        log[f"{n:03d}"] = {"ok": r.success, "error": r.error}
        log_path.write_text(json.dumps(log, indent=1), encoding="utf-8")
        print(f"{n:03d}", r.success, round(time.time() - t0), r.error or "", flush=True)


if __name__ == "__main__":
    main()
