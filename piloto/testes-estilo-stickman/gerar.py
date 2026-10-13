"""Teste de estilo stickman explainer (Ink Explainer / Diário Nada Normal): 20 quadros variados com Z-Image.
Roda no venv do OpenMontage, com o ComfyUI ligado.

  ../openmontage/.venv/Scripts/python.exe piloto/testes-estilo-stickman/gerar.py [ids...]

Sem ids, gera os quadros que ainda não têm imagem. Com ids, regera só esses (seed +100).
"""

import json
import sys
import time
from pathlib import Path

sys.path.insert(0, "D:/programacao/projetos/videos/openmontage")
from tools.tool_registry import registry  # noqa: E402

AQUI = Path(__file__).resolve().parent
OUT = AQUI / "imagens"

BASE = (
    "Hand-drawn cartoon illustration for an educational explainer video. "
    "Thick slightly wobbly black marker outlines of even weight on every shape. "
    "Flat colors with a subtle digital brush texture, large simple color areas, minimal detail, "
    "the background drawn in the same simple bold outlines and flat fills, everything in sharp focus, "
    "clean wide 16:9 composition with breathing room."
)

BONECO = (
    "All characters are stick figures with a big perfectly round white head with soft light grey shading on one side, "
    "no nose, small black dot eyes, expressive eyebrows, simple small mouth, "
    "thin single black line arms and legs, small rounded black mitten hands, "
    "clothes drawn as simple flat colored shapes over the stick body."
)

# quadros só de cenário, cartão ou mapa: sem o bloco de personagem (senão o modelo põe um stickman)
SEM_BONECO = {"01", "02", "12", "13", "14", "15", "16"}

GREGO = "wearing a simple knee-length off-white wool chiton tunic with a brown belt, sandals, short messy dark brown hair"
GREGA = "wearing a long ankle-length terracotta red peplos dress, dark hair tied in a bun"
MODERNO = "wearing a blue t-shirt and grey trousers, short messy brown hair"

