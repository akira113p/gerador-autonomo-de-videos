"""Prompts de imagem do vídeo 10 (operário da Grande Pirâmide, Egito) para o Z-Image local, um por linha numerada do roteiro.md.

prompt() põe o estilo (BASE) e, se a cena tem stick figure, a descrição do boneco (BONECO).
{CARD} = cartão de fundo branco (palavras curtas, conferir a grafia).
Sem hieróglifos (o modelo erra): paredes e cartuchos só com formas simples. Nenhum corpo, nenhuma violência.
Época: Egito do Reino Antigo (c. 2560 a.C.): linho branco, cobre, trenós, barcos a remo e vela quadrada, sem roda, sem ferro, sem moeda.
Cenas modernas (arqueólogos, físico, turista) são só para as linhas que falam de hoje.
"""

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

CARTAO = "Explainer card on a plain pure white background: "

T = {
    "C": "the stick figure farmer Ipi with short straight black hair with a fringe, a short white linen wrap kilt, a plain tan cloth headband and bare feet",
    "FAM": "his stick figure wife in a long plain white dress and two small stick figure children",
    "M": "the stick figure inspector Merer, a man with a short black wig, a long white pleated linen kilt and a wide gold-and-blue beaded collar, holding a papyrus scroll and a thin reed pen",
    "K": "a stick figure pharaoh in a striped blue-and-gold headcloth, a wide gold collar and a short white kilt",
    "OFF": "a stick figure royal official with a short black wig, a white pleated kilt and a gold collar",
    "SC": "a stick figure scribe sitting cross-legged in a white kilt with a half-unrolled papyrus sheet across his knees and a thin reed pen",
    "DOC": "a stick figure healer in a white kilt with a small clay pot of ointment and a roll of linen bandage",
    "ARCH": "a modern stick figure archaeologist in a khaki shirt and a wide-brim hat",
    "HERO": "a stick figure Greek traveler in a white tunic, sandals and a flat wide-brim travel hat, holding a small wax tablet",
    "WK": "stick figure workers in short white linen kilts and tan headbands",
    "BOAT": "a long wooden Nile boat with high curved ends, one square white sail, a row of oars and a pile of big pale limestone blocks on the deck",
    "SLED": "a wooden sled with two curved runners carrying one big square pale stone block, thick ropes tied to its front",
    "PYR": "the Great Pyramid, a huge four-sided pyramid with smooth bright white-yellow stone sides and a sharp pointed top, golden desert sand around it",
    "CARD": CARTAO,
    "S": "Split screen divided by a vertical black dashed line. ",
}

