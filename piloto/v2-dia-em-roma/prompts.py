"""Prompts de imagem do vídeo 2, um por linha numerada do roteiro.md (mesma numeração).

"SEM|" no início: cenário, cartão ou objeto, sem o bloco de personagem (senão o modelo põe um stickman).
Tokens {R}, {T}, {M}... são trocados pelas descrições fixas dos personagens abaixo.
Mapas falharam no teste de estilo e no 020 (Catânia nos Bálcãs): nenhum mapa por IA.
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

PERSONAGENS = {
    "R": "a stick figure Roman man with short messy black hair, wearing a short knee-length mustard-yellow wool tunic "
         "with a brown belt and brown sandals",
    "T": "a stick figure Roman man with short messy black hair, wearing a large white wool toga draped over a "
         "mustard-yellow tunic",
    "M": "a stick figure Roman poet with short curly grey hair and a small grey beard, wearing a white toga",
    "MOD": "a stick figure man wearing a blue t-shirt and grey trousers, short messy brown hair",
    "SEN": "a bald stick figure philosopher with a short grey beard, wearing a plain cream toga",
    "PLI": "a slim stick figure Roman gentleman with neat short brown hair, wearing a white toga",
    "JUV": "a stick figure satirist with short spiky grey hair and a sour frown, wearing a plain grey cloak",
    "PAT": "a plump stick figure rich Roman patron with neat grey hair, wearing a bright white toga",
    "IMP": "a stout cheerful stick figure Roman emperor with a golden laurel wreath and a purple cloak",
    "FOM": "a thin hungry stick figure man in a short patched brown tunic",
    "MES": "a stern bald stick figure Roman schoolmaster in a brown tunic",
}

S = "Split screen divided by a vertical black dashed line. "

# "dining couch" vira sofá moderno; descrever a forma do leito romano
PERSONAGENS["LEITO"] = (
    "a long narrow Roman dining bed of carved dark wood on tall turned legs, like a high daybed with a thin striped "
    "mattress and two round cushions at one end"
)
PERSONAGENS["MESA"] = "a small low round wooden table on three curved animal legs"
PERSONAGENS["LAMPADA"] = "a small flat oval clay oil lamp with a short spout and a tiny flame at the tip of the spout"
PERSONAGENS["CALENDARIO"] = (
    "a calendar painted in red and black on a white plastered wall: rows of small painted squares and Latin letters"
)

PERSONAGENS["SOL"] = (
    "a Roman sundial: a flat horizontal round stone slab on a short stone column, with a tall triangular bronze blade "
    "standing upright in its center that casts a dark shadow across carved straight lines radiating on the stone"
)

P = {
    # 0. Abertura
    1: "A modern bedroom at dawn: only one character, {MOD}, sits up sleepily alone in bed and reaches for a ringing alarm clock on the bedside "
       "table, small motion lines around the clock, pale blue morning light from the window.",
    2: "Close-up of {MOD} lying in bed holding a glowing smartphone that shows a calendar full of small colored boxes, "
       "worried raised eyebrows.",
    3: "SEM|" + CARTAO + "a hand-drawn weekly calendar grid filled with many small colored blocks, a coffee cup doodle "
       "and a round clock doodle showing twelve o'clock, the hand-lettered black capital words \"MEETINGS\" and "
       "\"DEADLINES\" with arrows pointing at the blocks.",
    4: "SEM|" + CARTAO + "a long horizontal hand-drawn black timeline arrow, a red map pin on the right end labeled "
       "\"TODAY\" with a small smartphone doodle, a red map pin on the left end labeled \"90 AD\" with a small Roman "
       "temple doodle, a curved black arrow looping back from right to left.",
    5: "SEM|Very simple wide panorama of ancient Rome with only a few big shapes: dense rows of terracotta-roofed "
       "apartment blocks and white temples on green hills, a big round stone arena in the middle distance, the river "
       "Tiber curving in the foreground, pale turquoise morning sky.",
    6: "SEM|" + CARTAO + "a round wall clock crossed out by a big thick red hand-drawn X, and next to it {SOL}, "
       "with a green check mark.",
    7: "{M} sits at a small wooden writing table in a simple plastered room, writing on a papyrus scroll with a reed "
       "pen, a clay ink pot beside him, sly smile.",
    8: "SEM|" + CARTAO + "an unrolled papyrus scroll with a few lines of black handwriting, and next to it a small "
       "hand-drawn sun doodle and the hand-lettered black capital words \"HOUR BY HOUR\".",
    9: "{R} stands at the entrance of a narrow sunny Roman street with terracotta-roofed buildings, waving at the "
       "viewer with a friendly smile.",
    10: "SEM|" + S + "Left side: a sunrise over the terracotta rooftops of ancient Rome. Right side: a deep navy blue "
        "starry night over the same rooftops with a crescent moon.",
    # 1. A hora romana
    11: "{R} stands on a plain cream background scratching his head, a big black question mark floating above him, "
        "{SOL} at his feet.",
    12: "SEM|" + CARTAO + "a big hand-drawn half circle like the path of the sun, from a small rising sun on the left to "
        "a small setting sun on the right, divided into twelve equal slices by thin black lines, the slices numbered "
        "1 to 12 in order from left to right in small black digits.",
    13: "SEM|" + CARTAO + "the number \"12\" in huge hand-lettered black digits in the center, a small blue snowflake "
        "doodle on the left and a small blazing yellow sun doodle on the right, each with a green check mark.",
    14: "SEM|" + CARTAO + "a long horizontal bar divided into twelve wide segments numbered 1 to 12 in small black digits, a big blazing yellow sun above it, "
        "the hand-lettered black words \"JUNE\" on the left and \"1 HOUR = 75 MIN\" underneath.",
    15: "SEM|" + CARTAO + "a short horizontal bar divided into twelve narrow segments numbered 1 to 12 in small black digits, a small pale sun and blue "
        "snowflakes above it, the hand-lettered black words \"DECEMBER\" on the left and \"1 HOUR = 45 MIN\" underneath.",
    16: S + "Left side: {R} eats bread slowly and happily under a bright summer sun. Right side: the same man, now "
        "wrapped in a brown wool cloak, gulps his bread in a hurry under a pale winter sky, a sweat drop.",
    17: "{R} stands in a sunny Roman square shading his eyes with one hand and looking up at the bright sun, a long "
        "shadow on the paving stones.",
    18: "{R} looks at {SOL} on a pedestal with a confused face, a big question mark above him.",
    19: "A small parade of stick figure Roman soldiers in red tunics and bronze helmets carry {SOL} on "
        "a wooden stretcher, a ship with one square sail on a blue sea behind them.",
    20: "SEM|" + S + "Left side: {SOL} under a sun high in the sky, the hand-lettered black capital word "
        "\"CATANIA\" and a small black arrow pointing down labeled \"SOUTH\". Right side: {SOL} under "
        "a lower sun, the hand-lettered black capital word \"ROME\" and a small black arrow pointing up labeled "
        "\"NORTH\". Plain white background.",
    21: "SEM|Close-up of {SOL}, the shadow falling between the carved lines, "
        "a big thick red hand-drawn X over the dial.",
    22: "A crowd of stick figure Romans in simple colored tunics stands in front of {SOL} in a sunny "
        "forum, all nodding and pointing at it with confidence, a hand-lettered black sign above them that reads "
        "\"99 YEARS\".",
    23: "{R} sits on a stone bench next to {SOL} with arms crossed and a grumpy face, a small grey storm cloud "
        "above his head.",
    24: "A simple open-air Roman theater stage with a painted wooden backdrop of house doors: {FOM} holds his empty "
        "belly with one hand and raises an angry fist at {SOL} standing on the stage.",
    25: "Close-up of {FOM} shaking both fists at the sky with furious eyebrows, {SOL} behind him broken into "
        "many small pieces by black crack lines.",
    26: "A small happy stick figure boy in a short brown tunic eats a big round loaf of bread and rubs his round belly, "
        "small hearts floating above him, a simple sunny courtyard.",
    27: S + "Left side: the small boy in a brown tunic happily eats bread under a smiling sun. Right side: {FOM} "
        "waits sadly next to {SOL} holding an empty clay bowl, a sweat drop.",
    28: "SEM|" + CARTAO + "the hand-lettered black number \"159 BC\" at the top, an ancient water clock: a tall clay jar on a wooden stand dripping water from a small hole at "
        "the bottom into a lower clay basin marked with lines, blue water drops, the hand-lettered black capital words "
        "\"WATER CLOCK\".",
    29: "{R} stands on a flat terracotta rooftop at dawn, looking up at the pink sky with one hand cupped behind his "
        "ear, the roofs of Rome around him.",
    30: "A busy narrow Roman street drawn in bold lines with many loud sound symbols: big jagged hand-lettered words "
        "\"BANG\" and \"CLANG\", a barking dog, a braying donkey, stick figure people shouting.",
    # 2. Acordar
    31: "Dim interior of a tiny rented room with plastered walls before sunrise: {R} wakes up on a straw mattress on a "
        "low wooden bed, yawning and stretching, a small window showing a dark blue sky.",
    32: "SEM|Very simple wide view of an ancient Roman apartment block of the first century: five floors of ochre and cream plastered walls with small square window openings with wooden shutters, a few wooden balconies, a terracotta tile roof, a row of small shops with wide arched openings on the ground floor, a cobbled street, the hand-lettered black word \"INSULA\" above it.",
    33: "SEM|Very simple drawing of a narrow ancient Roman cobbled street between two tall ochre and cream plastered apartment blocks with terracotta tile roofs, small square window openings with wooden shutters, wooden balconies, laundry hanging between them, cracks in the plaster, a clay amphora by a door.",
    34: "{IMP} stands next to a tall Roman apartment block and points at a vertical measuring line with tick marks, "
        "the hand-lettered black words \"70 FEET\" at the top of the line.",
    35: "A tall Roman apartment block leaning slightly to one side, propped up by several thin wooden poles, a nervous "
        "stick figure resident looks out of a window with a sweat drop.",
    36: "A Roman apartment block with orange flames and grey smoke coming out of the upper windows, stick figure "
        "residents run out of the door in panic, one carries a clay water jar.",
    37: "{R} lies in bed in his small dark room with wide-open eyes and both hands over his ears, jagged noise lines "
        "coming through the small window.",
    38: "SEM|" + CARTAO + "a heavy wooden Roman cart with two big wheels crossed out by a big thick red X, a big bright "
        "yellow sun next to it, the hand-lettered black capital words \"NOT BY DAY\".",
    39: "Night street scene with a navy blue sky and a crescent moon: heavy wooden carts pulled by oxen and loaded "
        "with stone blocks and clay amphorae roll through a narrow street between tall buildings, a stick figure "
        "driver cracks a whip, noise lines.",
    40: S + "Left side: a rich stick figure Roman sleeps peacefully in a big quiet bedroom with a garden outside. "
        "Right side: a poor stick figure Roman lies awake in a tiny room above a noisy street, dark circles under his "
        "eyes.",
    41: "A sick stick figure Roman lies on a simple wooden bed with a wet cloth on his forehead and dark tired circles under his eyes, staring at the ceiling; through a small window with open wooden shutters, wooden ox carts with big spoked wheels pass in the dark street, sound lines.",
    42: "{R} in his tiny room looks into an empty clay jug with a disappointed face, one single drop of water falling "
        "from it.",
    43: "{R} climbs a narrow wooden staircase carrying a heavy clay water jar on his shoulder, sweat drops, the stairs "
        "going up and up.",
    44: "SEM|" + CARTAO + "a simple round clay chamber pot on the left and, on the right, a long stone bench with three round holes in its top like an ancient Roman public latrine, the hand-lettered black capital word \"OR\" between them.",
    45: "{R} stands in his small room tightening his brown leather belt with both hands, satisfied smile.",
    46: "Only one character: {R} stands alone and holds up a huge folded white woolen toga with both arms, looking at it with doubt, a sweat drop, plain cream background.",
    47: "{R} is tangled up in a huge white wool toga wrapped messily around him, a small stick figure helper pulls at "
        "one end of the cloth, comic struggle lines.",
    48: "{T} steps out of a doorway into a narrow sunny Roman street full of stick figure people and a donkey.",
    49: "A dense crowd of stick figure Romans in colorful tunics packed into a narrow street, {T} squeezed in the "
        "middle with a squashed face, black arrows showing people pushing from the front and from behind.",
    50: "In a crowded street {T} gets an elbow in his side from one stick figure, while another stick figure carrying "
        "a long wooden beam on his shoulder bumps his head, little stars around his head, a clay wine amphora swinging "
        "nearby.",
    51: "Close-up at foot level: the mud-caked legs and sandals of a Roman man, and a Roman soldier's heavy studded "
        "leather boot stepping on his toe, a big jagged \"OUCH\" starburst.",
    52: "{T} walks past a public stone fountain on a street corner, water pouring from a carved lion head spout into a "
        "stone basin, two stick figure women fill clay jars.",
    53: "SEM|Very simple wide landscape: a long Roman aqueduct with tall stone arches crossing green countryside toward "
        "a city on the horizon, rolling hills behind, pale blue sky.",
    54: "A proud stick figure Roman official with short grey hair in a white toga stands in front of a big aqueduct "
        "arch with his chest out and one hand on his hip, holding a scroll of plans, small sparkles around him.",
    55: "SEM|" + S + "Left side: a tall Roman aqueduct with flowing water and a big green check mark. Right side: an "
        "Egyptian pyramid in the desert with a big red X.",
    56: "The proud stick figure Roman official with short grey hair in a white toga points at himself with his thumb "
        "and a smug smile, the aqueduct behind him.",
    # 3. Café da manhã e escola
    57: "SEM|" + CARTAO + "a round loaf of Roman bread scored into eight wedges, a wedge of white cheese, a small bowl "
        "of black olives and a small pile of salt, the hand-lettered black capital word \"BREAKFAST\".",
    58: "{R} buys a round loaf of bread at a bakery counter open to the street, the baker with flour on his apron hands "
        "it over, a big dome-shaped brick oven behind him.",
    59: "{M} sits on a stool and writes on a small wax tablet with a stylus, smiling, a rooster on the windowsill.",
    60: "Dawn street scene: a cheerful baker sells round loaves from his counter to three small stick figure boys in "
        "short tunics carrying wax tablets, roosters crow on a rooftop, pink sunrise sky.",
    61: "Three small stick figure boys in short tunics walk along a street at dawn carrying wax writing tablets, one of "
        "them yawning.",
    62: "Dark blue early morning sky with stars still visible: a small stick figure boy in a short tunic walks to "
        "school yawning hugely, holding a small clay oil lamp.",
    63: "{M} with messy hair leans out of an upper window with furious eyebrows, glaring down at the street below, a "
        "dark blue sky before dawn.",
    64: "{MES} shouts with his mouth wide open at a row of small boys on a bench, holding a long thin cane, jagged "
        "shout lines, a rooster asleep on a wall in the dark.",
    65: "An open-air classroom under a simple porch roof along a street: small stick figure boys sit on a bench with "
        "wax tablets, {MES} stands in front of them, passers-by walk past.",
    66: "Neighbors in a Roman street lean out of windows and doorways, some covering their ears and some laughing, "
        "while below a small boy reads aloud from a wax tablet, a red X next to his answer.",
    # 4. Salutatio
    67: "SEM|" + CARTAO + "a big hand-drawn sun just rising over a line of rooftops, a big black Roman numeral \"I\" "
        "above it, the hand-lettered black capital words \"FIRST HOUR\".",
    68: "{M} stands in a long queue of stick figure men in white togas outside a big wooden door, looking tired and "
        "bored, yawning.",
    69: "The bright atrium of a rich Roman house with a square opening in the roof and a shallow pool below it: {PAT} "
        "greets a line of clients in white togas who bow politely.",
    70: "On a plain white background: one big stick figure in a bright white toga at the top labeled \"PATRON\", black "
        "arrows pointing down to five smaller stick figures in togas labeled \"CLIENTS\", hand-lettered black capital "
        "text.",
    71: "{PAT} hands a small leather money pouch to a grateful client in a toga, a sunny atrium with columns behind.",
    72: "{PAT} walks proudly with a big crowd of clients in white togas following behind him like a parade, small "
        "sparkles.",
    73: "A long line of stick figure clients in white togas waits at dawn outside the closed wooden door of a grand "
        "house, some yawning, one looking at the sky.",
    74: S + "Left side: a rich man's door with a huge crowd of clients and a big green check mark. Right side: another "
        "rich man's door with one single lonely client and a sad face.",
    75: "A stick figure servant hands out small woven baskets with bread and fruit to a line of clients in white togas.",
    76: "SEM|" + S + "Left side: a small woven basket full of bread and fruit. Right side: a small pile of copper coins. "
        "A black arrow from left to right over the dashed line.",
    77: "SEM|" + CARTAO + "a big pile of small copper coins, the hand-lettered black number \"100\" above it and the "
        "hand-lettered black capital word \"QUADRANTES\" below it.",
    78: "SEM|" + CARTAO + "one single small rough-edged ancient bronze coin drawn very large in the center, greenish brown, stamped with a simple open hand, the hand-lettered black capital word \"QUADRANS\" written once under it.",
    79: "{PAT} walks into a sunny Roman forum with temples and columns, followed by a long line of clients in white "
        "togas.",
    80: "{M} walks at the end of a line of clients in togas, rolling his eyes, a small grey storm cloud above his head.",
    # 5. Tribunais
    81: "An open-air Roman courtroom: a stick figure lawyer in a white toga speaks with one arm raised and the other "
        "hand on his throat, a scratchy jagged speech bubble, a seated judge behind him.",
    82: "A huge Roman basilica hall with tall columns and a high wooden roof, groups of stick figures in togas around "
        "raised platforms with seated judges, light streaming through high windows.",
    83: "A stick figure lawyer in a white toga gives a speech with one raised arm, while a court attendant in a short brown tunic stands beside a tall clay water jar on a wooden stand that drips water into a clay basin, pointing at the dripping water.",
    84: "{PLI} speaks in court with sweat drops on his head, and three small suns in an arc above him show the sun "
        "moving across the sky.",
    85: "SEM|" + CARTAO + "twelve small clay water jars in a neat row with a black bracket under them labeled \"12\", "
        "and four more clay water jars colored red at the end labeled \"+4\", hand-lettered black capital text.",
    86: "A big crowd of stick figure Romans watches a trial in a basilica like spectators at a show, some standing on "
        "tiptoe, one eating nuts from a cloth bag.",
    87: "A row of stick figure Roman men in simple tunics sit on a stone bench in the audience and clap loudly with big fake smiles, one of them secretly receives a coin from a lawyer in a white toga behind his back.",
    88: S + "Left side: Roman men clapping in a basilica for coins. Right side: a modern television showing an audience "
        "laughing, the hand-lettered words \"HA HA\" floating above it.",
    # 6. Trabalho
    89: "A busy sunny Roman street of shops in the morning: a porter carries a sack, a blacksmith hammers, a woman "
        "sells vegetables, all stick figures at work.",
    90: "A tired but determined stick figure Roman worker in a short brown tunic carries a heavy sack on his back and "
        "wipes sweat from his forehead.",
    91: "SEM|Very simple wide street view: a row of small Roman shops with wide open fronts and wooden shutters folded "
        "back, each with a masonry counter facing the street and clay jars inside, upper floor windows above.",
    92: "Cutaway view of a small Roman shop: the counter on the ground floor faces the street, and above it a small "
        "loft room reached by a wooden ladder, where a stick figure family sleeps on mattresses.",
    93: "A row of Roman shops side by side: a baker with round loaves, a butcher with hanging meat, a shoemaker with "
        "sandals, a blacksmith at an anvil, each stick figure busy at work.",
    94: "Inside a small Roman barber shop open to the street: a customer sits on a stool with a cloth around his neck "
        "while the barber shaves him with an iron razor, two other stick figures sit on a bench chatting and laughing.",
    95: "Close-up of a nervous stick figure customer with wide eyes being shaved by a barber holding a small flat crescent-shaped iron blade, a sweat drop, a few tiny red nick marks on his chin.",
    96: "Comic strip with exactly three equal side-by-side panels separated by thick black frame lines, the same "
        "barber and customer in each: first panel the barber starts shaving the customer's cheek, second panel the "
        "barber has slowly moved to the chin and the customer looks bored, third panel a full black beard has grown "
        "back on the customer's cheek and he looks furious.",
    97: "A quiet back room of a Roman house: an enslaved stick figure worker in a plain grey tunic scrubs the floor "
        "alone, while through the doorway other people chat in the sunny street.",
    98: "Four stick figure workers in plain grey tunics side by side: a cook stirring a pot, a porter carrying a heavy "
        "amphora, a bath attendant carrying towels, a shop worker sweeping.",
    99: "An exhausted stick figure worker in a plain grey tunic sits on a doorstep at dusk, while a stern master in a "
        "toga in the lit doorway points inside to call him back.",
    100: "A Roman fullery workshop: rows of stone tubs, stick figure workers washing woolen cloth, long pieces of white "
         "and colored cloth hanging to dry on wooden poles.",
    101: "SEM|" + CARTAO + "a large clay jar full of yellow liquid with a cartoon green stink cloud above it, the "
         "hand-lettered black capital words \"SECRET INGREDIENT\" with a hand-drawn arrow pointing at the jar.",
    102: "Inside a Roman fullery: a stick figure worker stands in a stone tub up to his knees, stamping on wet cloth "
         "with his feet and pinching his nose, green stink lines, clay jars lined up on the floor next to the tub.",
    103: "{IMP} sits at a wooden desk counting gold coins into a chest with a big grin, a clay jar with green stink "
         "lines next to the desk.",
    104: "A young stick figure Roman prince with short dark hair in a white toga pinches his nose with a disgusted face, "
         "standing in front of {IMP}.",
    105: "{IMP} holds a small gold coin right under the nose of a young prince with short dark hair in a white toga, "
         "raising one eyebrow, a question mark above them.",
    106: "A young stick figure prince with short dark hair in a white toga sniffs a small gold coin and shakes his "
         "head, a small speech bubble with the word \"NO\".",
    107: "{IMP} laughs hugely with his head tilted back and holds up a gold coin in triumph, a young prince in a white "
         "toga looks embarrassed beside him.",
    108: "{R} eats a piece of flatbread standing at a street counter, chewing fast, a few crumbs flying.",
    109: "SEM|A Roman street-food bar: an L-shaped masonry counter facing the street with round openings holding large "
         "clay jars, bright painted decorations on its front, a few clay cups on a shelf behind.",
    110: "SEM|Very simple wide landscape: the small Roman town of Pompeii with terracotta roofs and columns in the "
         "foreground and the big mountain Vesuvius behind it under a blue sky.",
    111: "Two stick figure archaeologists in sun hats carefully brush dust off a brightly painted ancient street "
         "counter, small sparkles around the painting.",
    112: "SEM|The brightly painted front of an ancient Roman food counter on a yellow plastered surface, painted in a simple cartoon style: two hanging ducks, a rooster, a dog on a leash, and on the right a sea nymph riding a mythical sea creature whose front is a white horse head with two front legs and whose back is a long coiled green fish tail curling out of blue waves.",
    113: "SEM|" + CARTAO + "five small doodles in a row, a duck, a pig, a goat, a fish and a snail, each above a broken "
         "clay jar, the hand-lettered black capital words \"ON THE MENU\" at the top.",
    114: S + "Left side: a Roman street-food counter with clay jars and a stick figure customer eating. Right side: a "
         "modern fast-food counter with a burger and a stick figure customer eating in the same pose.",
    115: "A stick figure Roman cook pours a dark sauce from a small clay amphora onto a plate of food, the stick figure "
         "customer smiles happily.",
    116: "SEM|" + CARTAO + "a cross-section of a big open stone tank filled with layers of small fish and white salt, a "
         "yellow sun above it, the hand-lettered black capital word \"GARUM\" with a hand-drawn arrow.",
    117: "SEM|" + S + "Left side: a small Roman clay jar of fish sauce with a green check mark. Right side: a modern "
         "bottle of fish sauce on a kitchen shelf with a green check mark.",
    118: "Only one character: {R} walks toward a busy market stall with an orange cloth awning, counting on his fingers with a thoughtful face, a thought bubble above him with the big number 8.",
    119: "SEM|" + CARTAO + "a row of seven calendar squares crossed out by a red X, and below it a row of eight calendar "
         "squares marked with the letters A B C D E F G H and a green check mark.",
    120: "A busy Roman market day in a town square: stalls with vegetables, cheese, chickens in wicker cages and "
         "pottery, colorful cloth awnings, many stick figure shoppers.",
    121: "A stick figure farmer in a straw hat leads a donkey loaded with baskets of vegetables through a town gate, "
         "while another farmer whispers news in his ear.",
    122: "SEM|" + CARTAO + "a modern calendar page with the word \"MONDAY\" crossed out by a red X, and next to it a "
         "small market stall doodle with the hand-lettered black capital word \"NUNDINAE\" and a green check mark.",
    # 7. Sexta hora
    123: "{R} lies on a stone bench in the shade of a tree at midday with his eyes closed, the letters \"Z Z Z\" "
         "floating above him, a bright sun high overhead.",
    124: "SEM|A quiet sunny Roman street at midday, shops with wooden shutters half closed, a dog asleep in the shade, "
         "a cat on a wall, wavy heat lines in the air.",
    125: S + "Left side: {R} naps on a stone bench at midday. Right side: {MOD} naps on a sofa after lunch.",
    126: "SEM|" + CARTAO + "the big hand-lettered black capital words \"SEXTA HORA\" in the center, a small sun at the "
         "top of a curved arc above them, the black Roman numeral \"VI\" under the sun.",
    127: "SEM|" + CARTAO + "a hand-drawn black arrow from the hand-lettered word \"SEXTA\" on the left to the "
         "hand-lettered word \"SIESTA\" on the right, a small pillow doodle with the letters \"Z Z\".",
    # 8. Os muros
    128: "{M} rolls up a scroll and stretches his arms with a satisfied smile, the black Roman numeral \"VII\" "
         "hand-lettered in the corner.",
    129: "Stick figure shopkeepers close the wooden shutters of their shops in the early afternoon with cheerful faces, "
         "the sun past the top of the sky.",
    130: "{R} walks along a sunny street with two friends, chatting and laughing, red painted letters on the walls "
         "behind them.",
    131: "SEM|A white plastered Roman wall drawn as a cartoon character with two big round eyes and a wide open talking mouth, a few red painted brush strokes on it, three speech bubbles coming out of its mouth.",
    132: "SEM|A long Pompeian street wall covered with dozens of painted red and black notices and tiny scratched "
         "graffiti, a stone-paved street with big stepping stones in front.",
    133: "A stick figure sign painter on a wooden ladder paints the big red capital letters \"VATIA\" on a white plastered wall, another stick figure holds a bucket of red paint below him.",
    134: "A group of tipsy cheerful stick figure Romans with wine cups, arms around each other, cheer in front of a wall "
         "with a big red painted notice reading \"VATIA\".",
    135: "Two sneaky stick figure thieves tiptoe past a wall, one holding a stolen coin purse and giving a thumbs up to "
         "a big red painted notice reading \"VATIA\".",
    136: "Two smirking stick figure politicians in white togas hide around a street corner holding a paintbrush and a "
         "pot of red paint, giggling.",
    137: "A stick figure traveler in a brown cloak scratches letters into a plastered wall with a small pointed stylus, "
         "proud smile.",
    138: "SEM|Close-up of a plastered wall with scratched black capital letters reading \"C PUMIDIUS DIPILUS HEIC "
         "FUIT\", and below it a small hand-lettered label \"78 BC\".",
    139: "Outside a doorway of a Roman house on a sunny street: a stick figure traveler with a small bundle scratches "
         "letters into the plastered wall next to the door with a stylus, looking a bit guilty.",
    140: "Two embarrassed stick figure travelers stand next to a messy wooden bed, one shrugging with open hands and "
         "pointing at an empty corner of the room, a big question mark in the corner.",
    141: "{R} stands in front of a plastered wall covered with scratched doodles of little stick figures, a ship, a gladiator, a heart and a cat, nodding knowingly with one hand on his chin.",
    142: "A cartoon plastered wall with a tired face, covered in scribbles, sweating and bending under a heavy pile of "
         "words, small cracks in it, a stick figure with a stylus walking toward it.",
    # 9. Termas
    143: "{M} points at a sunny exercise courtyard surrounded by columns, where two adult stick figure wrestlers in short loincloths grapple, their bodies shining with oil, small sparkles on them.",
    144: "{R} walks happily toward the entrance of a big Roman bath building with arches and a domed roof, carrying a "
         "small towel and a small oil flask.",
    145: "Very simple wide view of a grand Roman public bath building: a big domed hall, arched windows, columns, smoke "
         "rising from the furnace chimneys, many tiny stick figures walking in.",
    146: "{R} pays one small copper coin to a bath attendant sitting at a small table at the entrance, the attendant "
         "smiles.",
    147: "SEM|" + CARTAO + "a big pile of small copper coins on the left, a black arrow, and on the right one single "
         "copper coin next to a small doodle of a steaming bath, the hand-lettered black capital words \"1 BATH\".",
    148: "A sunny exercise courtyard surrounded by columns: stick figures in short tunics throw a ball, two wrestle, one "
         "lifts round lead weights, one runs.",
    149: "Comic strip with exactly three equal side-by-side panels separated by thick black frame lines: first panel a "
         "warm orange room with a stick figure relaxing on a bench, second panel a steaming hot red room with a "
         "sweating stick figure, third panel a cold blue pool with a shivering stick figure jumping in.",
    150: "The entrance of a Roman bath with stick figure men in tunics and women in long dresses walking in, a cheerful "
         "busy scene.",
    151: "SEM|" + CARTAO + "a big hand-drawn half circle path of the sun divided into slices, the left part colored pink "
         "and labeled \"WOMEN\", the right part colored blue and labeled \"MEN\", hand-lettered black capital words.",
    152: "A stick figure archaeologist in a sun hat holds up a large flat bronze tablet covered with rows of engraved "
         "Latin letters, amazed face, a rocky mining hill behind him.",
    153: "SEM|" + CARTAO + "a horizontal timeline of the day marked with black Roman numerals, a pink bar from \"I\" to "
         "\"VII\" labeled \"WOMEN\", and a blue bar from \"VIII\" into a dark night section with a crescent moon "
         "labeled \"MEN\".",
    154: "SEM|" + CARTAO + "on the left a small copper coin cut in half labeled \"MEN 1/2\", on the right a whole copper "
         "coin labeled \"WOMEN 1\", and a big hand-lettered red \"x2\" between them.",
    155: "SEM|" + CARTAO + "a modern bar of soap crossed out by a big thick red X, and next to it a small clay oil flask "
         "with a green check mark.",
    156: "A stick figure bather sits on a stone bench and scrapes oil off his arm with a curved bronze strigil, drops of "
         "oil and dirt flying, a small oil flask beside him.",
    157: "Close-up of a stick figure bather looking with disgust and amazement at a curved bronze strigil full of brown "
         "grime.",
    158: "Inside a big echoing Roman bath hall full of stick figures, giant hand-lettered sound words \"SPLASH\", "
         "\"HEY!\" and \"AAAH\" floating in the air.",
    159: "Cutaway of a building: on the top floor {SEN} sits at a desk with a scroll in a small room; on the ground "
         "floor below him a noisy busy bath full of steam and stick figures.",
    160: "{SEN} writes a letter on a scroll with a tense face and twitching eyebrows, sound lines coming up through the "
         "floor.",
    161: "A muscular stick figure in a short loincloth lifts heavy round lead weights above his head, grunting, the big "
         "hand-lettered sound word \"HNNNG\", sweat drops.",
    162: "A stick figure masseur slaps the shoulders of a bather lying face down on a bench, big hand-lettered sound "
         "words \"SLAP\".",
    163: "A stick figure ball player throws a small ball in the air and shouts numbers, a speech bubble with "
         "\"7! 8! 9!\".",
    164: "A stick figure bather in a hot pool sings loudly with his eyes closed and musical notes floating around him, "
         "other bathers cover their ears.",
    165: "Stick figures jump into a big pool with huge water splashes and the hand-lettered sound word \"SPLASH\".",
    166: "A skinny stick figure hair plucker with tweezers plucks the armpit hair of a customer who screams with a big "
         "open mouth, the hand-lettered sound word \"OUCH\".",
    167: "Three stick figure sellers inside a bath hall: one with a tray of sausages, one with a tray of round pastries, "
         "one with a jug of drinks, all shouting with speech bubbles.",
    168: "{SEN} sits calmly with crossed legs and closed eyes, perfectly serene, while noise lines bounce around him.",
    169: "{SEN} carries a wooden box of scrolls out of a door with a fed-up face, a black arrow pointing away, a noisy "
         "steaming bath behind him.",
    170: "A Roman public latrine: a long row of stone seats with keyhole-shaped holes along the walls, several stick "
         "figure men sit side by side chatting, a small water channel in front of their feet.",
    171: "SEM|" + CARTAO + "a sea sponge stuck on the end of a wooden stick, the hand-lettered black capital words "
         "\"TOILET PAPER?\" with a hand-drawn arrow pointing at it.",
    172: "A stick figure man in a Roman latrine holds a sponge on a stick and looks at the viewer with a horrified face "
         "and a sweat drop.",
    # 10. Jantar
    173: "{M} lies on his left side on {LEITO}, propped on one elbow, smiling and reaching toward {MESA} with bowls of food, the hand-lettered black Roman numeral \"IX\" in the corner.",
    174: "A Roman dining room in the late afternoon with three of {LEITO} arranged around {MESA}, painted red walls, warm orange light, a stick figure servant carrying a tray of food.",
    175: "View from above of a Roman dining room: three of {LEITO} in a U shape around {MESA}, on each bed three stick figure guests lie on their left side propped on their left elbow, painted red walls.",
    176: "A Roman dinner party: stick figure guests in togas lie on their sides on {LEITO}, laughing and talking, {MESA} with many empty plates, painted red walls, the sun setting through a window.",
    177: "SEM|" + CARTAO + "a white egg on the left and two red apples on the right, joined by a long black arrow, the "
         "hand-lettered black capital words \"AB OVO USQUE AD MALA\".",
    178: "SEM|" + CARTAO + "a row of dishes from left to right: a plate of boiled eggs, a plate of grilled fish, a roast "
         "chicken, and a bowl of apples and grapes.",
    179: "{PAT} stands next to an empty {LEITO} with his arms crossed and an annoyed face, tapping his foot, painted red walls.",
    180: "{PLI} writes an angry letter at a desk, steam coming out of his head.",
    181: "SEM|" + CARTAO + "a small lettuce, three snails, two eggs, a small bowl of olives, red beets and onions laid "
         "out in a neat row like a menu.",
    182: "A small stage in a Roman dining room with three stick figure entertainers: one reads from a scroll, one acts "
         "holding a theater mask, one plays a lyre.",
    183: "A lively dinner party in another house: stick figure guests eat oysters and sea urchins while dancers with "
         "castanets perform, one guest in the middle laughing and having a great time.",
    184: "{R} shrugs at the viewer with a small smile and both hands open, plain cream background.",
    185: "A ridiculously rich, fat stick figure with gold rings on every finger lies on {LEITO} decorated with gold, next to him a tall bronze jar on a stone column with a thin stream of water dripping from it into a bronze basin below.",
    186: "A stick figure trumpeter in a fancy red and gold tunic blows a long curved bronze horn next to a rich fat man lying on {LEITO}, who looks startled, the hand-lettered sound word \"TOOT\".",
    187: "{R} looks at {SOL} and, next to it, a tall clay water jar on a wooden stand dripping into a basin, rubbing his chin thoughtfully, a question mark above.",
    188: "" + S + "Left side: a lavish Roman dinner in a villa with stick figures lying on {LEITO}. Right side: {R} eats a small bowl of porridge alone sitting on a wooden stool in a tiny plastered room.",
    189: "Inside a small apartment: a tiny clay brazier with a small fire on a wooden floor, a worried stick figure "
         "resident looks at the flames with a sweat drop.",
    190: "SEM|" + CARTAO + "a simple meal: a bowl of porridge, a round loaf of bread, a bowl of beans, a few vegetables, "
         "and a clay cup of wine next to a small water jug.",
    191: "{R} buys a steaming bowl of stew from a street bar counter in the late afternoon, smiling.",
    192: "{M} smiles mischievously and raises one finger with an idea, small sparkles around his finger.",
    193: "{M} proudly holds up several papyrus scrolls tied with red ribbons.",
    194: "{IMP} lies relaxed on {LEITO} after dinner, holding a wide shallow clay wine cup in one hand and reading a papyrus scroll with a smile, painted red walls.",
    195: "{M} winks at the viewer while secretly sliding a papyrus scroll toward a relaxed emperor with a golden laurel wreath who lies on {LEITO}.",
    196: S + "Left side: {M} offers a scroll to the viewer with a grin. Right side: {MOD} holds a smartphone and points "
         "at it with the same grin.",
    # 10b. Folga
    197: "{R} cheers happily in a festive Roman street decorated with flower garlands and colorful ribbons, people dancing behind him.",
    198: "A festive Roman street with flower garlands, a procession of stick figures carrying banners, people cheering.",
    199: S + "Left side: a stick figure actor holding a theater mask on a stage. Right side: two stick figure "
         "gladiators with shields facing each other in a sandy arena.",
    200: "SEM|Very simple wide view of the Circus Maximus: a long racetrack with a central barrier decorated with "
         "statues and an obelisk, huge tiers of seats full of tiny colorful spectators, four chariots racing.",
    201: "A giant crowd of tiny stick figure spectators fills the stands of a racetrack, waving cloths, the hand-lettered "
         "black number \"150,000+\" above them.",
    202: "SEM|" + CARTAO + "four flags in a row colored red, white, green and blue, each with a small chariot doodle "
         "and the hand-lettered black capital words \"REDS\", \"WHITES\", \"GREENS\", \"BLUES\".",
    203: "{PLI} sits at a wooden desk writing on a papyrus scroll in a quiet room with painted walls; through a window, far away, the stone stands of an ancient Roman racetrack full of a cheering crowd.",
    204: "{PLI} stands at a window shaking his head with a puzzled face; far away through the window, horse-drawn two-wheeled Roman chariots race on a sandy track in front of stone stands full of a cheering crowd.",
    205: "A crowd of stick figure fans cheers wildly for a green cloth flag on a pole, while horses race behind them "
         "unnoticed.",
    206: "Comic strip with exactly two equal side-by-side panels separated by a thick black frame line: first panel "
         "stick figure fans in green cheer for a charioteer in green, second panel the charioteers have swapped "
         "colors and the same fans now cheer for the blue one, small question marks.",
    207: "{MOD} wears a sports jersey and screams with joy at a television showing a football match, waving a scarf.",
    208: "{JUV} stands with his arms crossed and a dark grey cloud above his head.",
    209: "Stick figure Roman citizens in togas at an outdoor assembly raise their hands to vote, a general in a red "
         "cloak and bronze armor salutes them.",
    210: "SEM|" + CARTAO + "a round loaf of Roman bread on the left and, on the right, a small two-wheeled Roman racing chariot pulled by one galloping horse, joined by a plus sign, the hand-lettered black capital words \"PANEM ET CIRCENSES\".",
    211: "SEM|Very simple wide landscape of the rooftops of Rome at sunset, orange and purple sky, the sun sinking behind "
         "a hill with temples.",
    212: "SEM|A pitch-dark narrow Roman street at night under a navy blue sky with stars, only the dark shapes of the "
         "buildings.",
    213: "Night street: a rich stick figure Roman in a white toga walks home surrounded by servants carrying flaming "
         "torches, warm orange light on the walls, dark navy shadows.",
    214: "{R} sits in his room and writes on a wax tablet with a worried face and a sweat drop, a rolled dinner "
         "invitation on the table.",
    215: "Night street: a clay pot falls from an upper window toward a stick figure walking below, who looks up in "
         "horror, motion lines.",
    216: "Night street: a stick figure leans out of an upper window and empties a chamber pot, a passer-by below jumps "
         "aside just in time, the hand-lettered sound word \"SPLASH\".",
    217: "Night street with a navy blue sky: a heavy cart loaded with amphorae, two drunk stick figures singing arm in "
         "arm, and the orange glow of a fire on a distant rooftop.",
    218: "A group of stick figure Roman watchmen in short tunics carrying buckets, axes and torches run along a night "
         "street toward a burning building.",
    219: "{R} in his small dark room lights {LAMPADA}, a warm orange glow on his face and the walls.",
    220: "SEM|Close-up of the flickering flame of {LAMPADA} on a wooden table next to a few copper coins, the "
         "room dark around it.",
    221: "{R} sleeps on a straw mattress, {LAMPADA} on the floor with its flame out and a thin wisp of smoke; through a small window with open wooden shutters, ox carts rumble along the dark street, sound lines.",
    222: "Dark blue sky before dawn: {MES} takes a deep breath, ready to shout, while a rooster still sleeps on a wall.",
    # 12. Fechamento
    223: "{R} stands on a plain cream background facing the viewer, thoughtful, a big black question mark above him.",
    224: "{R} works at a market stall in the morning sun, stacking clay jars, sweat drops.",
    225: "{T} shakes hands with {PAT} in a sunny atrium, both smiling.",
    226: "Comic strip with exactly three equal side-by-side panels separated by thick black frame lines, the same man in "
         "each: {R}. First panel he eats at a street counter, second panel he writes on a wall with a stylus, third "
         "panel he relaxes in a steaming bath.",
    227: S + "Left side: {R} naps under the sun on a stone bench. Right side: {MOD} naps in an office chair.",
    228: "SEM|" + CARTAO + "the hand-lettered black capital words \"NONA HORA\" on the left, a black arrow to the "
         "hand-lettered word \"NOON\" on the right, the black Roman numeral \"IX\" above.",
    229: "SEM|" + CARTAO + "a hand-drawn half circle path of the sun with a small sun in the mid-afternoon position and a "
         "curved black arrow sliding it back up to the top of the arc, where the hand-lettered label \"12\" is.",
    230: "SEM|" + CARTAO + "the hand-lettered black capital words \"SEXTA HORA\" with a black arrow to the word "
         "\"SIESTA\", the black Roman numeral \"VI\" above, a small pillow doodle.",
    231: "{FOM} shakes his fist at {SOL} with furious eyebrows.",
    232: "{MOD} sits at an office desk and shakes his fist at a computer screen showing a calendar full of colored "
         "blocks, furious eyebrows.",
    233: "SEM|" + CARTAO + "a stack of papyrus scrolls and a wax tablet next to a fragment of plastered wall with "
         "scratched letters, the hand-lettered black capital word \"SOURCES\" with a hand-drawn arrow pointing down.",
    234: "{R} and {M} stand side by side in front of {SOL}, waving goodbye to the viewer with big smiles.",
}


def prompt(n: int) -> str:
    texto = P[n]
    sem = texto.startswith("SEM|")
    texto = texto.removeprefix("SEM|")
    for k, v in PERSONAGENS.items():
        texto = texto.replace("{" + k + "}", v)
    texto = texto[0].upper() + texto[1:]
    return f"{texto} {BASE}" if sem else f"{texto} {BONECO} {BASE}"