QUADROS = [
    # Grécia antiga: paisagens
    ("01-paisagem-acropole",
     "Very simple wide landscape with only a few big shapes: one large rocky ochre hill in the center with a single new, "
     "complete white marble temple with columns and a painted triangular roof on top, three small houses with terracotta "
     "roofs at the foot of the hill, two olive trees in the foreground, a big pale yellow rising sun, pale turquoise sky."),
    ("02-paisagem-costa-egeu",
     "Very simple wide landscape with only a few big shapes: a turquoise sea filling the lower half, one small wooden "
     "fishing boat with one square sail, a rocky golden coast on the left with two olive trees, "
     "pale blue sky with two simple clouds."),
    ("03-paisagem-colheita-oliva",
     "Olive harvest in an ancient Greek grove: two stick figure men " + GREGO + " beating the branches of a big olive tree "
     "with long sticks, a stick figure woman " + GREGA + " collecting black olives into a woven basket, "
     "dry golden grass, pale sky."),
    # Grécia antiga: personagens
    ("04-personagens-agora",
     "Market scene in the ancient Athenian agora with two stick figures facing each other across a wooden table: "
     "on the left a smiling merchant " + GREGO + " stands behind the table with clay amphorae, a bowl of olives and round "
     "loaves of bread; on the right a curious customer wearing a long green himation cloak points at the olives. "
     "A simple row of white columns of a stoa behind them, sunny sand colored ground."),
    ("05-personagens-filosofo",
     "Three stick figures in a sunny cream-colored colonnade with a pale blue sky between the columns. "
     "On the left, two young students " + GREGO + " sit side by side on a low stone step and listen; "
     "one of them scratches his head with a small question mark floating above. "
     "On the right, an old man with a short grey beard wearing a blue himation cloak draped over one shoulder "
     "stands and raises one finger while talking."),
    ("06-close-tear",
     "Medium close-up of a focused stick figure woman " + GREGA + " standing in front of a tall vertical wooden frame "
     "leaning against a plastered wall: two upright wooden posts with a crossbar at the top, many straight vertical threads "
     "hang from the crossbar down to a row of small round clay weights dangling near the floor, "
     "a half-woven striped cloth at the top of the threads, she passes a thread between them with one hand."),
    ("07-personagens-arado",
     "Side view of a plowing scene in a dry brown field: on the left two brown oxen walk to the left, joined by a wooden yoke, "
     "pulling a simple pointed wooden stick plough; on the right a stick figure farmer " + GREGO + " walks behind holding "
     "the plough handle with both hands, small drops of sweat fly from his head, rocky hills and one olive tree behind, "
     "clean flat pale yellow sky."),
    ("08-noite-simposio",
     "Night interior of an ancient Greek dining room with dark navy blue walls: three relaxed stick figure men wearing draped "
     "himation cloaks lie on their sides on three long wooden couches with cushions, propped on one elbow with legs stretched "
     "out, each holding a wide shallow two-handled drinking cup with red wine, one of them laughs. "
     "One small clay oil lamp on a tall stand in the corner gives a warm orange light."),
    ("09-interior-cozinha",
     "Medium shot in the courtyard of an ancient Greek house, the characters large in the frame: a stick figure woman "
     + GREGA + " kneels and grinds grain by rubbing a stone on a flat stone slab, a dome-shaped clay oven with a small fire "
     "on the right, two tall clay storage jars against a warm cream plastered wall that fills the background, "
     "a curious small stick figure boy " + GREGO + " watches her."),
    ("10-paineis-dia-menino",
     "Comic strip with exactly three equal side-by-side panels separated by thick black frame lines, each panel showing "
     "the same small stick figure boy with a perfectly round white head " + GREGO + ": first panel he wakes up yawning on "
     "a simple wooden bed, "
     "second panel he eats a piece of bread with a bowl of figs, third panel he walks beside an old slave tutor "
     "carrying a wax writing tablet."),
    # Cartões e diagramas
    ("11-tela-dividida-now-then",
     "Split screen divided by a vertical black dashed line on a plain white background. Hand-lettered black capital words "
     "at the top: \"NOW\" on the left and \"THEN\" on the right. Left side: a tired stick figure " + MODERNO + " "
     "slumped at a desk in front of a laptop with a coffee mug. Right side: a relaxed smiling stick figure " + GREGO + " "
     "sitting under an olive tree eating grapes."),
    ("12-cartao-anfora",
     "Explainer card on a plain pure white background: one large Greek clay amphora in the center, "
     "a big green hand-drawn check mark next to it, and the hand-lettered black capital words \"OLIVE OIL\" underneath."),
    ("13-cartao-x-geladeira",
     "Explainer card on a plain pure white background: on the left a modern white refrigerator crossed out by a big thick "
     "red hand-drawn X, a hand-drawn black arrow pointing right, on the right a tall clay storage jar with a green check mark."),
    ("14-cartao-linha-tempo",
     "Explainer card on a plain pure white background: a long horizontal hand-drawn black timeline arrow across the middle, "
     "a red map pin on the left end labeled \"500 BC\" and a red map pin on the right end labeled \"TODAY\" "
     "in hand-lettered black capital letters, a small Greek temple doodle above the left pin and a small smartphone doodle "
     "above the right pin."),
    # Mapas
    ("15-mapa-grecia",
     "Very simple hand-drawn cartoon map with only a few big flat shapes, like a children's book, on a plain white background: "
     "the Greek peninsula as one big flat orange shape with a thick black wobbly outline on the left, "
     "a light blue sea in the middle with five small flat yellow island shapes, the coast of Turkey as one flat green shape "
     "on the right. One red map pin on the orange peninsula near the sea, with the hand-lettered black capital label "
     "\"ATHENS\" next to it."),
    ("16-mapa-mundo",
     "Simple hand-drawn world map on a plain white background: continents filled with flat colors (green, orange, yellow, "
     "tan, light purple) with thick black wobbly outlines, a red map pin on Greece, a dashed black line curving from Greece "
     "toward the right edge."),
    # Mundo atual
    ("17-atual-escritorio",
     "Modern office: a stick figure office worker " + MODERNO + " sits at a desk with a laptop and a tall stack of papers, "
     "big tired eyes and a frown, a round wall clock behind showing five o'clock, grey and beige office colors."),
    ("18-atual-sofa-noite",
     "Modern living room at night: a stick figure " + MODERNO + " lies on a grey sofa scrolling on a glowing smartphone, "
     "the blue light of the screen on his face, a dark window with a city view and a small lamp, navy blue shadows."),
    ("19-atual-cidade",
     "Very simple wide landscape of a modern city at sunset with only a few big shapes: a row of five tall flat-colored "
     "buildings with square windows, one street in front with two small cars and a traffic light, "
     "two small stick figure pedestrians, orange and pink sky."),
    ("20-atual-turista-partenon",
     "One cheerful stick figure tourist " + MODERNO + " with a small backpack stands on the left and takes a photo with "
     "a smartphone of a ruined ancient temple on the right, the temple drawn as a simple cartoon: a row of flat cream "
     "columns with bold black outlines, a broken triangular roof, a few fallen stone blocks, two tiny stick figure tourists "
     "far behind, flat bright blue sky."),
]


def main() -> None:
    pedidos = set(sys.argv[1:])
    OUT.mkdir(parents=True, exist_ok=True)
    log_path = OUT / "prompts.json"
    log = json.loads(log_path.read_text(encoding="utf-8")) if log_path.exists() else {}

    registry.discover()
    tool = registry._tools["zimage_image"]
    for i, (qid, cena) in enumerate(QUADROS):
        out = OUT / f"{qid}.png"
        if pedidos and qid not in pedidos and qid[:2] not in pedidos:
            continue
        if not pedidos and out.exists():
            continue
        seed = log.get(qid, {}).get("seed", 7000 + i - 100) + 100
        prompt = f"{cena} {BASE}" if qid[:2] in SEM_BONECO else f"{cena} {BONECO} {BASE}"
        t0 = time.time()
        r = tool.execute({"prompt": prompt, "seed": seed, "output_path": str(out)})
        log[qid] = {"seed": seed, "ok": r.success, "error": r.error, "prompt": prompt}
        log_path.write_text(json.dumps(log, indent=1, ensure_ascii=False), encoding="utf-8")
        print(qid, r.success, round(time.time() - t0, 1), r.error or "", flush=True)


if __name__ == "__main__":
    main()
