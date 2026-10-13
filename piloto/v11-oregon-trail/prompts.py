"""Prompts de imagem do vídeo 11 (Oregon Trail) para o Z-Image local, um por linha numerada do roteiro.md.

prompt() põe o estilo (BASE) e, se a cena tem stick figure, a descrição do boneco (BONECO).
{CARD} = cartão de fundo branco (palavras curtas, conferir a grafia).
Sem pessoas indígenas desenhadas (cartões, mãos e paisagens). Sem violência, sangue ou corpos.
A carroça é descrita pela forma (arcos de madeira, cobertura de lona, dois bois). Época: abril a setembro de 1850.
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
    "C": "the stick figure pioneer farmer in his thirties with short messy brown hair, a wide-brimmed flat straw hat, "
         "a red checked shirt, brown trousers and sturdy brown boots",
    "W": "his stick figure wife in a long blue cotton dress, a white apron and a cloth sunbonnet",
    "K": "two small stick figure children in plain patched clothes and straw hats",
    "AK": "a stick figure pioneer mother with a brown braid, a long grey dress and a cloth sunbonnet, holding a small notebook",
    "MARCY": "a stick figure army captain in a long dark blue coat with brass buttons and a wide-brimmed dark hat",
    "H": "a stick figure man in a long tan coat and a brimmed hat with a smug smile, holding a rolled map",
    "WAG": "a small wooden wagon with a white canvas cover stretched over curved wooden hoops, four wooden wheels, "
           "pulled by two oxen",
    "OX": "a big brown ox wearing a wooden yoke across its neck",
    "CARD": CARTAO,
    "S": "Split screen divided by a vertical black dashed line. ",
}

P = {
    # 0. Abertura
    1: "{CARD}a calendar page with a small spring flower and the hand-lettered black capital words \"APRIL 1850\".",
    2: "{C} stands in a wide muddy frontier street lined with small wooden buildings and a general store, horses at a hitching post, pale spring morning.",
    3: "{WAG} packed to the roof with barrels, sacks and a rocking chair tied on the back, standing in a muddy street, {C} beside it with his hands on his hips.",
    4: "{CARD}a long winding dotted line running from a tiny covered wagon on the left to a small green hill on the right, the hand-lettered words \"2,000 MILES\" above it.",
    5: "{CARD}three small icons in a row, a gas pump, a highway road sign and a toilet, each crossed out by a thick red X.",
    6: "{C} sits on a tree stump holding a small paper pennant on a stick with a big fake smile, a bored ox behind him, plain cream background.",
    7: "{C} stands beside a wagon with his arms spread wide and a surprised face, the empty wooden seat of the wagon clearly visible.",
    8: "{C} walks with long strides along a dirt trail beside {WAG}, {W} and {K} walking behind him, a vast green prairie under a big sky.",
    9: "{CARD}a long trail of tiny footprints along a dotted line and a bandaged foot icon, the hand-lettered words \"4,000,000 STEPS\".",
    10: "{CARD}three small icons in a row, a farm field with a small house, a shiny gold nugget and a bright rising sun, the hand-lettered words \"LAND GOLD HOPE\".",
    11: "{CARD}the hand-lettered number \"20,000+\" above a long row of small wooden cross grave markers stretching to the horizon.",
    12: "{C} scratches his head with a big question mark above it and a thought bubble holding a snake, a storm cloud and a question mark, plain cream background.",
    13: "{C} lifts the last heavy sack onto {WAG} while {W} and {K} tie down the canvas, sunrise over the muddy street.",
    # 1. Por que alguém faria isso?
    14: "{C} sits at a kitchen table at night with his chin in his hand, a lit candle and a paper map in front of him, {W} sleeping in a chair behind.",
    15: "A stick figure salesman in a top hat points at a big hand-drawn poster on a wooden board showing a lush green valley with cows and a bright sun.",
    16: "{CARD}a small farm house with a field, two small stick figure adults in front of it, the hand-lettered number \"640\" and the word \"ACRES\".",
    17: "{CARD}a small farm house with a field, one small stick figure in front of it, the hand-lettered number \"320\" and the word \"ACRES\".",
    18: "A wide quiet green river valley with a winding river, rolling hills with oak trees and wildflowers, soft morning mist, a thin curl of smoke rising far away.",
    19: "{CARD}a rolled paper scroll with a big question mark above it and the hand-lettered year \"1855\".",
    20: "{CARD}a folded travel brochure with a smiling sun on the cover, its right half torn away, plain white background.",
    21: "{CARD}a shiny gold nugget in a metal pan with sparkles around it, the hand-lettered word \"GOLD\".",
    22: "{CARD}a small covered wagon icon with the hand-lettered number \"30,000\" and the year \"1849\" below.",
    23: "{CARD}a pile of many small covered wagon icons with the hand-lettered number \"55,000\" and the year \"1850\" below.",
    24: "A very long line of covered wagons waiting one behind another along a dirt road to the horizon, a bored stick figure leaning on an ox in the foreground.",
    25: "{CARD}a big circle filled with tiny stick figures, a question mark beside it and the hand-lettered number \"300,000+\".",
    26: "A stick figure with a tiny pencil and notebook stands on a wide dirt road looking overwhelmed as hundreds of tiny wagons pass in the distance.",
    27: "A modern stick figure in a baseball cap gives a thumbs up beside a small rented moving truck on a sunny road, plain cream background.",
    # 2. Dia de compras
    28: "{C} stands at the counter of a general store, shocked, while a shopkeeper stick figure in an apron holds up a very long receipt, shelves of sacks and tools behind.",
    29: "{C} counts gold coins from a leather pouch onto a store counter where a big pile already sits, a nervous sweat drop on his head, shop shelves behind.",
    30: "A storeroom with sacks of flour, barrels and sacks of beans stacked up to the ceiling, {C} looking up at them with wide eyes.",
    31: "{CARD}a taller pile of gold coins with a thought bubble holding the hand-lettered text \"TODAY: $30,000+\".",
    32: "{WAG} standing alone on a plain cream background, seen from a three-quarter front view, simple and clear.",
    33: "{CARD}a side view of a small wooden wagon bed with a long double-headed arrow below it, the hand-lettered words \"10 FEET\".",
    34: "A close-up of the back of a small wooden wagon showing a white canvas cover stretched over five curved wooden hoops, plain cream background.",
    35: "{C} squeezes into the back of a wagon packed with barrels, sacks, pots and a rocking chair, only his worried face visible between the sacks.",
    36: "{CARD}on the left a big heavy wagon with a boat-shaped swayback body and a canopy overhanging both ends, crossed out, labeled \"TOO HEAVY\", on the right a small straight-sided wagon with a green check mark, labeled \"JUST RIGHT\".",
    37: "A huge heavy wagon with a curved boat-shaped body and a canvas canopy overhanging both ends, stuck deep in mud at a river bank, two stick figures pushing from behind.",
    38: "A small wooden wagon with straight sides and a white canvas cover rolls across a sea of tall green grass like a little ship, waves of grass around its wheels.",
    39: "A big brown ox on the left and a mule on the right stand side by side facing the viewer with thoughtful faces, a big question mark between them, plain cream background.",
    40: "{CARD}on the left a mule with small motion lines labeled \"FASTER\", on the right a strong ox pulling a heavy sack labeled \"STRONGER\".",
    41: "{CARD}a big pile of small ox icons with the hand-lettered number \"36,000\" and a much smaller pile of mule icons with the number \"7,500\".",
    42: "{MARCY} stands beside a team of eight oxen in two rows holding a small price tag with the hand-lettered text \"$200\".",
    43: "A big brown ox walks calmly and steadily across a prairie at sunset, a tired mule lying down far behind it.",
    44: "A fast mule dashing ahead on a dirt path and flopped down exhausted halfway, while a calm ox keeps walking past it, wide prairie.",
    45: "A stick figure salesman in a top hat offers a paper contract to a bored ox, plain cream background.",
    # 3. O que vai na carroça
    46: "{MARCY} sits on a tree stump reading a small thick book with a brown cover, a compass and a tin cup beside him, plain cream background.",
    47: "{CARD}two calendar pages side by side, the left with a small wagon and the year \"1850\", the right with a small book and the year \"1859\".",
    48: "{CARD}a calendar page with a clock beside it and the hand-lettered words \"110 DAYS\".",
    49: "{CARD}a big sack of flour with a hand-lettered label \"150 LB\".",
    50: "{CARD}three strips of bacon on a plate with a hand-lettered label \"25 LB\".",
    51: "{CARD}on the left a coffee pot with the label \"15 LB\", on the right a sugar cube pile with the label \"25 LB\".",
    52: "A tin plate with a piece of bread and two strips of bacon, beside a tin cup of coffee on a tree stump, plain cream background.",
    53: "A brown cow with a bored face walks beside a wagon with a small white napkin tied around its neck.",
    54: "{C} stands in a general store holding a shovel in one hand and a wooden wagon wheel in the other, a thought bubble full of question marks above him.",
    55: "A big brown ox leans forward straining to pull a heavily loaded wagon uphill, sweat drops flying, the wagon piled with barrels.",
    56: "{CARD}a hand-drawn scale with a small wagon on it and the hand-lettered text \"2,500 LB MAX\".",
    57: "A happy ox pulls a modestly loaded wagon along a flat trail at a steady pace, a green check mark floating above, plain cream background.",
    58: "A rocking chair, a mirror and a dresser sit alone on a dirt trail while a covered wagon rolls away in the distance.",
    59: "The edge of a dirt trail littered with abandoned furniture, a chest of drawers, an iron stove, barrels and a spinning wheel, in a grassy prairie.",
    60: "{AK} holds a glass jar of pickles in one hand about to toss it into the tall grass, a sad look on her face, a wagon behind her.",
    61: "A big sad ox looks at a single huge pickle jar sitting on top of a wagon load, a bead of sweat on its forehead, plain cream background.",
    # 4. O problema do guia
    62: "A stick figure traveler holds a thick guidebook open and turns a map sideways, lost, a big question mark above his head, plain cream background.",
    63: "{CARD}an old book with a plain brown cover and a small map drawn on it, the hand-lettered words \"EMIGRANT GUIDE\".",
    64: "{H} writes at a wooden desk with a feather quill, a stack of papers and an inkwell, a candle lit, a smug smile.",
    65: "{H} hands a long wooden-stock rifle to {C} with a wink, plain cream background.",
    66: "{CARD}a hand-drawn simple map with a long dotted line cutting straight across a white salt flat desert from a lake on the left, a big arrow labeled \"SHORTCUT\".",
    67: "{CARD}a small paper note with only three short wobbly lines of writing and a magnifying glass over it, the hand-lettered words \"A FEW LINES\".",
    68: "{H} sits on a rock with a big smug grin holding a map upside down, a question mark above his head, plain cream background.",
    69: "{CARD}a small covered wagon on a long dotted line leading toward a snowy mountain, the hand-lettered year \"1846\".",
    70: "{CARD}a snowy mountain peak with falling snowflakes, the number \"87\" on the left, an arrow in the middle and the number \"48\" on the right.",
    71: "A quiet snowy mountain pass at dusk with a lone small wagon half buried in snow, a bare pine tree and falling flakes, silent mood.",
    72: "{C} holds up one finger with a wise face, a lightbulb above his head, plain cream background.",
    73: "{CARD}a video play button icon with a green check mark and a magnifying glass beside it.",
    # 5. Um dia na estrada
    74: "A stick figure sentry blows a brass trumpet beside a row of covered wagons while {C} sits up in his bedroll with messy hair and tired eyes, pink sunrise on the prairie.",
    75: "A busy camp at dawn, stick figures hitching oxen to wagons, a woman cooking at a campfire, kids chasing cattle, a row of covered wagons.",
    76: "A wagon master in a brimmed hat stands on a wagon seat shouting with a big speech bubble holding an exclamation mark, a line of wagons ready behind him, morning light.",
    77: "A close-up of a pair of stick legs in sturdy boots walking along a dirt trail beside a big wooden wagon wheel, small dust puffs.",
    78: "{CARD}a small covered wagon with arrows beside it and the hand-lettered text \"12-15 MILES\" above it.",
    79: "{CARD}a stick figure runner with a sweatband and a determined face, a few cows running behind him, the hand-lettered words \"EVERY DAY\".",
    80: "Stick figures rest in the shade under a wagon at noon with tin cups, the oxen unyoked and grazing nearby, the sun high above.",
    81: "A bird's-eye view of covered wagons arranged in a big circle on a prairie with oxen inside the circle and a small campfire in the middle.",
    82: "Oxen grazing calmly inside a circle of wagons at evening, a stick figure leaning on a wagon wheel watching them, warm orange light.",
    83: "A vast flat prairie with tall grass, one lonely tree far away and a tiny wagon on the trail, a big empty sky.",
    84: "A woven basket full of flat round dried brown discs, plain cream background.",
    85: "{W} and {K} walk across the prairie at sunset carrying big sacks of flat brown discs over their shoulders.",
    86: "A campfire with an iron pot on a tripod and a skillet of bacon, smoke rising, a tin coffee pot at the edge, a covered wagon behind.",
    87: "{CARD}a stack of old diaries tied with a ribbon, the hand-lettered words \"103 WOMEN\".",
    88: "Three small scenes in one image: a woman cooking at a campfire, a woman driving two oxen with a long stick, a woman rocking a baby in a wagon.",
    89: "{AK} writes in her small notebook by candlelight inside a wagon while rain drums on the canvas, dim blue light.",
    90: "{AK} sits wrapped in a shawl by a campfire with a hand on her rounded belly, small children sleeping near her, night.",
    91: "{CARD}a deck chair and a drink with a little umbrella, crossed out by a big red X, the hand-lettered words \"NOT A VACATION\".",
    92: "{C} seen from behind walks slowly on a dirt trail behind the rear end of an ox, a bored look in the thought bubble, an endless horizon ahead.",
    # 6. Os rios
    93: "A wide brown river flowing across a prairie, covered wagons lined up on the bank in the distance, big sky.",
    94: "{CARD}a wide blue river with a small bridge icon crossed out by a big red X.",
    95: "A covered wagon floating across a river on a raft of logs, stick figures pulling a rope, oxen swimming beside it.",
    96: "{CARD}a flat wooden ferry boat carrying a small wagon and tied to a rope, the hand-lettered text \"$4 PER WAGON\".",
    97: "A very long line of covered wagons waiting on a riverbank, stick figures sitting bored on the ground and on wagon tongues.",
    98: "Stick figures build a raft from two wagon boxes tied together with thick ropes on a riverbank, tools and planks around.",
    99: "Women and children wait on the riverbank holding bundles and watching, while a raft with a wagon moves far out on the water.",
    100: "An ox with a surprised face leaps off the side of a small paddle steamboat into the river, a big splash, stick figures on deck staring with open mouths.",
    101: "An ox swims confidently across a river with a smug face and a tiny thought bubble holding a map with a dotted line.",
    102: "A river with a red warning triangle on its bank and a wooden wagon wheel poking out of the water, stick figures standing back on the shore looking worried.",
    103: "A dry cracked brown riverbed under a blazing sun, a single ox with a drooping head standing next to a wagon, heat shimmer lines.",
    104: "{CARD}a single big water drop beside a wooden bucket, the hand-lettered word \"WATER\".",
    105: "{MARCY} points at a small pot boiling over a fire next to a green stagnant pond, plain cream background.",
    106: "{C} looks at a tin cup of cloudy water with a doubtful face, a wagon camp in the background.",
    # 7. A doença
    107: "A lone wooden grave marker on a vast prairie at dusk with a wagon trail passing by, quiet mood.",
    108: "{CARD}the single hand-lettered black capital word \"CHOLERA\" in big clear letters with a few small green bubbles around it.",
    109: "{CARD}a magnified round drop of water with tiny green wiggly microbes inside, a magnifying glass beside it.",
    110: "A crowded campsite on a creek with dozens of wagons and tents, a long line of stick figures filling buckets from the single small creek, hazy light.",
    111: "{CARD}a calendar page with a small spring flower, the hand-lettered words \"EVERY SPRING\" and a small town icon with a red warning triangle.",
    112: "A wide prairie at night with many small campfires scattered in a long line along a trail and a thin pale green mist drifting over them.",
    113: "{CARD}on the left a low morning sun with a smiling stick figure, on the right a high noon sun with a small wooden grave marker, the hand-lettered words \"MORNING\" and \"NOON\".",
    114: "{W} holds a small medicine bottle and a spoon over a stick figure lying under a blanket inside a wagon, dim lantern light, caring mood.",
    115: "A wide prairie campsite at dusk with a row of small wooden grave markers beside a trail, many of them, quiet golden light.",
    116: "A wide prairie at dusk with a long line of wagons passing and many small wooden grave markers on both sides of the trail.",
    117: "{CARD}the hand-lettered number \"20,000+\" above a row of small grave markers.",
    118: "{CARD}four small icons in a row, a green water drop, a broken wagon wheel, a few waves and a medicine bottle, the hand-lettered words \"ALL CAUSES\".",
    119: "{CARD}a wobbly hand-drawn range bar with a question mark at each end, the hand-lettered words \"ROUGH ESTIMATE\".",
    120: "A grassy hillside with scattered small flat stones and tall grass swaying, quiet golden light, a faint wagon trail in the distance.",
    121: "A stick figure historian in glasses holds a pointer next to a chalkboard showing two bars of nearly the same height, one labeled \"TRAIL\" and the other \"HOME\".",
    122: "A busy river port town of 1849 with brick buildings and two paddle steamboats at a dock, grey cloudy sky.",
    123: "{CARD}a wooden water bucket with a big red warning triangle above it.",
    # 8. O mito do ataque
    124: "A movie theater screen showing a circle of covered wagons with a cartoon explosion burst, an audience of stick figures eating popcorn in the dark.",
    125: "{CARD}a magnifying glass over a clipboard with tally marks, the hand-lettered words \"LET'S CHECK\".",
    126: "{CARD}a small covered wagon icon next to the hand-lettered number \"362\", the years \"1840-1860\" below.",
    127: "{CARD}the hand-lettered number \"426\" in big letters and below it the hand-lettered words \"NATIVE PEOPLE\".",
    128: "A wall calendar with its pages flying away one by one in the wind over a prairie, a tiny wagon in the distance.",
    129: "{CARD}a magnifying glass over a small cluster of dots, the hand-lettered words \"A FEW HUNDRED\".",
    130: "{CARD}two bars side by side, a very tall bar labeled \"DISEASE\" and a tiny bar labeled \"CONFLICT\".",
    131: "A stick figure park ranger in a green uniform and a flat brimmed hat holds a pointer next to a screen showing a cartoon wagon circle with a red X.",
    132: "Two big simple hands shaking each other in front of a sunset prairie, a wagon trail winding behind them.",
    133: "{CARD}two bars side by side, the shorter bar labeled \"EMIGRANTS\" and the slightly taller bar labeled \"NATIVE PEOPLE\".",
    134: "A nervous stick figure sits on a wagon seat clutching a long old rifle across his chest and looking around with wide eyes at an empty horizon, a sweat drop.",
    135: "Two small stick figure girls hide behind a bundle of blankets in a wagon peeking out with huge eyes through the canvas flap at a sunny prairie.",
    136: "A small open notebook page with handwritten scribble lines and a pencil beside it on a wooden wagon seat, warm light.",
    137: "{C} sits on guard by a campfire at night with wide eyes, glancing at the dark, tense mood, a wagon behind him.",
    138: "{CARD}a movie clapperboard and a big red question mark, the hand-lettered words \"MOVIE VS REAL LIFE\".",
    # 9. Os povos que já estavam lá
    139: "A wide prairie with a faint dirt trail, a hawk in the sky and a small hill, soft golden light.",
    140: "{CARD}a simple hand-drawn map shape with many overlapping circles in different colors, the hand-lettered words \"MANY NATIONS\".",
    141: "A flat wooden ferry raft carrying a covered wagon across a calm river, a rope stretched to the far bank, quiet morning light.",
    142: "{CARD}a coin on the left and a handshake on the right with a thin slash between them, the hand-lettered words \"PAID OR FREE\".",
    143: "A wooden table in a prairie camp with a stack of folded shirts, a hammer, a hand mirror and a cow tied beside it, sunny day.",
    144: "A big heavy wagon wheel in the foreground rolling over a field of wildflowers, flattened grass behind it.",
    145: "A bird's-eye view of a wide strip of bare brown flattened ground cutting through a green prairie, cattle grazing the last green grass at its edges.",
    146: "A herd of brown bison grazing and walking far away across a wide prairie, a faint wagon trail crossing in front of them.",
    147: "{CARD}a dotted trail line with a small green cloud puffing along it, the hand-lettered word \"SPREAD\".",
    148: "{CARD}a big circle made of many small round dots around a central fire, the hand-lettered words \"HORSE CREEK 1851\".",
    149: "{CARD}a road sign on a dirt trail with a green check mark and a handshake icon, the hand-lettered words \"SAFE PASSAGE\".",
    150: "{CARD}the hand-lettered words \"50 YEARS\" crossed out and the words \"10 YEARS\" written next to it, a paper document in the background.",
    151: "{S}Left side: a prairie seen from a wagon seat with oxen heads in the foreground. Right side: the same prairie seen from a hill with a tiny wagon train far away.",
    152: "A wide sunset landscape with a wagon trail receding into the distance, empty hills and a big sky, quiet.",
    # 10. Montanhas e o fim da estrada
    153: "A huge tall rounded granite rock rising from flat grassland with small covered wagons camped at its base, sunny.",
    154: "A stick figure traveler paints his name on a big rock with a brush and a bucket of tar, many scribbled names already covering the rock, a wagon behind.",
    155: "{CARD}a big rock outline filled with tiny scribbles and the hand-lettered number \"5,000+\".",
    156: "A wide gentle mountain pass between low rounded hills with a smooth wide valley and a wagon train winding across, bright sky.",
    157: "{CARD}a wide valley with a double-headed arrow across it and the hand-lettered words \"12 MILES WIDE\".",
    158: "A hot dry landscape of sagebrush with a lone wagon and tired oxen with drooping heads, harsh sun, {C} leading an ox by a rope.",
    159: "{C} stands at a fork in the trail with two wooden signposts pointing different ways, a big question mark above his head.",
    160: "{S}Left side: a flat wooden boat loaded with a wagon floating down a wide river between forested cliffs. Right side: a narrow dirt road winding through tall pine trees around a snowy mountain.",
    161: "{CARD}a simple map with a trail ending at a small town marker, the hand-lettered words \"THE DALLES\".",
    162: "{CARD}a wooden barrier across a dirt road with a sign and a coin, the hand-lettered text \"$5 PER WAGON\".",
    163: "A very steep forested hill with a covered wagon being lowered on thick ropes tied around a tree trunk, stick figures holding the ropes, dramatic angle.",
    164: "Stick figures lean back pulling a thick rope wrapped around a big tree trunk, lowering a wagon with chained wheels down a steep slope.",
    165: "A deep U-shaped groove worn into a steep hillside by ropes, a tiny stick figure standing at its bottom beside a tree, towering walls.",
    166: "{CARD}a wooden road sign with a big arrow pointing downhill and a toll gate, the hand-lettered words \"ONE WAY\".",
    # 11. Chegada
    167: "{CARD}a simple map pin on a small town marker, the hand-lettered words \"OREGON CITY\".",
    168: "{AK} smiles softly holding her notebook, plain cream background.",
    169: "{AK} writes the last line in her notebook sitting on a wagon seat in light rain with a small farm field in front of her, gentle light.",
    170: "A stick figure farmer shakes hands with another stick figure farmer while two oxen are led away, a small log cabin in the background.",
    171: "{CARD}two ox heads and an equals sign beside a green field, the hand-lettered words \"320 ACRES\".",
    172: "{AK} sits holding a tiny baby wrapped in a blanket in front of a small log cabin, other children near her, warm light.",
    173: "{CARD}a small steam locomotive with a puff of smoke, the hand-lettered year \"1869\".",
    174: "{CARD}a steam locomotive beside a clock, the hand-lettered words \"2 WEEKS\".",
    175: "Two deep parallel grooves worn into a grassy hillside running into the distance, a small wooden marker sign beside them, golden light.",
    176: "{CARD}a big hand-drawn question mark above a small covered wagon.",
    177: "A long procession of ordinary stick figure families walking beside covered wagons across a wide green prairie, soft golden light.",
    178: "A single wooden bucket close-up with a drop of water sparkling above it, plain cream background.",
    179: "A green river valley seen at sunrise from a hill, a quiet river, a faint column of smoke from a distant camp, a wagon trail arriving.",
    180: "{CARD}a split card divided by a thin vertical line, on the left a small farm with a smiling sun, on the right the same valley with a question mark and a faint trail of footprints.",
    181: "{C} stands in the muddy street in front of the loaded wagon, deep in thought, sunrise light.",
    182: "{C} looks down at his boots and then at the long road ahead, a big thought bubble holding a farm and a question mark.",
    183: "{CARD}a speech bubble holding the hand-lettered words \"WHAT WOULD YOU LEAVE?\" and a small covered wagon below it.",
}


def prompt(n: int) -> str:
    t = P[n]
    for k, v in T.items():
        t = t.replace("{" + k + "}", v)
    t = t[0].upper() + t[1:]
    return f"{BASE} {BONECO} {t}" if "stick figure" in t else f"{BASE} {t}"


def cartao(n: int) -> bool:
    return P[n].startswith("{CARD}")
