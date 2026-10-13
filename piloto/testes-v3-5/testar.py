"""Teste rápido de estilo: gera imagens soltas com BASE/BONECO do vídeo 2. Uso: python testar.py nome 'prompt' [seed]"""
import sys, json
from pathlib import Path
sys.path.insert(0, "D:/programacao/projetos/videos/openmontage")
sys.path.insert(0, "D:/programacao/projetos/videos/v1 geracao de videos/piloto/v2-dia-em-roma")
from prompts import BASE, BONECO
from tools.tool_registry import registry
registry.discover()
tool = registry._tools["zimage_image"]
AQUI = Path(__file__).resolve().parent
pedidos = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
for nome, (prompt, sem) in pedidos.items():
    texto = f"{prompt} {BASE}" if sem else f"{prompt} {BONECO} {BASE}"
    r = tool.execute({"prompt": texto, "seed": 4242, "output_path": str(AQUI / f"{nome}.png")})
    print(nome, r.success, r.error or "", flush=True)
