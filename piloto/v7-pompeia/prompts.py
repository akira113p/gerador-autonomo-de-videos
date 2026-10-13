"""Prompts de imagem do vídeo 7 (Pompeia, o último dia) para o Z-Image local, um por linha numerada do roteiro.md.

prompt() põe o estilo (BASE) e, se a cena tem stick figure, a descrição do boneco (BONECO).
{CARD} = cartão de fundo branco (palavras curtas, conferir a grafia).
Sem corpos, sem moldes de gesso desenhados, sem sofrimento explícito: o vulcão e a nuvem aparecem de longe.
Época: Pompeia, 79 d.C. Estação neutra (a data é disputada): sem roupa pesada nem fruta de outono nas cenas.
Objeto de época descrito pela forma, não pelo nome (moinho, pedras de passagem, jarra de garum, toldo).
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
    "C": "the stick figure baker Felix in his thirties with short messy dark curly hair, a short undyed cream wool tunic dusted with white flour, "
         "a rope belt and leather sandals",
    "PY": "the stick figure teenager Pliny the Younger, eighteen years old, with short brown hair and a plain white tunic",
    "PE": "the stick figure Pliny the Elder, a heavyset older man with grey hair, a white tunic and a dark red cloak",
    "M": "a stick figure woman in a long pale green dress with her hair tied up (Pliny's mother)",
    "TAC": "a stick figure historian with grey hair in a dark red toga",
    "BOY": "a tiny stick figure boy of six in a small white toga with a proud serious face",
    "CARD": CARTAO,
    "S": "Split screen divided by a vertical black dashed line. ",
}

P = {
    # 0. Abertura
    1: "{C} stretches and yawns beside a narrow window at dawn in a small plain room, through the window a green mountain with a flat top glows in soft pink light.",
    2: "{C} walks down a quiet street of a small Roman town at dawn with his hands behind his back, long shadows, orange tiled roofs, a big green mountain far behind the roofs painted in calm blue.",
    3: "{C} stands on a flat rooftop looking over a busy small Roman town with orange terracotta roofs and white and ochre walls, the blue bay with small wooden boats with square sails beyond, morning light.",
    4: "{CARD}a crowd of tiny stick figures filling a circle, the hand-lettered black capital words \"10,000 TO 20,000\" under it.",
    5: "{C} holds a small leather coin purse and a long paper list that reaches the floor, a broken iron chain lying on the ground beside him, proud smile, plain cream background.",
    6: "{CARD}four small hand-drawn icons in a row: a sack of flour, a coin with a small frown, a raised hand voting, and a gladiator helmet, the hand-lettered words \"TO DO\" above.",
    7: "{CARD}a small smoking mountain with a thick red X over it, the hand-lettered black capital words \"RUN AWAY?\" below.",
    8: "A calm green mountain covered with rows of grapevines up to a flat top, blue sky with a few small white clouds, a small farmhouse and a stick figure farmer waving.",
    9: "A stick figure Greek geographer in a long white robe holds a scroll and squints at a grey mountain top with dark pitted rocks, a thought bubble above him with a tiny flame fading into a wisp of smoke.",
    10: "{C} points with a big smile at the viewer like a tour guide, small Roman houses behind him, plain pale yellow sky.",
    11: "{PY} sits at a wooden desk writing on a roll of papyrus with a reed pen, a small oil lamp beside him and a window with a calm bay behind him.",
    12: "{CARD}the black capital word \"POMPEII\" with a thick red X drawn through it, a small quill pen beside it.",
    13: "{C} walks along a long wall completely covered with painted red lines and black scribbles, reading it with a curious face and his head tilted.",
    14: "{CARD}a big hand-lettered question mark and the words \"WHICH DAY?\" beside a sun icon and a moon icon.",
    # 1. Que dia é hoje?
    15: "{CARD}the hand-lettered black capital words \"AUGUST 24\" and \"79 AD\" in the middle with a small sun doodle.",
    16: "{PY} hands a sealed rolled scroll to {TAC} in a sunny courtyard, both smiling.",
    17: "A stick figure monk in a brown hooded robe copies a scroll by hand with a quill at a slanted wooden desk, a small candle, a shelf behind him with a gap where one scroll is missing.",
    18: "{CARD}three old parchment pages side by side, two of them with the hand-lettered word \"AUGUST\" and one with a question mark.",
    19: "A stick figure archaeologist in a sun hat kneels in front of a half-dug room with a small brush, a small excited sparkle above him, bright sunshine.",
    20: "A wall of rough white plaster with a rough black charcoal scribble on it, wooden poles of scaffolding, a pile of building stones and a bucket nearby, a stick figure holding a piece of charcoal.",
    21: "{CARD}the hand-lettered black capital words \"OCT 17\" with a small charcoal stick drawn beside them.",
    22: "A stick figure thumb smudges a black charcoal line on a white plaster wall, grey dust floating, close-up cartoon view.",
    23: "{CARD}a pomegranate and a chestnut with small leaf doodles, the hand-lettered word \"AUTUMN\" above.",
    24: "A stick figure scientist in a white coat with a clipboard stands next to a plaster wall holding a magnifying glass, thoughtful face, plain cream background.",
    25: "A stick figure archaeologist writes with a charcoal stick on a plaster wall, a small camera on a tripod beside him, sunshine.",
    26: "{CARD}ten small squares in a row each with a tiny charcoal line, the hand-lettered words \"10 MONTHS LATER\" and a green check mark.",
    27: "{CARD}a single charcoal scribble on a wall with two arrows pointing at it, the left one labeled \"OCT 78\" and the right one labeled \"OCT 79\", a question mark in the middle.",
    28: "{CARD}a pomegranate beside a small clay jar, the hand-lettered word \"STORED?\" above.",
    29: "A stick figure scholar in a neat jacket and glasses stands in a sunny excavated Roman street, holds up one finger, and shrugs with a small smile.",
    30: "{CARD}the hand-lettered black capital words \"PROBABLY AUGUST\" with a small question mark.",
    31: "{PY} smiles with a thumbs up next to a neat stack of scrolls, plain pale yellow background.",
    32: "{C} rolls up his sleeves with a grin, holding a big wooden bread paddle, a brick oven with an orange glow behind him.",
    # 2. Antes do amanhecer
    33: "{C} walks through a dark quiet Roman street before dawn carrying a small oil lamp, deep blue sky with a few stars, sleeping houses.",
    34: "{CARD}a loaf of bread icon next to the hand-lettered black number \"31\" and the word \"BAKERIES\" beneath.",
    35: "Inside a small Roman bakery: a round brick oven with an arched mouth glowing orange, a wooden counter and shelves with round loaves, {C} in front of it.",
    36: "A big stone grain mill made of two stone cones stacked tip to tip with a wooden beam through it, flour pouring from it into a basket, warm lamplight.",
    37: "{S}Left side: a grey donkey pushes the wooden beam of a stone grain mill. Right side: a tired stick figure worker pushes the same wooden beam.",
    38: "{CARD}the hand-lettered black number \"2023\" with a small shovel, a brush and a tiny brick oven.",
    39: "A small stone room with thick walls and tiny high windows with iron bars, light rays falling in, a grey donkey and two tired stick figure workers around a stone mill, dim muted colors.",
    40: "{C} stands thoughtful and looks at a small iron chain link in his hand, soft light from a window, quiet mood.",
    41: "{C} proudly slides a round golden loaf out of a brick oven with a long wooden paddle, warm light, steam.",
    42: "{CARD}a big round loaf of bread seen from above with eight wedge-shaped cuts radiating from the center.",
    43: "A round brick oven with its mouth open, rows of round black charcoal loaves inside, a small sparkle above them, drawn like a museum find.",
    44: "A stick figure baker presses a small bronze stamp into a round raw loaf on a floury table, flour dust in the air.",
    45: "{CARD}a dark round bread loaf with a small stamped rectangle on top and the hand-lettered word \"CELER\" above it.",
    46: "A round loaf of bread on a table with a tiny name tag tied to it with string, {C} winking beside it.",
    47: "{CARD}a big hand-drawn question mark above a flat round bread, the single hand-lettered word \"PIZZA?\" below.",
    48: "A painting on a red plaster wall showing a flat round bread, a cup of wine and a few fruits on a small table, a thin black frame around it.",
    49: "{CARD}a bold headline banner with the hand-lettered word \"PIZZA!\" and a surprised pizza slice doodle.",
    50: "A stick figure museum director shakes his head with a small smile and wags a finger at a painting of a flat bread on an easel, plain cream background.",
    51: "{CARD}a tomato and a block of cheese, each with a thick red X over it.",
    # 3. Manhã
    52: "{C} opens wooden shutters of a shop at sunrise and steps outside with his arms stretched, warm light, a shop counter behind him.",
    53: "A busy narrow Roman street at morning with stick figures carrying baskets, a donkey with bags on its back, a small cart, shopfronts with counters, orange roofs, warm light.",
    54: "A paved Roman street after heavy rain with brown puddles and a small stream of dirty water with straw, a stick figure with muddy sandals stepping carefully with a disgusted face, grey sky.",
    55: "A paved Roman street with three big flat-topped stone blocks set in a row across it, cart wheel ruts between them, side view, sunlight.",
    56: "{C} hops from one big flat stone block to another across a street with a grin, a small cart with big wooden wheels rolling between the blocks.",
    57: "A small stone street fountain on a corner with a square basin and a carved spout, stick figures lining up with clay jars, morning light.",
    58: "A tall stone aqueduct with arches carrying a water channel across green hills toward a Roman town in the distance, blue sky.",
    59: "{C} tilts his head back and looks up at a long white plaster wall covered with red painted letters and black scribbles, small curious sparkles.",
    60: "{CARD}a white wall with many lines of red painted writing, the hand-lettered number \"2,600\" in large clear digits above it, a small red paintbrush.",
    61: "{CARD}on the left a market stall with a street broom, on the right a stern official in a white toga, a plus sign between them.",
    62: "A small group of stick figures in long white robes raise their arms to support a stick figure candidate in a bright white toga, a red painted wall behind them.",
    63: "A line of stick figure men in white togas raise one hand to vote in a town square, while a stick figure woman and a stick figure worker watch from behind a rope with crossed arms.",
    64: "{C} leans toward a wall full of scribbles with a smirk, a small speech bubble with wavy lines above his head.",
    65: "A stick figure leans on a plaster wall and scribbles with a piece of charcoal while another stick figure watches, the wall completely filled with drawings and scribbles.",
    66: "{CARD}a cracked plaster wall covered with scribbles and a small speech bubble above it with the hand-lettered words \"I ADMIRE YOU, WALL\".",
    67: "A group of cheerful stick figures raise clay cups at a street bar under a lantern, one of them holding up a painted red notice.",
    68: "{CARD}a plaster wall full of small speech bubbles, heart doodles and a thumbs-up, the single hand-lettered word \"COMMENTS\" at the top.",
    # 4. Meio da manhã
    69: "{C} carries a flat basket of round loaves through the open door of a big Roman house, bright sun, a doorman waiting.",
    70: "Inside a Roman house: a bright open hall with a square pool in the floor under an opening in the roof, walls painted bright red with golden decorations, a garden with columns beyond, a proud stick figure owner in a white toga.",
    71: "{C} peers curiously at a proud stick figure owner in a white toga, a small thought bubble with a tiny iron chain link above the owner's head.",
    72: "A grand Roman house entrance with red painted walls and a mosaic floor, two stick figures in rich tunics shaking hands proudly in the doorway, gold coins around them.",
    73: "Rows of grapevines on a sunny hillside with big clay wine jars in front, a stick figure winemaker treading grapes in a wooden tub, purple juice.",
    74: "A stick figure in a plain tunic looks up at a tall carved stone chair of a magistrate with a thick red X over it, plain cream background.",
    75: "{C} scratches his head with a coin purse in one hand and a puzzled question mark above him, plain cream background.",
    76: "A small side door in a big stone wall is slightly open with warm golden light spilling out, a stick figure peeks in with a sly smile.",
    77: "A Roman street with cracked walls, fallen stone blocks and tilted columns, stick figures running with surprised faces, dust clouds, drawn as a memory in faded colors.",
    78: "A Roman street with wooden scaffolding poles against a half-repaired wall, stick figure workers carrying bricks on their shoulders next to a pile of stones, sunny.",
    79: "A small temple with columns and a front staircase, one corner of it broken and held up with wooden poles, stick figure workers around it.",
    80: "A stick figure freedman in a clean white tunic hands a heavy bag of coins to a stick figure builder in front of a half-rebuilt temple, a small boy beside him.",
    81: "A group of stick figure men in white togas sit on a curved stone bench and raise their hands to welcome a tiny child in a small white toga who stands in the middle, warm light.",
    82: "{CARD}the hand-lettered black capital words \"AGE 6\" with a small boy icon with a big smile.",
    83: "{BOY} sits in a big stone chair far too large for him, feet dangling, a serious frown, council men clapping behind him.",
    84: "A stick figure banker behind a wooden table counting coins, a stack of wooden writing boards covered with wax and a stylus, a small iron strongbox.",
    85: "{CARD}a neat stack of small wooden writing tablets, the hand-lettered black number \"153\" in large clear digits and a small coin icon.",
    86: "A stick figure shakes hands over a table with a pile of coins, another stick figure holds a stack of writing tablets and a third points at a long list, lively market, warm light.",
    # 5. Meio-dia
    87: "{C} stands at a street corner at noon holding his tummy, a thought bubble with a bowl of food, bright midday sun and short shadows, hungry face.",
    88: "{CARD}a stone snack counter icon next to the hand-lettered black number \"80\" in large clear digits and a small bowl icon.",
    89: "A street food bar with an L-shaped stone counter with big round clay jars sunk into its top and steam rising, {C} leaning on it with a smile, a bartender stick figure ladling food.",
    90: "Archaeologists with brushes and small trowels clean an L-shaped stone counter inside a half-dug shop in the sun, a wheelbarrow, blue sky.",
    91: "A close-up of the front of a stone counter painted with two colorful ducks hanging upside down and a red rooster, bright flat colors.",
    92: "{CARD}a clay jar with small icons of a pig, a goat, a fish and a snail floating above it.",
    93: "{C} points at painted ducks on a counter with a thumbs up and an impressed face, a plate of food in his other hand.",
    94: "A painted dog on a leash on the side of a stone counter, drawn in simple flat colors with a cartoonish look.",
    95: "A small scratched scribble on the painted frame of a dog picture with a tiny angry face drawn on it, a stick figure with a nail grinning behind it.",
    96: "{C} and a bartender both chuckle, a lone angry stick figure shakes his fist in the corner.",
    97: "A big clay wine jar with crushed beans dropped into it by a stick figure and red wine swirling, a wine cup beside it.",
    98: "A tall clay jar with a pointed bottom and a tiny fish painted on its side, a ladle of brown sauce above it, steam, plain cream background.",
    99: "A tall clay jar with a pointed bottom and a tiny fish painted on it, a small crown above it, a stick figure merchant standing proudly next to it.",
    100: "{CARD}a bottle of ketchup with a fish tail sticking out of its top.",
    101: "{C} sits relaxed at a bar table with a bowl and a cup, chatting with friends, small speech bubbles with scribbles, midday light.",
    # 6. A arena
    102: "A group of stick figures chat excitedly on a street with their arms waving, one holding a small wooden practice sword, a painted gladiator helmet icon on the wall behind them.",
    103: "A painted wall poster of a gladiator with a round shield and a crested helmet in bold red and black, a crowd of stick figures cheering in front of it.",
    104: "{CARD}a gladiator helmet icon with hearts around it and the hand-lettered words \"THE GIRLS' IDOL\".",
    105: "{CARD}a red painted notice with a tiny gladiator helmet icon and a cloth awning icon, the hand-lettered words \"MAY 31\" in the middle.",
    106: "A big striped cloth canopy stretched over arena seats giving shade, stick figures fanning themselves underneath, sunny.",
    107: "A group of stick figure fans with painted faces and banners cheer loudly in a stone arena with their mouths wide open.",
    108: "Two groups of stick figures face each other across a gap in the stands of an oval stone arena, one group with green banners and one with orange banners, pointing and shouting, speech bubbles with scribbles.",
    109: "Stick figures throw small stones across the stands in a chaotic cartoon scuffle, lots of motion lines and dust clouds, banners flying.",
    110: "A group of stick figures with green banners raise their arms in triumph on the arena steps, the others with orange banners walk away slumped.",
    111: "A stern stick figure senator in a toga hands a sealed scroll to a messenger in a large hall with columns, a poster of an oval arena with a thick red X behind them.",
    112: "{CARD}a small stack of ten boxes with a loose lid and the hand-lettered words \"10 YEARS?\".",
    113: "A colorful wall painting of an oval arena seen from above with tiny crowds in the stands, drawn in a childlike flat style on a red wall, a stick figure admiring it with a snack.",
    # 7. A nuvem
    114: "A bright afternoon sky above the Bay of Naples with a small tall plume starting to rise from a distant green mountain, calm blue water in front, small boats.",
    115: "{M} stands on a stone terrace by the sea pointing up at a strange tall cloud in the sky with an astonished face, {PE} beside her.",
    116: "{PE} stands in his dark red cloak on a stone terrace with a scroll in one hand, a harbor with Roman galleys below him.",
    117: "{PE} walks up a grassy hill to a better viewpoint shielding his eyes with his hand and looking at a tall cloud.",
    118: "A tall tree with a thin bare brown trunk and a wide flat spreading green crown (an Italian umbrella pine) next to a tall grey cloud of exactly the same shape, plain cream background.",
    119: "A tall column of smoke rising from a mountain top, bright white in some patches and dark grey-brown in others with speckles, flat blue sky.",
    120: "{CARD}a tall column of smoke with a flat spreading top and a small scroll beside it, the hand-lettered words \"PLINY'S CLOUD\".",
    121: "{CARD}a tall column of smoke next to a vertical ruler, the hand-lettered words \"30 KM HIGH\" at the top.",
    122: "A small Roman town seen from a street with a huge column of grey smoke rising right behind the rooftops, a stick figure pointing at it small and stunned, flags blowing toward the town.",
    123: "{C} turns to the viewer with a hand on his chin and a thoughtful face, a small question mark above him, plain cream background.",
    124: "A small group of stick figures in a street stare up at the sky with hands shading their eyes, one shrugs, speech bubbles with scribbles.",
    125: "{CARD}a small phone, a bell and a loudspeaker each with a thick red X over it, the hand-lettered words \"NO ALARM\" above.",
    126: "Small white lumps of pumice stone fall like hail in a street, stick figures hold out their hands to catch them with curious faces, dim sky with grey streaks.",
    127: "{CARD}a single white porous stone full of little holes next to a feather, the hand-lettered word \"LIGHT\" above.",
    128: "{C} holds a white pumice stone in his palm and smiles, relaxed, while small white stones fall around him, dim light.",
    # 8. Chuva de pedra
    129: "A street in a Roman town under falling white pumice stones, a layer already on the rooftops, stick figures holding baskets over their heads, twilight.",
    130: "{CARD}a vertical ruler with a white pile of pumice growing step by step beside it, the hand-lettered words \"12-15 CM / HOUR\".",
    131: "A pile of white pumice stones covering three big flat stone blocks across a street until only their tops peek out, evening light.",
    132: "{CARD}a stick figure standing next to a tall white pile of pumice that reaches his chest, the hand-lettered words \"1.5 METERS\".",
    133: "A house with orange roof tiles sagging under a heap of white pumice, the roof beam bending, stick figures in the doorway looking up in worry, dusk.",
    134: "{S}Left side: a stick figure inside a house looks up at a sagging ceiling. Right side: a stick figure outside holds a pillow over his head while white stones fall around him.",
    135: "{PE} walks along a dark beach at dusk with a small group of stick figures, torches in their hands, white stones falling around them, the sea beside them.",
    136: "A group of stick figures walks along a path with pillows tied on their heads with white cloth napkins, carrying torches, white pumice falling around them, dark sky.",
    137: "A dark sky over a village at midday, a line of stick figures with burning torches walking, a faint line of bright daylight on the far horizon.",
    138: "A Roman galley with oars sails across a bay toward a smoking mountain, {PE} at the bow, ash falling on the deck.",
    139: "{PE} stands on the deck of a Roman galley with a raised finger, the helmsman points back, a smoking mountain ahead, ash falling.",
    140: "A calm empty beach at dawn with a folded sail on the sand, a neatly folded red cloak on it and a burnt-out torch, grey light.",
    141: "A crossroads where stick figures head in different directions, some carrying bundles, some standing at their doors, arrows pointing different ways.",
    142: "A line of stick figures carrying bundles on their heads along a road toward the sea, small wooden boats waiting at a beach, white flakes falling.",
    143: "{CARD}a stone plaque with scratched letters and the hand-lettered word \"POMPEII\" on it, a small green check mark beside it.",
    144: "A stick figure sits on a doorstep with his arms around his knees and an old oil lamp, a heavy bundle beside him, white stones falling in the street outside, dim light.",
    145: "{C} sits on a stool by the door of his bakery looking out at the street with a thoughtful face, a bundle and a lantern at his feet, muted colors.",
    # 9. A noite
    146: "A dark street at night lit only by a few torches and a red glow in the sky from a distant mountain, stick figures walking in the dark.",
    147: "{PY} sits in an open courtyard by the sea at night with a book in his lap, a red glow on the horizon across the bay.",
    148: "{CARD}a small oil lamp with a thin trail of smoke, the hand-lettered words \"LIGHTS OUT\" beside it.",
    149: "A crowd of stick figures huddled in the dark on a road with open mouths and raised arms, tiny speech bubbles with scribbles, torches, dim night colors.",
    150: "A group of stick figures raise their hands to a dark sky, one holds a small statue of a god, another turns away with empty hands, the sky full of dark clouds.",
    151: "{PY} sits calmly on a stone bench reading a scroll with a stylus and a wax tablet on his knee, dark ash flakes falling around him.",
    152: "A stick figure friend in a hooded traveler cloak wags a finger at {PY}, who keeps reading with a calm face, {M} beside him.",
    153: "{PY} gives a small smile and a thumbs up to the viewer with a scroll under his arm, plain cream background, a small speech bubble with three dots.",
    154: "A Roman street with cracks in the stones and wobbling houses, dust shaking from rooftops, motion lines, stick figures bracing themselves, dark sky.",
    155: "{CARD}a wavy ground line with small cracks and the hand-lettered words \"NORMAL HERE\".",
    156: "{C} looks up at the sky with a worried frown and a lantern, a faint exclamation mark in a thought bubble, ash falling.",
    157: "A far-away view of a mountain with a glowing red top and a grey cloud rolling down its side toward a coastal town, night sky, tiny buildings seen from a very long distance.",
    158: "{C} stands on a hill looking at a glowing mountain in the distance and a town on the coast, a small thought bubble with a question mark.",
    # 10. A manhã seguinte
    159: "A Roman street filled with white pumice up to the doorways at grey dawn, only the tops of the roofs visible, silent empty scene.",
    160: "A far-away silhouette of a town at dawn under a huge grey cloud with a pale streak of light on the horizon, very calm distant view.",
    161: "{CARD}a black marker lying on a plain white page with its cap beside it, the hand-lettered words \"WE STOP HERE\" above.",
    162: "{C} waves goodbye to the viewer with a gentle smile, plain cream background.",
    163: "{CARD}a single burning candle with the hand-lettered number \"1,300\" in clear digits.",
    164: "{CARD}a circle of ten identical small round dots with one dot colored dark grey, the hand-lettered words \"1 IN 10\".",
    165: "A long line of stick figures carrying bundles on their heads walk along a road at sunrise toward distant blue hills, soft light, a sad but hopeful mood.",
    166: "{CARD}a chunk of grey hardened ash with a small round hollow, a funnel and a bucket of white plaster beside it, the hand-lettered number \"1863\".",
    167: "{CARD}a plain white plaster jar inside a thin frame with small measuring marks, the hand-lettered word \"REWORKED\" above.",
    168: "{CARD}a single candle and a small white flower on a stone, the hand-lettered words \"WITH RESPECT\" below.",
    169: "{CARD}a smoking mountain with a lava stream crossed out by a thick red X, white stones and a grey ash cloud with a green check mark, the hand-lettered words \"NO LAVA\".",
    # 11. Depois
    170: "A green grassy hill with the tops of a few stone columns and orange roof tiles peeking out of the ground, sheep grazing, calm sunny landscape.",
    171: "A stick figure architect in a dark velvet hat and a long dark coat digs a deep narrow trench with workers and hits an old painted wall, then puts a finger to his lips.",
    172: "{CARD}a simple timeline with two marks \"1748\" and \"1763\", a small shovel on the first and a stone plaque with scratches on the second.",
    173: "{CARD}a square picture frame with a big crack through it, the hand-lettered words \"NOT A SNAPSHOT\".",
    174: "{CARD}three small icons in a row: a knocked-over stool, a bundle with an arrow, and an open empty chest.",
    175: "The upper floors of a ruined Roman house with a few stick figures cooking over a small fire in a room, planks and curtains, the ground floor filled with grey ash, warm firelight.",
    176: "A winding road from a ruined hilltop town leading toward a bright sunrise, small stick figures walking away and others walking back, hopeful colors.",
    177: "{C} walks happily down a sunny Roman street greeting neighbors, a basket of bread on his arm, cheerful bright colors.",
    178: "{CARD}five small hand-drawn icons in a row: a loaf of bread, a wine cup, a raised hand voting, a gladiator helmet, and a coin purse.",
    179: "A wall completely covered in scribbles, a stick figure on tiptoe writes one more scribble at the very top with charcoal, a small speech bubble with grumpy squiggles.",
    180: "A stick figure tourist with a hat and a camera reads scribbles on an old Roman wall with a magnifying glass, bright sun, curious smile.",
    181: "{C} wakes up in his room at dawn and stretches at the window, the green mountain glowing outside, a paper list in his hand reaching the floor.",
    182: "{C} sits at a table with a loaf of bread and an oil lamp, closing a thick scroll with a gentle smile, last warm light.",
    183: "{CARD}a speech bubble reading \"WHICH DAY NEXT?\", a small bell doodle and a big question mark.",
}


def prompt(n: int) -> str:
    t = P[n]
    for k, v in T.items():
        t = t.replace("{" + k + "}", v)
    t = t[0].upper() + t[1:]
    return f"{BASE} {BONECO} {t}" if "stick figure" in t else f"{BASE} {t}"


def cartao(n: int) -> bool:
    return P[n].startswith("{CARD}")