P = {
    # 0. Abertura
    1: "A wide desert landscape beside the blue Red Sea at sunrise, tiny modern stick figure archaeologists with brushes digging in the sand in front of a dark cave opening cut into a pale limestone hill.",
    2: "{CARD}a rolled papyrus scroll with a gold medal ribbon on it and the hand-lettered words \"OLDEST PAPYRUS EVER\" in capitals.",
    3: "{ARCH} reads an unrolled papyrus with a surprised face, two small thought-bubble icons beside him, a praying hands icon and a lightning bolt curse icon, both crossed out with red X marks.",
    4: "{M} sits cross-legged on the deck of a wooden Nile boat writing in a papyrus diary with a reed pen, calm sunny morning, a pyramid far behind him.",
    5: "{S}Left side: a modern stick figure tourist in a sun hat and sunglasses holding a camera, crossed out by a big red X. Right side: {C} carrying a coil of thick rope on his shoulder, a huge pyramid behind him.",
    6: "{C} holds a papyrus scroll in one hand and a rope in the other, standing in a small mud-brick town below a huge pyramid under construction, curious smile.",
    7: "{C} scratches his head between two speech bubbles, one with a chain icon and one with a little green alien head, a big question mark above him, plain cream background.",
    8: "{CARD}three icons in a row: a loaf of bread, a big round-bellied clay jar and a papyrus scroll, with the hand-lettered words \"BREAD BEER BOSS\".",
    9: "{CARD}a plate with a round loaf of bread and a clay beer jar, tiny sparkles around them and a small pyramid icon behind, the hand-lettered words \"THE LUNCH\".",
    # 1. O diário e o chefe
    10: "{M} stands proudly on the bank of the Nile holding a papyrus scroll, a wooden boat behind him, bright morning sun.",
    11: "{M} holds a papyrus scroll under one arm like a clipboard and points at a wooden boat with his other hand, hands-on foreman pose, sunny river bank.",
    12: "{M} stands in front of a long row of many identical stick figure workers in white kilts lined up on the river bank, seen from the front, green fields behind.",
    13: "{BOAT} sailing on the wide blue Nile between green fields, a pale limestone quarry in the cliffs far behind it, two stick figure rowers at the oars, bright sun.",
    14: "{CARD}a small hand-drawn boat on a blue river between two icons, a quarry on the left and a pyramid on the right, curved loop arrows, the hand-lettered words \"4 DAYS\".",
    15: "{CARD}a long papyrus scroll unrolled with a table of tiny pictures in rows: boats, moons and suns, the hand-lettered word \"TIMESHEET\" on top.",
    16: "{K} sits on a golden throne in front of a stone temple, sunlit, arms crossed, plain desert behind him.",
    17: "{PYR} under a bright turquoise sky seen from a low angle, a tiny stick figure standing at the bottom for scale, warm light.",
    18: "{CARD}a long horizontal timeline with a pyramid icon on the far left, a queen's gold crown in the middle and a rocket next to a moon on the far right, the hand-lettered word \"CLEOPATRA\" above the crown.",
    19: "A tall layered cake with each layer a different color and a tiny pyramid on top, plain cream background.",
    20: "A busy office with a stick figure clerk sitting among stacks of papyrus scrolls and baskets, drawing lines on a big table of boats and numbers.",
    21: "A stick figure clerk hands baskets of loaves and fish to a line of workers while a scribe records it on a papyrus scroll, warm light.",
    22: "{SC} buried up to his chin in a mountain of papyrus scrolls, smiling apologetically with a shrug.",
    # 2. Os mitos
    23: "{CARD}a big red stamp reading \"MYTH\" next to a hand-drawn chain link icon and the hand-lettered word \"SLAVES\".",
    24: "{HERO} sits on a wooden stool writing on a wax tablet beside a huge pyramid, curious face, golden afternoon light.",
    25: "A huge crowd of tiny stick figure workers covering the sand around a pyramid, a Greek traveler in front holding up a wax tablet with a big scribbled number.",
    26: "{CARD}three vegetables in a row: a radish, an onion and a leek, plus a small pile of shiny silver bars, the hand-lettered word \"SILVER\".",
    27: "A giant mountain of onions with a tiny stick figure standing in front of it with wide eyes, plain cream background.",
    28: "{HERO} holds a hand to his chin with a thought bubble full of question marks, a stick figure translator reading from a wall in front of them, sandy background.",
    29: "{CARD}on the left an orange-brown copper chisel and saw with a green check mark and the hand-lettered word \"COPPER\", on the right a grey iron axe with a thick red X.",
    30: "A papyrus accounting page with holes torn through it, a stick figure accountant peeking out through one hole with a funny face.",
    31: "A long sandy slope below a huge pyramid with rows of small mud-brick tombs and flat stone tombs, stick figure archaeologists with brushes walking between them, warm light.",
    32: "A modern stick figure tourist on a horse stumbling beside a low stone wall, the horse's front legs bent and the tourist wobbling, a stick figure archaeologist watching nearby, dust.",
    33: "{CARD}a big hand-drawn grid of many small tomb icons, the hand-lettered words \"700 GRAVES\".",
    34: "{ARCH} points at a small tomb right at the foot of a big pyramid, thoughtful, golden light.",
    35: "A narrow stone chamber with a low ceiling, simple red-ochre painted marks on the wall blocks drawn as plain shapes, a stick figure explorer with a lantern looking at them.",
    36: "{CARD}a hand-painted red banner reading \"FRIENDS OF KHUFU\" with a small team flag beside it.",
    37: "A team of stick figure workers in white kilts posing proudly in a row with arms around each other's shoulders, big smiles, one holding a flag with a smiling pyramid.",
    38: "A cute little green alien with big black eyes holding an empty plate and looking hungry beside a table with a single loaf of bread, plain cream background.",
    39: "{CARD}five small icons in a row: a papyrus scroll, a boat, a mud-brick house, a tomb and a copper chisel, the hand-lettered words \"THE EVIDENCE\".",
    40: "{CARD}a plain oval ring with the hand-lettered word \"KHUFU\" inside it, red paint style, small stick figure workers painting it.",
    41: "A small green alien stands in front of an empty wall and an empty papyrus, shrugging with open palms, plain cream background.",
    42: "A big crowd of cheerful stick figure workers in white kilts raising their fists in front of a pyramid, golden sunset.",
    # 3. Você é convocado
    43: "{C} looks directly at the viewer and points at himself with a thumb, surprised, plain cream background.",
    44: "{C} stands in a small green field beside the blue Nile with a few palm trees and a mud-brick hut, holding a wooden hoe, sunny.",
    45: "{C} holds up a big sign that reads \"MADE UP\" and winks, plain cream background.",
    46: "The Nile in flood: wide blue water covering green fields up to the doors of mud-brick houses on little hills, palm trees standing in the water, {C} sitting on a flat roof.",
    47: "{C} sits on the floor of a small mud-brick house with {FAM}, an almost empty bowl and a single loaf of bread on the floor, worried faces.",
    48: "{OFF} unrolls a long papyrus list at the door of a mud-brick hut, {C} looking at it with wide eyes.",
    49: "A long line of stick figure men in white kilts walking along a dusty path from small villages toward a distant pyramid, bundles on their shoulders.",
    50: "{CARD}on the left a few small stick figures labeled \"ALL YEAR\", on the right a big crowd labeled \"FLOOD TIME\", a small blue wave icon in the middle.",
    51: "{K} hands a small sack of grain to a stick figure worker, many workers lining up behind, warm light.",
    52: "{ARCH} stands in a dig pit at Giza, a speech bubble over his head with a chain icon crossed out by a red X, sunny.",
    53: "{CARD}a hand-drawn balance with the word \"DUTY\" on the left pan and the word \"PRIDE\" on the right pan, both pans level.",
    54: "{OFF} holds out a big loaf of bread and a clay jar toward {C}, who looks at them hopefully with raised eyebrows, plain sandy background.",
    55: "A wide wooden boat full of stick figure workers in white kilts sitting side by side, drifting down a blue river with green fields on both banks.",
    56: "Many stick figure workers divided into small groups, each group gathered around a small colored flag on a pole, seen from above on sand.",
    57: "{CARD}a small crowd of tiny stick figures labeled \"5,000\" and a huge crowd labeled \"40,000\", with a double arrow between them.",
    58: "{C} sits at the front of a boat with other workers, hair blowing, looking ahead, river and palm trees around.",
    59: "{PYR} shining white and smooth in the sun, seen from far across green fields, {C} small in the foreground with his mouth open.",
    60: "{S}Left side: the Great Pyramid today, rough stepped yellow stones with only a small pale smooth patch at the bottom. Right side: the same pyramid smooth and gleaming bright white-yellow, with sparkle lines.",
    # 4. A cidade dos operários
    61: "{C} walks down a dusty path toward a town of flat-roofed mud-brick houses at the foot of a big pyramid, a small bag on his shoulder.",
    62: "A wide view of a sandy plateau with a tall pyramid on the left, a big lion-bodied statue with a human head and a striped headcloth lying down in the middle, and a long thick stone wall running across the sand with a small town beyond it.",
    63: "{CARD}a papyrus scroll sign with a small pyramid drawn on it and the hand-lettered words \"LOST CITY\".",
    64: "{CARD}a timeline with a big pyramid on the left, an arrow, and a small town with two smaller pyramids on the right, the hand-lettered word \"LATER\" above the arrow.",
    65: "Two smaller pyramids standing next to a big one, with a little mud-brick town in front of them, sunny day.",
    66: "A narrow sandy street between small flat-roofed mud-brick houses, stick figure people sitting at doorways, a long low building with a wall at the end of the street, warm sunset.",
    67: "{CARD}a row of many small bakery ovens in a line, each with a little loaf and a tiny steam curl, the hand-lettered word \"BAKERIES\".",
    68: "{CARD}a temple icon and a tomb icon both crossed out by red X marks, and a big round loaf of bread with a green check mark, the hand-lettered word \"BAKERIES\".",
    69: "A big mud-brick bakery with rows of tall clay pots set in the ground and glowing ash, a stick figure baker pulling out round loaves with a wooden paddle, smoke rising, warm orange light.",
    70: "A round-bellied clay jar of beer with foam on top standing beside a loaf of bread on a small low table, a stick figure worker eating bread next to it, plain cream background.",
    71: "A cutaway view of a long low mud-brick hall with a row of narrow doorways, rows of sleeping mats inside with tiny stick figures lying on them, warm lamp light.",
    72: "{ARCH} points at a plan drawn on a big sheet of paper showing a long hall divided into small rooms, thoughtful face, a question mark above.",
    73: "{C} lies on a thin reed sleeping mat on the floor of a long hall between many other sleeping stick figure workers, small snoring Z letters, dim light.",
    74: "A wide view with a pyramid on the left, a small town of mud-brick houses with smoking bakery chimneys in the middle and green fields with boats on the right, thin dashed lines connecting them, bright day.",
    # 5. Pão, cerveja e salário
    75: "{C} sits on the ground with a round loaf of bread in one hand and a clay beer cup in the other, taking a happy bite, plain cream background.",
    76: "{CARD}six small food icons in two rows: a loaf, a fish, a fruit, a honey pot, a small cake and a beer jar, the hand-lettered words \"THE MENU\".",
    77: "A small clay pot of honey and a few dates on a plate with a gold crown above it, a stick figure worker looking at them longingly from a distance, plain cream background.",
    78: "{CARD}a hand-drawn coin crossed out by a thick red X, next to a loaf of bread, a jar and a folded white cloth with green check marks, the hand-lettered words \"PAY = FOOD\".",
    79: "A stick figure worker holding a huge stacked sandwich of flat bread, onions and fish in both hands and grinning, plain cream background.",
    80: "A pile of cartoon animal bones, cow ribs, sheep bones and fish skeletons, on sandy ground with a magnifying glass over them.",
    81: "A big round roasted piece of beef on a plate with a golden shine and sparkles, plain cream background.",
    82: "{C} looks at the viewer with one raised eyebrow and a finger up, plain cream background.",
    83: "A stick figure in a fine pleated linen kilt and a wide gold collar eating a big piece of roasted meat at a table while a thin stick figure worker watches him from the doorway.",
    84: "Stick figure workers sitting around a big clay pot of steaming soup with bones sticking out, each holding a bowl, warm firelight.",
    85: "{C} eats a bowl of soup and smiles with his eyes closed, steam rising, cozy light.",
    86: "{CARD}a cow icon with the hand-lettered number \"11\" and a goat icon with the hand-lettered number \"37\", the hand-lettered words \"EVERY DAY\".",
    87: "A long line of cattle and sheep walking along a dusty road toward a town beside a pyramid, stick figure herders leading them, golden dust.",
    88: "{CARD}a pyramid on the left, a loaf of bread, a boat and a papyrus scroll on the right, with an equals sign between them and the hand-lettered words \"SUPPLY CHAIN\".",
    # 6. O trabalho
    89: "A pale limestone quarry on a sandy plateau beside a pyramid, stick figure workers cutting a big square block out of the rock, dust in the air.",
    90: "Stick figure workers kneel on a big stone block and cut grooves with orange-brown copper chisels and wooden mallets, rock dust flying.",
    91: "{CARD}a copper chisel, a copper saw and a round stone hammer in a row, the chisel and saw colored orange-brown, the hand-lettered word \"COPPER\".",
    92: "{BOAT} passing a white quarry on the river bank, the pyramid far in the distance, two stick figure rowers, bright day.",
    93: "A long wooden Nile boat carrying one huge dark red-grey granite beam along its deck, many oars, a stick figure captain at the front, rocky orange desert hills on the bank.",
    94: "A stone chamber with a flat ceiling made of enormous granite beams, a tiny stick figure standing on the floor looking up, lantern light.",
    95: "{SLED} dragged by a long line of stick figure workers pulling thick ropes and leaning forward, on a sandy path, dust.",
    96: "A stick figure worker kneels on the front of a stone-loaded sled and pours water from a clay jar onto the sand in front of it.",
    97: "A painted wall in simple flat side-view style in red, ochre, blue and black on pale plaster, showing a giant seated statue on a sled pulled by many tiny figures in rows and one small figure pouring water in front.",
    98: "A stick figure physicist in a lab coat and glasses pulls a small toy sled across a tray of sand with a string, a scale beside it, modern lab bench.",
    99: "{CARD}two small sleds side by side: on the left a sled on dry sand with a big pile in front labeled \"DRY\", on the right a sled on wet sand with a thin arrow labeled \"WET\", the hand-lettered words \"HALF THE PULL\" below.",
    100: "{C} holds a bucket of water and winks at the viewer with a thumbs up, a stone-loaded sled behind him, plain sandy background.",
    101: "{CARD}a pile of tiny square stone blocks stacked into a pyramid shape, the hand-lettered words \"2.3 MILLION\".",
    102: "{CARD}a calendar page with a small stone block icon, the hand-lettered number \"250\" and the words \"A DAY\".",
    103: "{CARD}a stopwatch icon next to a small stone block, the hand-lettered words \"EVERY 2 MINUTES\".",
    104: "{C} hauls on a rope with other workers, face red and sweating, drops of sweat flying, another worker resting on a stone block behind him.",
    105: "{C} places one square stone block into a giant puzzle shape of a pyramid made of many stones, proud smile, sunny.",
    # 7. Como subiram as pedras
    106: "A giant question mark drawn with sand and stones in front of a pyramid, stick figure archaeologists scratching their heads around it.",
    107: "{CARD}four icons in a row with green check marks: a stone block, a sled, a copper chisel and a boat, the hand-lettered words \"THEY AGREE\".",
    108: "A stick figure engineer draws a sloped ramp leading up the side of a small pyramid model on a table, pointing, other stick figures nodding.",
    109: "{CARD}four small pyramids in a row, each with a differently shaped ramp, a big question mark above them.",
    110: "A small pyramid with one very long straight ramp running far out across the sand, tiny stick figure workers hauling a sled up it, the ramp huge and tall.",
    111: "A pyramid with a ramp winding around it in a spiral all the way to the top, stick figure workers climbing with sleds.",
    112: "A cutaway view of a pyramid with a tunnel spiraling inside it, a stick figure architect pointing at it, tiny workers hauling in the tunnel.",
    113: "{CARD}four small ramp pyramids in a row with a big thick red question mark and the hand-lettered words \"NOT PROVEN\".",
    114: "A pale alabaster quarry in a barren desert valley, light stone cliffs, stick figure archaeologists with notebooks standing at the edge, bright sky.",
    115: "A ramp cut into quarry rock, with a wide sloped path in the center and a staircase on each side, rows of small round holes along both staircases, wooden tools beside it.",
    116: "Stick figure workers on the staircases pulling ropes tied to wooden posts set in the holes, a sled with a big stone block going up the center ramp.",
    117: "{CARD}a steep slope triangle with a sled on it and the hand-lettered words \"20% SLOPE\" with an arrow pointing up.",
    118: "A stick figure archaeologist holds up one hand like a stop sign and a pale alabaster block in the other, a big grey pyramid far behind him with a question mark above it.",
    119: "An aerial cartoon view of a wide blue river arm curving along the edge of a green valley and passing right at the foot of the pyramids, drawn as a dotted lost river branch.",
    120: "A wooden boat full of stick figure workers and stone blocks arriving at a short stone causeway at the foot of the pyramid, a ramp leading up from the water, golden light.",
    121: "A man-made harbor basin cut into the sand with stone quays at the edge of a plateau, three boats unloading stone blocks, stick figure workers on the quay, a pyramid in the background.",
    122: "A river drawn as a conveyor belt, small boats on it carrying blocks along toward a pyramid, funny cartoon belt with rollers.",
    123: "{CARD}a pyramid cutaway with a glowing hidden empty room inside and tiny particle streaks coming from below, the hand-lettered words \"HIDDEN VOID\".",
    124: "{CARD}a long empty room shape with a measuring ruler beside it and a question mark, the hand-lettered words \"30 METERS\".",
    125: "{PYR} at night under a sky full of stars with a soft golden glow, a stick figure archaeologist standing in front looking up with a question mark above.",
    # 8. Acidentes e médicos
    126: "A stick figure worker with a bandaged arm in a sling sits on a stone block, other workers hauling in the background, dust and sweat.",
    127: "A stick figure archaeologist with a magnifying glass studies a single long bone lying on a white cloth on a table, notes beside him.",
    128: "{CARD}three icons in a row: a bent spine, a stiff knee and a bandaged arm, the hand-lettered words \"WORN OUT\".",
    129: "A close-up of a long bone with a bump where it healed, lying on a white cloth, a magnifying glass above, plain cream background.",
    130: "{CARD}a box full of tiny stick figure adults, the hand-lettered words \"204 ADULTS\".",
    131: "{CARD}a bundle of many long bones with the hand-lettered number \"2,287\" and a small red circle around a few of them with the number \"45\".",
    132: "{CARD}a long bone with a big green check mark and the hand-lettered words \"HEALED STRAIGHT\".",
    133: "{DOC} gently wraps a bandage and two wooden splints around the arm of a seated stick figure worker, calm, warm light.",
    134: "{SC} writing a medical manual on papyrus with little drawings of bandaged limbs on the sheet, a clay pot and a small oil lamp next to him.",
    135: "{CARD}a big new-looking papyrus scroll labeled \"COPY\" and a faded old scroll behind it labeled \"OLDER?\" with an arrow between them.",
    136: "{CARD}a big circle full of tiny stick figures with a small gold circle inside it, the hand-lettered words \"NOT ONLY BUILDERS\".",
    137: "{CARD}a hand-drawn clinic sign with a red cross and a big red X over it, the hand-lettered words \"FREE HEALTH CARE?\".",
    138: "{DOC} stands next to a small basket of bandages, an ointment pot and wooden splints, beside {C} who holds a sore arm.",
    # 9. Quando você morre
    139: "A long sandy slope below a big pyramid with rows of small mud-brick tombs and flat-topped stone tombs, evening light, tiny stick figure mourners.",
    140: "The low part of a cemetery with simple small mud-brick graves in rows, a stick figure family gathered around one, warm sunset.",
    141: "Higher on the slope, bigger stone tombs with small statues in front, a stick figure craftsman's family bringing bread and jars as offerings, golden light.",
    142: "A statue of a seated man in a short white kilt holding a carpenter's wooden tool, in a small stone room, lantern light, a stick figure archaeologist beside it.",
    143: "{CARD}a plain pit with a big red X on the left and a neat little tomb with a green check mark on the right.",
    144: "{CARD}four small portrait cards of stick figures each with a tool: a carpenter's wooden adze, a baker's loaf, a boat captain's oar and a scribe's reed pen, the hand-lettered words \"REAL PEOPLE\".",
    # 10. A greve
    145: "A huge pyramid with a tiny crack running through its base, stick figure workers looking up at it with worried faces.",
    146: "{CARD}a long timeline arrow to the right with a pyramid icon on the left and a rocky valley icon on the right, the hand-lettered words \"1,000 YEARS LATER\".",
    147: "{CARD}a hand-drawn calendar page with the hand-lettered words \"1157 BC\" and a small pharaoh head wearing a tall blue crown.",
    148: "A tiny village of white mud-brick houses squeezed into a rocky desert valley, a stick figure craftsman painting a tomb wall in a doorway, steep cliffs with tomb entrances above.",
    149: "{OFF} hands a big sack of grain to a worker at a stone doorway, a line of stick figure craftsmen waiting behind him.",
    150: "A crowd of angry stick figure craftsmen in white kilts walking out of a stone village gate with raised fists and open mouths, a guard watching, a speech bubble with the hand-lettered words \"WE ARE HUNGRY\".",
    151: "The back of a big stone temple with columns, a large group of stick figure workers sitting in the sand in rows with their arms crossed, calm protest.",
    152: "Stick figure workers sitting in front of a big temple shaking their heads, refusing an order from a stick figure official who points toward the village.",
    153: "Stick figure craftsmen standing in front of a golden throne room door with {K} on a throne in the distance, one worker raising his hand to speak.",
    154: "{CARD}a golden trophy cup with a small raised fist on it, the hand-lettered words \"FIRST STRIKE EVER\".",
    155: "{SC} writes quickly on a papyrus sheet in the shade while a crowd of workers shouts at him, speech bubbles with exclamation marks.",
    # 11. Fecho
    156: "{C} looks at the viewer with sweat on his forehead and a tired smile, a big pyramid behind him, golden light.",
    157: "A group of stick figure workers in matching tan headbands proudly raising a small team flag with a smiling pyramid on it.",
    158: "{C} sits beside a baker's clay oven eating bread with a beer jar at his side, relaxed, firelight, evening.",
    159: "{DOC} bandages the hand of {C}, who grimaces, plain sandy background.",
    160: "{C} stands on a hill looking at a huge shining white pyramid in the distance with a proud smile, hands on hips, sunset.",
    161: "{C} faces the viewer with a finger on his chin, thoughtful, plain cream background.",
    162: "{CARD}a loaf of bread with a curved arrow turning it into a pyramid, the hand-lettered words \"BREAD TO PYRAMID\".",
    163: "{PYR} with a cutaway of the ground in front of it showing boats, bakeries and scribes working underneath, golden light.",
    164: "{CARD}five small icons in a row: a farmer's hoe, a boat, a loaf of bread, a papyrus scroll and a bandage, the hand-lettered words \"ALL ON TIME\".",
    165: "{S}Left side: a grand pyramid in golden light. Right side: a crowd of stick figure workers with raised fists and hungry faces.",
    166: "A half-built pyramid with stick figure workers sitting on the ground with tools dropped beside them, a big empty bread basket in the foreground, quiet golden desert.",
    167: "{K} sits on a golden throne with a loaf of bread on his lap, looking at it, a pyramid behind him.",
    168: "{CARD}a speech bubble reading \"WHICH JOB NEXT?\" and a small papyrus scroll doodle.",
}


def prompt(n: int) -> str:
    t = P[n]
    for k, v in T.items():
        t = t.replace("{" + k + "}", v)
    t = t[0].upper() + t[1:]
    return f"{BASE} {BONECO} {t}" if "stick figure" in t else f"{BASE} {t}"


def cartao(n: int) -> bool:
    return P[n].startswith("{CARD}")
