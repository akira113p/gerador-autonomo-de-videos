"""Monta a descrição do YouTube (inglês) com capítulos, fontes, créditos e hashtags. Rode depois do montar.py.

  python piloto/v11-oregon-trail/gerar_descricao.py                 # versão ACE-Step: tempos.json -> descricao.md
  SUFIXO=_jazz python piloto/v11-oregon-trail/gerar_descricao.py    # versão jazz: tempos_jazz.json -> descricao_jazz.md

Regras do YouTube: só as ~150 primeiras letras aparecem na busca (por isso o gancho com as palavras-chave vem
primeiro); capítulos começam em 0:00, são 3 ou mais e duram 10 s ou mais; limite de 5000 caracteres.
"""

import json
import os
from pathlib import Path

AQUI = Path(__file__).resolve().parent

CAPITULOS = {
    "0": "Intro: you will not be riding",
    "1": "Why would anyone do this?",
    "2": "Shopping day: the wagon and the oxen",
    "3": "What goes in the wagon",
    "4": "The guidebook problem",
    "5": "A day on the trail",
    "6": "River crossings",
    "7": "Cholera: the real killer",
    "8": "The myth of the attack",
    "9": "The people who were already there",
    "10": "Mountains and the end of the road",
    "11": "Arrival: the journey's end",
}

TOPO = """What would your life be like on the Oregon Trail? We start in Independence, Missouri, in the spring of 1850, with a wagon, a team of oxen, and about 2,000 miles of walking ahead.

What it cost to outfit a wagon, why nobody rode in it, what a day on the trail looked like, how rivers and cholera (not arrows) were the real dangers, what the numbers say about attacks, and what the trail meant for the Native nations whose homelands it crossed."""

FONTES = """SOURCES
- National Park Service, Oregon National Historic Trail: history, FAQ, "Traveling the Emigrant Trails", "Cholera: a Trail Epidemic", "The Barlow Road", "Horse Creek Treaty"
- Bureau of Land Management, National Historic Oregon Trail Interpretive Center: "Basic Facts About the Oregon Trail"
- Oregon-California Trails Association (OCTA): emigrant profiles and trail facts
- Randolph B. Marcy, The Prairie Traveler (1859)
- Lansford Hastings, The Emigrants' Guide to Oregon and California (1845)
- John D. Unruh Jr., The Plains Across: The Overland Emigrants and the Trans-Mississippi West, 1840-60 (1979)
- Lillian Schlissel, Women's Diaries of the Westward Journey (1982)
- Diary of Mrs. Amelia Stewart Knight (1853), Transactions of the Oregon Pioneer Association (1933)
- American Heritage, "The Prairie Schooner Got Them There"
- Museum at the Gateway Arch: "Conflict on the Trail"
- Oregon Encyclopedia: Donation Land Act, Willamette Valley treaties
- Wyoming State Parks: Independence Rock

Numbers about deaths and travelers are estimates, and sources disagree; we give ballparks and say so.
Illustrations: AI-generated in a custom style and checked for anachronisms. Narration: synthetic voice."""

MUSICA = {
    "": "Music: AI-generated (ACE-Step 1.5).",
    "_jazz": 'Music: "No Copyright - Royalty Free 12 hours JAZZ Music" by 741Hz, '
             "https://www.youtube.com/watch?v=HqPsROn8e8k",
    "_medieval": 'Music: "No Copyright Medieval Fantasy Ambient Music Mix | The Old Kingdom [No AI]" by AlkaKrab, '
                 "https://www.youtube.com/watch?v=2FEUVx8F4dk",
}

# as 3 primeiras aparecem acima do título; mais de 15 anulam todas
HASHTAGS = "#OregonTrail #History #PioneerLife"


def mmss(s: float) -> str:
    s = int(s)
    return f"{s // 60}:{s % 60:02d}"


def main() -> None:
    sufixo = os.environ.get("SUFIXO", "")
    tempos = json.loads((AQUI / f"tempos{sufixo}.json").read_text(encoding="utf-8"))
    cenas = json.loads((AQUI / "roteiro.json").read_text(encoding="utf-8"))["cenas"]
    linhas = []
    for c in cenas:
        if c["inicio_capitulo"]:
            t = 0 if c["id"] == "001" else tempos["cenas"][c["id"]]
            linhas.append(f"{mmss(t)} {CAPITULOS[c['capitulo']]}")
    texto = f"{TOPO}\n\nCHAPTERS\n" + "\n".join(linhas) + f"\n\n{FONTES}\n{MUSICA[sufixo]}\n\n{HASHTAGS}\n"
    assert len(texto) <= 5000, f"descrição com {len(texto)} caracteres (limite do YouTube: 5000)"
    (AQUI / f"descricao{sufixo}.md").write_text(texto, encoding="utf-8")
    print(texto)


if __name__ == "__main__":
    main()
