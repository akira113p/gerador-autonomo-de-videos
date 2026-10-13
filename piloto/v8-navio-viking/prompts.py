"""Prompts de imagem do vídeo 8 (navio viking, Islândia e Groenlândia, ano 985) para o Z-Image local, um por linha numerada do roteiro.md.

prompt() põe o estilo (BASE) e, se a cena tem stick figure, a descrição do boneco (BONECO).
{CARD} = cartão de fundo branco (palavras curtas, conferir a grafia).
Sem sangue, sem combate, sem corpos. O elmo é sempre uma calota redonda de ferro com protetor de nariz.
O navio dos colonos é o knarr (casco largo, uma vela quadrada); o navio longo e estreito só aparece nas cenas de navio de guerra.
Nenhum objeto moderno, salvo nas cenas marcadas de réplica de museu, de 1893 ou de gag.
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
    "C": "the stick figure farmer with short messy brown hair, a tan wool tunic with a rope belt, brown trousers, "
         "soft leather shoes and a grey wool cloak fastened with a round brooch",
    "W": "his stick figure wife with long braided hair under a white head cloth, a long blue wool dress and a brown apron",
    "K": "two small stick figure children in simple wool tunics",
    "E": "the stick figure Erik the Red, a broad man with a big bushy red beard and long red hair, a green tunic with a wide belt "
         "and a dark cloak, a confident grin",
    "L": "the stick figure Leif, a young man with light brown hair, a blue tunic and a hooded dark-blue cloak, a thin gold ring on his arm",
    "B": "the stick figure sailor Bjarni with a grey beard and a hooded blue cloak, squinting",
    "IBN": "the stick figure traveler Ibn Fadlan in a long cream robe with a white cloth wrapped around a small cap, holding a scroll and a reed pen",
    "RUS": "stick figure traders with beards in wool tunics, wide belts and round fur caps",
    "SH": "stick figure sailors in wool tunics, hoods and woolen caps",
    "KNARR": "a wide wooden cargo ship with a deep rounded belly, high curved front and back posts, overlapping planks like roof shingles, "
             "one short mast with one big square red-and-cream striped sail, a long steering paddle at the back on the right side",
    "LONG": "a long narrow wooden ship with a tall curved front post carved like an animal head, a row of oars on each side, "
            "round painted shields along the rail and one square striped sail",
    "HELM": "a plain round iron helmet with a nose guard",
    "CARD": CARTAO,
    "S": "Split screen divided by a vertical black dashed line. ",
}

P = {
    # 0. Abertura
    1: "{CARD}a calendar page with a small sun above and the hand-lettered black capital words \"SUMMER 985\", small waves doodled below.",
    2: "{C} stands in front of a low turf-roofed farmhouse in western Iceland looking at a thin cow and a patch of rocky green grass, grey sky, a small sigh cloud above his head.",
    3: "Inside a farmhouse, {C} reaches for the handle of a heavy wooden door with a surprised face, warm light under the door and a hand-drawn knock mark on the wood.",
    4: "{E} stands at the door of a turf farmhouse holding a rolled map and grinning widely, a tiny dark storm cloud floating over his head.",
    5: "A wooden sign planted in green grass with a big hand-lettered \"FOR SALE\" on it, a wide fjord and mountains behind it, sunny.",
    6: "{CARD}three simple icons in a row: a green hill, a wooden farmhouse and a cow, the hand-lettered black capital words \"FREE LAND\" above them.",
    7: "{CARD}the hand-lettered black capital word \"GREENLAND\" in big letters with a small green sprout on top and a smiling sun, plain white background.",
    8: "{C} sits on a grassy cliff edge above a wide empty ocean, a small bundle beside him, {W} and {K} behind him and a cow tied to a post, a worried face looking at the horizon.",
    9: "{C} waves at the viewer with a big smile, a rope over his shoulder, plain cream background.",
    10: "A long fast-looking warship with a carved animal head is crossed out by a thick red X on the left, next to {KNARR} with a cow looking out from it and a green check mark on the right, plain cream background.",
    11: "{C} flips through a pile of old storybook pictures of Vikings on a table, shaking his head with a skeptical face, cozy warm room.",
    # 1. O vendedor
    12: "A steep Norwegian fjord with tall green mountains and a small wooden farm on the shore, a small stick figure toddler with a red tuft of hair waving at the door.",
    13: "A stick figure father and a small boy with a red tuft of hair carry bundles up a gangplank onto {KNARR} at a fjord shore, worried looks, grey morning.",
    14: "{E} shrugs with open hands and an innocent smile, a small cloud of tiny question marks above his head, plain cream background.",
    15: "A big outdoor assembly on a grassy plain with many stick figures in cloaks standing in a half circle, one on a rock pointing a long finger at {E} who stands alone with his head down, blue sky.",
    16: "{E} stands at the front of {KNARR} at sea, one hand over his eyes, looking toward a clear western horizon with an orange sunset glow.",
    17: "{E} walks along the shore of a wild green fjord with tall grey mountains and floating ice, a small boat pulled up on the beach, a few seabirds, wide shot.",
    18: "{E} walks along a row of turf farmhouses in Iceland knocking on doors with a rolled map under his arm, farmers peeking out of the windows.",
    19: "{CARD}a big white-blue iceberg and a snowy mountain with a snowflake, the hand-lettered black capital word \"ICE\" below them.",
    20: "{CARD}a hand-drawn paper tag with a pencil and the hand-lettered black capital words \"NEW NAME\".",
    21: "{E} paints a big wooden signboard with bright green leaves and a happy sun using a thick brush, standing on a small ladder, sunny.",
    22: "{E} whispers to a small group of farmers with cupped hands, they smile with sparkling eyes, thought bubbles with green meadows float above them.",
    23: "A glossy cartoon billboard showing a big green meadow with flowers, a tiny ice mountain hiding behind in the corner, {E} winking beside it.",
    24: "{CARD}a row of many small wooden ships on blue waves with the hand-lettered black number \"25\" in big digits above them and the word \"SHIPS\".",
    25: "{CARD}a big hand-lettered \"14\" in green on the left and a big \"11\" in red on the right with a small question mark between them, plain white background.",
    # 2. O navio errado
    26: "{C} looks up with sparkly eyes, a thought bubble above his head shows {LONG} sailing fast through waves, cinematic.",
    27: "{LONG} cuts fast through blue waves seen from the front at a low angle, rows of rowers, speed lines and white foam.",
    28: "{C} looks at the viewer with an awkward smile at a wooden pier where {KNARR} floats with a cow looking out of it.",
    29: "{CARD}{KNARR} drawn small, with one green check mark and the hand-lettered black capital word \"CARGO\" under it.",
    30: "{KNARR} seen from the side on calm water, sacks and barrels and a cow on the deck, wide shot.",
    31: "A big museum hall with the old wooden pieces of a ship laid out on a metal frame, a stick figure curator with glasses pointing at them.",
    32: "A shipyard by the water where stick figure builders in aprons hammer a new wooden ship, wood shavings on the ground, a half-built hull on stands.",
    33: "{CARD}a side view of {KNARR} with a hand-drawn wooden ruler along it, the hand-lettered black numbers \"50 FT\" along the length and \"16 FT\" across the width.",
    34: "A wide wooden ship seen from the side with one big square striped sail and only four small oars sticking out, {C} counting on his fingers with a skeptical face.",
    35: "{C} pushes a wooden ship away from a wooden pier with one long oar, a few seagulls watching, calm water.",
    36: "A view from above of an open wide wooden ship packed with stick figure people sitting shoulder to shoulder with bundles, grandmother and children, tight and cheerful.",
    37: "A cow standing on the deck of {KNARR} among barrels with a worried face, a stick figure holding its rope, waves behind.",
    38: "{CARD}three icons in a row, a bed, a wall and a roof, each with a thick red X over it.",
    39: "{C} and {W} and {K} sit wrapped in wool blankets on an open ship deck under a grey sky, with a cow wearing a tiny cloak beside them, like a camping trip.",
    40: "A cutaway close-up of a ship side with overlapping wooden planks nailed together with iron nails drawn as big dots, a stick figure hammering in a nail.",
    41: "{C} pats the wooden side of the ship with a nervous smile and a bead of sweat, looking down at the hull.",
    # 3. O barco de guerra
    42: "{LONG} sails across the frame in full sun, stick figure rowers pulling together, bright blue sea, proud pose.",
    43: "A replica of {LONG} floats at a wooden dock, a stick figure museum guide with glasses points at it proudly, blue sky.",
    44: "A fjord with old wooden planks lying under clear shallow water, oak trees on the shore, a stick figure archaeologist in a hat pointing at a plank.",
    45: "{CARD}a long narrow ship drawn from above with many small oars along both sides, the hand-lettered black capital words \"60 OARS\" on top.",
    46: "{CARD}small stick figure sailors in rows inside a long ship outline seen from above, the hand-lettered black number \"65\" in big digits and the word \"CREW\".",
    47: "A small support boat pulls {LONG} with a long rope across a calm grey sea, the sail hanging limp, sailors waiting with folded arms.",
    48: "A stick figure sailor on the deck of {LONG} holds a long rope with an embarrassed smile and a tiny sweat drop, a small boat pulling in the distance.",
    49: "A big hall with a long dark wooden ship resting on a stand, tiny stick figures beside it looking up, soft light.",
    50: "A replica of {LONG} sails on a wide grey ocean with stick figure sailors in wool hoods and woolen caps, an empty horizon.",
    51: "{CARD}a round speedometer dial with a needle pointing to the right and the hand-lettered black words \"10 KNOTS\".",
    52: "{CARD}a round road speed sign with the hand-lettered black number \"12\" in the middle, plain white background.",
    53: "{CARD}a calendar grid with four rows crossed off and the hand-lettered black words \"4 WEEKS\".",
    54: "{LONG} glides up a narrow river between green banks over shallow water, birds flying above, stick figure rowers, sunny.",
    55: "{C} and {W} and {K} carry bundles and sacks down a gangplank onto a green coast, a cow following behind, moving house.",
    # 4. Sem bússola
    56: "{C} stands on the deck of {KNARR} in the middle of a round empty horizon of blue sea with a hand over his eyes, wide shot.",
    57: "{CARD}three icons each crossed out by a red X: a round compass, a rolled map and a phone with a map pin, the hand-lettered black capital words \"NO COMPASS\".",
    58: "Two stick figure sailors whisper into each other's ears on a wooden dock next to {KNARR}, an old one with a grey beard and a hooded blue cloak, speech bubbles with wavy lines and tiny arrows.",
    59: "An old thick book with a wooden cover open on a table, a quill beside it, wavy sea lines and a tiny ship drawn on the page, candlelight.",
    60: "{KNARR} sails to the left under a big setting sun with a large arrow drawn over the sea pointing left, the hand-lettered black capital word \"WEST\" on the arrow.",
    61: "A group of small green hilly islands far on the horizon seen from a ship deck, a stick figure pointing at them, clear sky, sparkly sea.",
    62: "Low hills of an island with only the top halves visible above the sea line, a stick figure on a deck pointing at them.",
    63: "A big whale tail and flying seabirds above the waves, {C} stands on the open deck of {KNARR} pointing up happily at the birds, a green coast far away.",
    64: "A smiling whale and a seagull each holding a tiny blue arrow sign, {C} on his ship looking down at them with raised eyebrows.",
    65: "{CARD}four sun icons in a row with small moons between them and the hand-lettered black words \"4 DAYS\".",
    66: "{KNARR} sails along a straight dashed line drawn across the sea toward the setting sun, small in the frame, simple clean composition.",
    67: "A thick uniform grey cloud blanket covers the whole sky above {KNARR} on dark water, {C} on its open deck looking up with a worried frown.",
    68: "{SH} hold up a clear glassy crystal toward the sky with a hopeful face, little sparkle lines inside the crystal.",
    69: "{CARD}a clear crystal with a thin beam of light going through it and a small sun above, the hand-lettered black number \"2011\" in the corner.",
    70: "{CARD}a magnifying glass over an empty wooden ship deck, the hand-lettered black capital words \"NONE FOUND\".",
    71: "{C} shrugs with raised eyebrows and open hands, a big question mark above his head, plain cream background.",
    72: "{KNARR} in thick white fog with only the top of the red-and-cream sail visible, {B} at the long wooden steering paddle at the back with a confused face, grey sea.",
    73: "{B} on the deck looks through thin fog at a dark forested low coast with surprised wide eyes, tall green pines on a flat shore.",
    74: "{CARD}a ship sailing on blue waves toward a small green island, a big arrow pointing right and the hand-lettered black capital word \"AMERICA\" with a question mark.",
    75: "{C} gives a tired thumbs up while holding the long wooden steering paddle at the back of {KNARR} under a darkening sky, a small cloud above his head.",
    # 5. Comida, sono e enjoo
    76: "{C} sits on a ship deck eating porridge from a wooden bowl with a wooden spoon, a few dried fish hanging on a rope above him, grey sea.",
    77: "{CARD}a roasted drumstick with a big red X over it, plain white background.",
    78: "A wooden barrel on a ship deck with a stick figure drinking water from a wooden ladle, a water drop falling, bright light.",
    79: "A stick figure chieftain with a gold arm ring and a thick cloak raises a foaming wooden mug on the deck of a long warship, the sailors behind him holding wooden ladles of water.",
    80: "{S}Left side: a modern stick figure cook in a yellow raincoat at a small camp stove on a replica ship. Right side: an old-time stick figure cook sitting sadly on the deck beside an empty iron pot.",
    81: "{CARD}three icons in a row: a bowl of porridge, a dried fish and a water drop, the hand-lettered black capital words \"EVERY DAY\".",
    82: "{C} looks around the open wooden deck of {KNARR} with his hands on his hips searching for a place to sleep, wool bundles, children and a cow everywhere, no cabin.",
    83: "{C} lies wrapped in a grey wool cloak on the bare deck between sacks with closed eyes, a small \"Z z z\" above him, stars and a moon in the sky.",
    84: "A view from above of an open ship at dusk with stick figure sailors asleep in rows pressed together under blankets, moonlight.",
    85: "Heavy rain falling in diagonal lines on a ship deck, stick figure sailors hunched under their hoods, grey sky and a cloud with \"brr\" lines.",
    86: "A close-up of a cold wet stick figure sailor with blue lips and shivering lines, rain dripping from his hood, a thought bubble with a small bed and a house.",
    87: "{C} shelters {K} under his wool cloak on the deck in the rain, the kids peeking out, a tender mood.",
    88: "Several stick figure sailors with green faces lean over the rail of a wooden ship, wobbly lines from their mouths, choppy waves.",
    89: "{CARD}ten small stick figure faces in two rows, eight of them green and two normal, the hand-lettered black words \"8 IN 10\".",
    90: "A cheerful stick figure sailor with a green face gives a weak thumbs up while holding the side of the ship, a sweat drop.",
    # 6. Quatorze de vinte e cinco
    91: "A shiny travel brochure with a picture of a sunny green hill and tiny stick figures, {C} reading it with a raised eyebrow, the bottom of the page curling over.",
    92: "{CARD}a row of 25 tiny ship icons, 14 of them green and 11 faded grey, the hand-lettered black words \"14 OF 25\".",
    93: "A wide empty grey sea with a lone wooden barrel floating on it and a big question mark made of waves above.",
    94: "{S}Left side: {KNARR} turning back toward a green coast with sailors waving. Right side: scattered wooden planks floating on dark waves.",
    95: "{KNARR} very small in the middle of an enormous ocean under a darkening sky, wide shot from far above.",
    96: "Two copies of {KNARR} far apart on a wide grey sea, tiny sailors on one waving their arms toward the other, which has a torn flapping sail.",
    97: "A row of fourteen ships sails in a line over a calm sunny sea, one with {C} waving from the deck.",
    98: "A coastline with floating white icebergs, tall snowy mountains and green slopes by the water, sailors pointing excitedly from the open deck of {KNARR}, morning light.",
    99: "{C} and {W} and {K} step off a gangplank onto a green shore of a fjord with icebergs, arms wide, a cow behind them, golden light.",
    # 7. Groenlândia
    100: "A big turf-roofed longhouse with a green roof on a steep hillside above a fjord, {E} stands in front of it, smoke rising, cows grazing.",
    101: "{CARD}many tiny turf-roofed houses in a big cluster, the hand-lettered black number \"500\" below them.",
    102: "{CARD}a small cluster of tiny turf-roofed houses, the hand-lettered black number \"90\" below them.",
    103: "Sheep, goats and a cow graze on a short-grass hillside beside a turf farm, a snow line on the mountains behind, a cold wind swirl.",
    104: "A farm in deep winter with snow piled on the turf roof, a stick figure family looks out of a tiny window, pale blue light and frost patterns.",
    105: "A stick figure with flushed cheeks lies in a wooden box bed under a wool blanket with a wet cloth on the forehead, a candle, a worried family around the bed.",
    106: "{C} looks around a wide snowy fjord with a hand over his eyes, a single small farm far in the distance, a tiny question mark above him.",
    107: "{C} sits on a rock above the fjord with his chin in his hand, thinking, a question mark above him, grey sky.",
    108: "{CARD}a walrus head with two long white tusks, the hand-lettered black capital word \"IVORY\" below it.",
    109: "A pile of long white walrus tusks stacked beside a Greenland shore, stick figures loading them onto a ship, a walrus watching from the ice.",
    110: "A stick figure bishop in a tall pointed hat holding a curved staff stands at the door of a small stone church above a fjord, a pile of tusks on the grass beside him.",
    111: "{C} stands proudly on a hill above a small beach with several wooden ships with square striped sails, hands on hips.",
    112: "{C} wears a tidy apron and hands a long white tusk to a merchant in a fine hat across a wooden counter, coins on the table.",
    # 8. Mercadores
    113: "{CARD}the hand-lettered black capital word \"MYTH\" in big letters with a small round iron helmet icon and a question mark.",
    114: "A thought bubble above {C} shows a tiny ship landing on a beach next to a stone church, stick figures with round iron helmets stepping off, a church bell.",
    115: "A small stone monastery on a green island surrounded by waves, a wooden ship with a square striped sail approaching on the sea, a monk stick figure on a path looking surprised, sunrise.",
    116: "{CARD}a calendar page with the hand-lettered black number \"793\" and a small ship icon.",
    117: "{CARD}a speech bubble with the hand-lettered black capital words \"GO VIKING\" next to a small ship, plain white background.",
    118: "Three small scenes around one green hill: a farmer plowing a field with an ox, a fisherman with a net, and a craftsman carving wood, bright colors.",
    119: "{IBN} stands on the muddy bank of a wide river looking at {RUS} who stand beside wooden boats pulled up on the shore, overcast sky.",
    120: "{RUS} stand tall in a line with hands on their belts, tiny palm trees drawn beside them as a comparison, {IBN} taking notes.",
    121: "{IBN} holds his nose with a disgusted face and turns his head away, wavy smell lines, plain cream background.",
    122: "A stick figure girl in a plain dress carries a wooden basin between seated men in a wooden hall, the men in rows, gentle mood.",
    123: "A stick figure man washes his face in a wooden basin with water splashing while other men wait in a line behind him.",
    124: "{CARD}a wooden basin of murky brown water with wavy lines above it, the hand-lettered black capital word \"YUCK\".",
    125: "{CARD}a stack of brown furs next to a thick chain link, simple icons, plain white background.",
    126: "{IBN} looks down at his hands with a serious face, soft grey light, plain background.",
    127: "A pile of round silver coins on a table with {RUS} and a pair of balance scales.",
    128: "{CARD}a pile of round silver coins with a small shovel, the hand-lettered black capital word \"SILVER\".",
    129: "A round coin with a decorative pattern travels along a dotted line from a desert city with domes to a pine-tree island by the sea, a dotted arrow trail.",
    # 9. Vinlândia
    130: "{E} sits at the long table of his turf longhouse with {L} and a woman, a bowl of food, a fire in the center, smoke rising through a hole in the roof.",
    131: "{L} stands at the front of a ship sailing across the sea toward a rocky Norwegian coast with tall mountains, one hand on the front post, sunrise.",
    132: "A king in a long red robe and a gold crown sits on a carved wooden chair handing a small wooden cross to {L} in a stone hall.",
    133: "A large outdoor assembly on a green plain with many stick figures in cloaks raising their hands, a man on a rock speaking, mountains behind, blue sky.",
    134: "{L} stands on a hill by a fjord pointing west over the sea, a thought bubble with a fog-covered forest coast, a determined face.",
    135: "{E} falls off a small horse on a dirt path leading down to a sandy beach, arms flailing and stars circling his head, {L} rushing to help.",
    136: "{E} sits on the ground rubbing his head while {L} stands beside him, a wooden ship with a square striped sail waiting at the shore behind them, a thought bubble with a stop sign.",
    137: "{E} walks slowly back up a hill toward his turf longhouse, his horse trotting after him, {L} and the ship small in the distance, gentle sunset.",
    138: "{L} and about thirty-five stick figure sailors in rows on the deck of a ship wave at the viewer, filling the frame, dawn.",
    139: "A sunny green shore with tall golden grass and grapevines hanging over bushes, {L} and sailors picking grapes, bright warm colors.",
    140: "{CARD}a row of sixty tiny blue stick figures and five tiny pink ones, the hand-lettered black words \"60 + 5\".",
    141: "A friendly trade on a beach: stick figures in wool tunics hold a bold red cloth, stick figures in leather and fur clothing hold stacks of grey furs, a pile of goods in the middle.",
    142: "{CARD}three snowflake icons in a row and a small wooden boat with one square sail, the hand-lettered black capital words \"3 WINTERS\".",
    143: "A dark storm cloud over a quiet village of turf houses on a beach, stick figure settlers looking over their shoulders at the dark forest edge with worried faces.",
    144: "A wooden chest in a dusty library with the lid half open and a question mark floating up, a stick figure historian with glasses scratching his head.",
    145: "A stick figure explorer in a woolen sweater and a stick figure woman archaeologist with a trowel and a hat stand on a windy grassy headland, pointing at the ground, rocky coast.",
    146: "A cutaway view of low grass-covered mounds in a green field with outlines of wooden-framed walls below ground: a forge with an anvil, a woodworking bench and a small boat with rivets, a tiny stick figure archaeologist beside it.",
    147: "A stick figure scientist in a lab coat holds a thick slice of tree trunk with rings in one hand and a magnifying glass in the other, a sun with big flares in the sky above.",
    148: "{CARD}a slice of tree trunk with rings and a clean ax cut on its edge, the hand-lettered black number \"1021\".",
    149: "{CARD}a big green check mark on a calendar page with the hand-lettered black capital words \"FIRST PROOF\".",
    150: "Three brown oval nuts on a wooden plate and a stick figure archaeologist scratching his head over them.",
    151: "{CARD}a green tree icon and an arrow pointing south from a small island to a larger land, the hand-lettered black capital words \"FARTHER SOUTH\".",
    # 10. Mitos
    152: "{CARD}a broom sweeping away three small icons, the hand-lettered black capital word \"MYTHS\" at the top.",
    153: "{CARD}a round helmet with two big curved horns and a bold red X across it, the hand-lettered black capital words \"MYTH 1\".",
    154: "A stage in an opera house with red curtains, stick figure singers in dramatic costumes and horned helmets, a stick figure costume designer with a sketchbook smiling in the corner.",
    155: "{HELM} on a small wooden stand in a museum glass case, a stick figure visitor looking at it closely, soft light.",
    156: "An old green bronze helmet with two curved horns on a museum stand, a stick figure curator with glasses pointing at a long hand-drawn timeline behind it.",
    157: "{CARD}a drinking horn with a green check mark and a skull cup with a red X, the hand-lettered black capital words \"MYTH 2\".",
    158: "A stick figure scholar in a dark coat with a ruff collar and a quill squints at an old page at a desk, a thought bubble where a tiny drinking horn turns into a skull.",
    159: "{CARD}a smiling stick figure with a big thought bubble full of question marks, the hand-lettered black capital words \"MYTH 3\".",
    160: "A framed old book illustration of a bearded old man with one eye shut, a wide-brimmed hat and two ravens on his shoulders, a spear in hand, simple frame.",
    161: "A stick figure scribe in a brown robe writes with a quill on parchment at a wooden desk in a turf room, a candle, a stack of books.",
    162: "{CARD}a long timeline bar with a bracket over it, the hand-lettered black numbers \"985\" at one end and \"1220\" at the other.",
    163: "{C} holds a magnifying glass up to a stack of old books with a skeptical raised eyebrow, a small question mark above him.",
    # 11. Fechamento
    164: "{C} sits quietly at the rail of {KNARR} gliding on calm blue water at sunset, looking ahead, peaceful.",
    165: "{C} and {W} and {K} eat porridge on a ship deck with a cow behind them and sacks piled around, the sea behind, warm light.",
    166: "{C} plants a small seedling in the green soil of a hillside farm, {W} and a cow behind him, calm morning light.",
    167: "{C} looks at the viewer with raised eyebrows and a small smile, plain cream background.",
    168: "A few small grey swords on a rack on the left while a big glowing golden ship takes the center with sparkles around it, the ship far bigger than the swords.",
    169: "{CARD}three icons in a row, a wave, a river between two banks and a beach, each with a small ship, the hand-lettered black capital words \"SEA RIVER BEACH\".",
    170: "{CARD}four little icons joined by curved arrows: a cow farm, a white tusk, a brown fur and a round blank silver coin with a small cross stamped on it, tiny wooden boats with square sails on the arrows.",
    171: "{CARD}a network of dots connected by lines with small ship icons on the lines, the hand-lettered black capital word \"NETWORK\".",
    172: "A fragile chain of tiny ships linked by thin lines with one link starting to crack, tense grey tone.",
    173: "A falling bar chart drawn on a wooden board with tall white tusks getting smaller from left to right, a sad walrus beside it.",
    174: "{CARD}a white tusk with a red X beside the hand-lettered black number \"1327\".",
    175: "A grass-grown ruin of turf walls and an empty stone church doorway beside a quiet fjord, wind blowing the grass, grey gloom.",
    176: "{CARD}a long timeline bar with five small markers and the hand-lettered black capital words \"500 YEARS\".",
    177: "{E} grins with a mischievous smirk holding a rolled scroll, sparkle lines and a tiny iceberg beside him, plain cream background.",
    178: "{CARD}a speech bubble with the hand-lettered black capital words \"WHICH JOURNEY NEXT?\" and a small ship with a question mark, plus a small bell doodle.",
}


def prompt(n: int) -> str:
    t = P[n]
    for k, v in T.items():
        t = t.replace("{" + k + "}", v)
    t = t[0].upper() + t[1:]
    return f"{BASE} {BONECO} {t}" if "stick figure" in t else f"{BASE} {t}"


def cartao(n: int) -> bool:
    return P[n].startswith("{CARD}")
