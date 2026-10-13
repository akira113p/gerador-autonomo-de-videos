"""Prompts de imagem do vídeo 6 (camponês medieval inglês, c. 1300) para o Z-Image local, um por linha numerada do roteiro.md.

prompt() põe o estilo (BASE) e, se a cena tem stick figure, a descrição do boneco (BONECO).
{CARD} = cartão de fundo branco (palavras curtas, conferir a grafia).
Sem sangue nem corpos: fome e peste aparecem por chuva, celeiro vazio e cartões. Nenhum objeto moderno (sem chaminé, vidro,
batata, milho, relógio, calendário de espiral); objetos de época descritos pela forma. Época: Inglaterra, por volta de 1300.
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
    "C": "the stick figure peasant Hugh, a man in his thirties with short messy brown hair, a rough knee-length brown tunic "
         "with a rope belt, grey cloth leggings and simple leather shoes",
    "W": "his stick figure wife Alice with a white linen cloth wrapped over her hair, a long green wool dress and a simple apron",
    "K": "two small stick figure children in plain undyed tunics",
    "LORD": "the stick figure abbot, a stern man in a long black hooded robe with a rope belt and a round bald patch on top of his head, "
            "a gold ring on one hand",
    "R": "a stick figure village reeve in a red tunic and a soft hood, holding a long wooden staff",
    "PR": "a stick figure village priest in a long plain dark-green robe",
    "OX": "two big brown oxen with curved horns joined by a wooden yoke, pulling a wooden plough with a pointed iron blade",
    "HOUSE": "a low small house with walls of woven sticks plastered in brown mud, a thick thatched roof of golden straw reaching almost "
             "to the ground and a rough wooden door",
    "FIRE": "a small open fire of burning logs in the middle of a dirt floor ringed by round stones, a thin line of grey smoke rising to the thatched roof",
    "CARD": CARTAO,
    "S": "Split screen divided by a vertical black dashed line. ",
}

P = {
    # 0. Abertura
    1: "{CARD}a row of seven simple boxes with three of them filled in red, a tiny abbey icon above the red ones, the hand-lettered words \"3 DAYS UNPAID\".",
    2: "{CARD}a pair of tiny stick figures, a bride with a flower wreath and a groom, next to a pile of coins, the hand-lettered words \"MARRIAGE FEE\".",
    3: "{CARD}a happy brown cow with a thick red circle around it and a small hand reaching for it from the side, the hand-lettered words \"YOUR BEST ANIMAL\".",
    4: "A wide green English countryside with a small village of low thatched houses, a small stone church with a square tower, narrow strips of fields in green and gold and a winding dirt road, bright blue sky.",
    5: "{C} points at himself with one thumb and a shy smile, plain cream background.",
    6: "{C} scratches his head with a big thought bubble showing a muddy stick figure bent over a hoe next to a small tombstone with the number 30, plain cream background.",
    7: "{CARD}a big hand-drawn question mark in the middle with a green check on the left and a red X on the right, the hand-lettered words \"TRUE OR MYTH?\".",
    8: "{CARD}a flower wedding wreath and a small stone castle with a big red question mark between them, the hand-lettered words \"FIRST NIGHT?\".",
    9: "{CARD}a big hand-lettered number \"150\" with a thick red question mark and small sun doodles around it, the hand-lettered words \"DAYS A YEAR?\".",
    10: "A wide view of an English village across a whole year: green spring field on the left, golden wheat in the middle and bare brown fields with a little snow on the right, a winding road through them, soft light.",
    11: "{C} walks behind {OX} across a brown field, a plain flat horizon, early morning light.",
    12: "A dark rainy sky over an English village, grey rain falling on thatched roofs, a small stick figure family looking out of a low doorway with worried faces.",
    # 1. Quem é você
    13: "{CARD}a round name tag sticker with the hand-lettered black capital word \"HUGH\" in the middle and a small smiling stick figure drawn beside it.",
    14: "{C} holds a hand over his heart with a faint outline of an old rolled parchment scroll behind him, plain cream background.",
    15: "A stick figure king in a red robe and a gold crown sits on a throne in a stone hall and hands a rolled parchment to two stick figure officials in long grey robes holding feather quills.",
    16: "Two stick figure officials in long grey robes write on a long roll of parchment while a stick figure villager stands in front of them holding his cap in both hands, thatched houses behind.",
    17: "{CARD}on the left a small stick figure farmer holding a handful of grain, an arrow in the middle, and on the right a big manor house, the hand-lettered words \"LAND FOR WORK\".",
    18: "{CARD}a green square field with the hand-lettered number \"25\" in it and the word \"ACRES\" below.",
    19: "{C} stands proudly with open arms in front of a big green field, a dotted red line splits the field into many narrow strips, bright green and gold.",
    20: "A bird's-eye view of a big open field cut into many long narrow strips in different shades of green and gold, a few tiny stick figure farmers working on different strips side by side.",
    21: "{CARD}a big full square labeled \"FULL\" next to a half-size square labeled \"HALF\", the hand-lettered numbers \"18\" and \"5\" above them.",
    22: "A stick figure cottager in a ragged tunic stands outside a very small hut with a tiny garden plot and a single hen, scratching his head.",
    23: "{CARD}a big hand-drawn crowd of tiny stick figures filling a circle, the hand-lettered words \"4.5 TO 6 MILLION\".",
    24: "A wide countryside with several tiny villages of thatched houses connected by dirt paths, green rolling hills and one small walled town far in the distance.",
    25: "{LORD} stands in front of a stone abbey with a square tower, one hand raised in a blessing, warm golden light.",
    26: "A wide view of a manor: a big stone hall with a flag, a large wooden barn, a small stone church and thatched cottages around a green.",
    27: "{CARD}a rolled parchment contract with a feather quill and a big question mark, the hand-lettered words \"SIGN HERE?\".",
    # 2. Michaelmas
    28: "{CARD}a bundle of golden wheat stalks tied with a rope, a small angel with wings above it, the hand-lettered words \"29 SEPTEMBER\".",
    29: "A stick figure steward in a green tunic sits at a wooden table covered with parchment rolls, counting small stacks of coins, a feather quill in his hand.",
    30: "A circle of stick figure villagers under a big oak tree raise their hands, {R} stands in the middle and is lifted up by two neighbors, cheerful mood.",
    31: "{CARD}a purse of coins with a big arrow pointing to a small abbey, the hand-lettered words \"EXTRA TAX\".",
    32: "{CARD}a blank price tag with a big question mark, the hand-lettered words \"ANY AMOUNT\".",
    33: "{C} walks behind {OX} ploughing a brown field at dawn, mist over the soil, birds following the plough.",
    34: "{C} holds up one palm in a stop gesture with a worried face, behind him a big field of golden stubble, light grey sky.",
    35: "{C} ploughs the abbot's big field under a hard sun while {LORD} watches from a shady stool with crossed arms, a tiny unploughed field far away in the distance.",
    36: "{CARD}three small icons in a row: a candle, a painted egg and a white dove, the hand-lettered words \"3 WEEKS OFF\".",
    37: "{C} and a second stick figure man swing small curved blades in a golden wheat field, {LORD} sits on a stool nearby and watches.",
    38: "{C} eats bread and drinks from a clay cup at a long outdoor table at the edge of a field, other stick figure workers eating around him, a steward serving.",
    39: "{C} ploughs a small strip of brown land with {OX} under a dark cloudy sky, heavy mist, a thin narrow strip beside the big field.",
    40: "A stick figure man in a green tunic holds a big open handwritten book showing a drawing of a plough, standing in a brown field next to a pair of oxen with a wooden yoke.",
    41: "{CARD}a green square field divided into four equal parts with one part colored, the hand-lettered words \"ROOD = 1/4 ACRE\".",
    42: "A big cheerful brown ox with curved horns stands next to a tall white horse, the horse has a big plain price tag hanging from its neck and a worried face, plain cream background.",
    43: "{CARD}a sack of golden seed grain with a wooden scoop next to a small green square, the hand-lettered words \"2 BUSHELS / ACRE\".",
    44: "{CARD}one small grain sack, an arrow and three small grain sacks, a big red zero coin on the right, the hand-lettered words \"3x = NO GAIN\".",
    45: "{C} scatters handfuls of golden seed over a brown field and looks up at the sky with crossed fingers, bright clouds on the left and dark clouds on the right.",
    46: "An open decorated old book with a gold border, bright blue and red, a small drawing of two oxen pulling a plough in the bottom margin and a rich knight in a red coat on a horse at the top.",
    47: "A close-up of the margin of an old decorated book where tiny peasants in colorful clothes work with tools, a magnifying glass held over one of them.",
    # 3. Inverno
    48: "A snowy village at dusk with grey smoke rising from thatched roofs, bare trees and a stone church with a square tower, warm orange glow at the low doors.",
    49: "{HOUSE}, {C} stands proudly in front of the door.",
    50: "A cut-away of a long low thatched house: stick figures sleeping on straw on the left side, two cows and a goat on the right side, a low wall in the middle, warm light.",
    51: "Two stick figure archaeologists in sun hats kneel beside low grey stone foundations of a long rectangular house on a green moor, brushes in their hands, small flags in the ground.",
    52: "A stick figure family walks through a low doorway in the middle of a long thatched house while a brown cow walks through the same door from the other side, seen from the front.",
    53: "{HOUSE}, close-up of the wall showing woven sticks and brown mud, wooden beams showing at the corner, plain cream background.",
    54: "{C} warms his hands at {FIRE}, long shadows dancing on the walls of the dark house.",
    55: "{C} coughs with a hand over his mouth, wavy grey smoke fills the small room around him and drifts up into the thick straw roof.",
    56: "{CARD}a cartoon gold medal on a ribbon next to a cloud of grey smoke and a ham hanging on a hook, the hand-lettered word \"CONGRATS!\".",
    57: "A small crooked house falling apart in a puff of dust, a stick figure historian with grey hair and a pointer stick watching with a surprised face.",
    58: "A long row of sturdy old timber-framed thatched houses on a quiet village street in warm sunlight, a stick figure historian gives a thumbs up.",
    59: "A village at sunset with the orange sky fading to deep blue, thatched houses and a distant church, {C} walks home with a hoe on his shoulder.",
    60: "{C} lounges on a pile of straw with a clay cup in one hand, eyes closed, smiling, soft winter sun.",
    61: "{CARD}a small stone church with a square tower and a row of five small golden halos above it, the hand-lettered words \"NO WORK TODAY\".",
    62: "{C} swings a long wooden stick joined to a shorter stick by a short rope over a pile of grain on a barn floor, golden dust flying in the air.",
    # 4. Primavera
    63: "{CARD}a white lily flower with the hand-lettered words \"25 MARCH\" and \"LADY DAY\".",
    64: "{CARD}a big banner with the hand-lettered words \"NEW YEAR\" and the date \"25 MARCH\", the date \"1 JAN\" crossed out with a thick red X.",
    65: "{CARD}a long arrow from left to right with the hand-lettered number \"1752\" at the arrow tip, small flower doodles.",
    66: "{C} scatters seeds from a cloth bag slung over his shoulder across a fresh brown field, green sprouts in the neighbor's field, birds flying, spring sunshine.",
    67: "{CARD}a plate with a roasted chicken leg crossed out by a thick red X and a fish next to it with a green check, the hand-lettered words \"LENT: NO MEAT\".",
    68: "A wooden barn with open doors showing an almost empty floor with only a few grains, spring flowers growing outside, soft light.",
    69: "{CARD}a nearly empty grain sack labeled \"LAST YEAR\" on the left and a field of still-green stalks labeled \"THIS YEAR\" on the right.",
    70: "A skinny stick figure family of three sits on the doorstep of a tiny hut with empty wooden bowls and big sad eyes, spring flowers in the background.",
    71: "{CARD}a single small loaf of bread next to a coin cut into a quarter, the hand-lettered words \"1/4 PENNY / DAY\".",
    72: "{CARD}a round coin divided into four slices with one slice highlighted in gold, the hand-lettered fraction \"1/4\".",
    73: "{LORD} sits at a table in front of a barn while {C} bows and sets three hens, a rooster and a basket of five eggs on the table, bright spring day.",
    74: "{CARD}three hens, a rooster and five eggs in a row, the hand-lettered numbers \"3\", \"1\" and \"5\" under each group.",
    75: "{LORD} holds up a painted egg with a delighted smile, small sparkles, plain cream background.",
    # 5. A mesa
    76: "{C} holds an empty wooden bowl toward the viewer with a hopeful face and a rumbling belly drawn with curly lines, plain cream background.",
    77: "{CARD}a big round pie chart with four fifths filled in golden wheat color and a wheat icon, the hand-lettered words \"80% GRAIN\".",
    78: "{CARD}three icons in a row: a dark loaf of bread, a bowl of stew and a clay jug of ale, the hand-lettered words \"BREAD, STEW, ALE\".",
    79: "{CARD}a big dark brown loaf labeled \"DARK\" on the left and a small light white loaf with a thick red X over it labeled \"WHITE\" on the right.",
    80: "A big dark round-bellied cooking pot on three short legs hanging over a small fire, thick bubbling stew with peas, leeks and onions floating in it, a long wooden spoon.",
    81: "Two clay jugs side by side: a fresh jug with golden foamy ale and a second jug with a sour green wobbly cloud around it and a sad face, plain cream background.",
    82: "{W} stirs a big wooden tub of frothing ale with a long wooden paddle outside a thatched house, jugs lined up beside her, a bundle of green leaves tied to a pole above the door.",
    83: "A plump pink pig snuffles under an oak tree among fallen acorns, a thatched house behind it, autumn colors.",
    84: "{CARD}a wooden table with a big pile of bread, a small wedge of cheese, a tiny cup of ale and a tiny fish, the hand-lettered words \"MUCH BREAD, LITTLE MEAT\".",
    85: "{CARD}a plate with bread, cheese and a bit of fish labeled \"HARVESTER\" next to a smaller plate with only bread labeled \"PEASANT\".",
    86: "{C} stares sadly at a plate with a loaf of bread, next to another loaf of bread, plain cream background.",
    # 6. Verão e colheita
    87: "A wide golden wheat field under a hot yellow sun, red poppies at the edges, a few tiny stick figures far away in the field, bright orange sky.",
    88: "{CARD}a big golden bundle of wheat tied with a rope under a shining star, the hand-lettered word \"HARVEST\".",
    89: "{C} and {W} and {K} cut wheat with small curved blades side by side in a golden field, sweat drops flying, a blazing sun above, neighbors in the background.",
    90: "A close-up of {C} bent over, cutting a handful of wheat with a small curved blade held in one hand, golden stalks in his other arm, sweat drops.",
    91: "Two stick figure workers walk along a dirt road toward a big golden field where {LORD} waits with crossed arms, their own field behind them half cut.",
    92: "A line of tidy tied golden wheat sheaves stands in a big field, while the neighboring small field is still uncut and a dark cloud approaches.",
    93: "A cart piled high with golden wheat sheaves pulled by {OX} along a dirt road toward a big wooden barn, {C} walks beside it.",
    94: "{CARD}the hand-lettered words \"ONLY 150 DAYS?\" with a big red question mark and a tiny sun, wheat doodles around.",
    95: "A smug stick figure author holds up a thick book and points a stick at the smallest number on a list of numbers written on a hanging cloth.",
    96: "{CARD}a bar chart with a tall bar labeled \"250+\" and a much shorter bar labeled \"150\" with a thick red X over it.",
    97: "{CARD}a tall bar with the hand-lettered number \"300\" and a small wheat icon, the hand-lettered words \"BEFORE THE PLAGUE\".",
    98: "{C} shakes his head from side to side firmly with crossed arms, plain cream background.",
    99: "{CARD}three small icons in a row: a church, a golden halo and a sun, the hand-lettered words \"SUNDAYS, SAINTS, 3 WEEKS\".",
    100: "A dark thundercloud rolling toward a golden wheat field and a barn, a stick figure farmer looks up nervously with clasped hands.",
    # 7. Dia de tribunal
    101: "A stream of stick figure villagers in rough tunics and hoods walks along a dirt road toward a big wooden hall, some carrying hens, a bell ringing.",
    102: "Inside a plain wooden hall, stick figure villagers sit on benches in rows, {R} stands at the front holding his staff, a clerk writes on a parchment roll at a table, serious faces.",
    103: "{CARD}a small pile of coins with an arrow falling onto it and a stern face, the hand-lettered word \"FINES\".",
    104: "A stick figure clerk in a plain robe writes with a long feather quill on a very long parchment roll that unrolls across the floor, an ink pot beside him.",
    105: "A close-up of a rolled parchment covered with tiny handwritten lines, brown with age, a stick figure historian points at a line with a stick.",
    106: "A stick figure inspector in a green hood tastes a jug of ale with a suspicious face, jugs lined up on a table, a stick figure woman brewer waits nervously outside her house.",
    107: "{CARD}two small coins labeled \"2d\" and a foamy mug of ale, the hand-lettered words \"2 PENCE PER BREW\".",
    108: "A brown cow stands in a neighbor's green crop field munching, a broken hedge of branches behind it, two stick figure farmers argue with raised fists.",
    109: "A small empty thatched house with its door swinging open and a field of weeds, a stick figure official in a green tunic hammers a wooden marker stake into the ground, a distant figure walks away down a road with a bundle on a stick.",
    110: "{CARD}a foamy mug of ale with a paper ticket attached and a coin beside it, the hand-lettered word \"PERMIT\".",
    111: "{CARD}a coin on the left, an equals sign and a paper ticket on the right, the hand-lettered words \"FINE = PERMIT\".",
    112: "A row of stick figure villagers in plain tunics sits on a long bench as a jury, facing the viewer with serious faces, one nodding.",
    113: "{C} sits on the jury bench and points at himself with a surprised face, the other villagers laugh.",
    114: "{C} runs along a dirt road away from a thatched village with a bundle on a stick over his shoulder, a trail of dust behind him, {R} far behind waving his staff.",
    115: "A stone town gate with two towers and an open gate with sunshine behind it, {C} peeks through the gate with a hopeful smile, a flag on top of the tower.",
    116: "{CARD}a sun and a moon repeated in a long row with the hand-lettered words \"A YEAR AND A DAY\".",
    # 8. As contas
    117: "{C} sits at a rough wooden table counting a small pile of coins with a worried frown, a stick with notches beside him.",
    118: "{CARD}four icons in a row: a plough, a coin purse, a hen and an egg, the hand-lettered words \"WORK, TAX, HENS, EGGS\".",
    119: "{C} hands a small purse of coins to {LORD} while his daughter in a flowered dress and a stick figure groom wait hand in hand behind him.",
    120: "{CARD}a roll of film with a thick red X over it, the hand-lettered words \"NOT LIKE THE MOVIES\".",
    121: "{CARD}a rolled scroll with a big question mark and a thick red X, the hand-lettered words \"NO EVIDENCE\".",
    122: "{CARD}a purse of coins moving along an arrow from a small family icon to a big manor icon, the hand-lettered words \"A PAYMENT\".",
    123: "{CARD}a sheet of paper with boxes to tick and a coin, the hand-lettered words \"TAX FORM\".",
    124: "A stick figure old man sleeps peacefully in a straw bed with a small cross on the wall, {W} and {K} sit by the bed holding hands, a stick figure steward waits in the doorway holding a parchment roll.",
    125: "A stick figure steward in a green tunic leads away the family's best brown cow by a rope from a small barn while the family waves sadly from the door.",
    126: "{PR} leads away a second animal, a sheep, by a rope from the yard while a stick figure family stands in the doorway of a thatched house.",
    127: "{CARD}a sad face with a tear, a cow and a sheep each crossed out with a red X, the hand-lettered words \"-2 ANIMALS\".",
    128: "{PR} points at one sheaf out of a row of ten wheat sheaves, which glows gold, while {C} watches with a pained face.",
    129: "{CARD}ten bundles of wheat in a row with the tenth bundle colored gold and an arrow to a small church, the hand-lettered words \"1 IN 10\".",
    130: "{CARD}a big round pie chart with exactly half colored red and a small abbey icon on the red half, the hand-lettered words \"HALF YOUR WEEK\".",
    131: "{CARD}a round pie chart with a thin golden slice and a small church icon, the hand-lettered words \"10% CHURCH\".",
    132: "{C} stares at an almost empty sack and a small pile of seed, with a thought bubble full of tiny question marks, plain cream background.",
    # 9. Alice, as crianças e a escola
    133: "{C} and {W} hold hands in front of their thatched house, hearts floating above them, bright spring day.",
    134: "{W} stirs a pot over the fire with one hand and balances a jug on her hip, a small child tugs her skirt, hens at her feet, steam rising.",
    135: "Small stick figure children herd a flock of white geese with a long stick, carry water buckets and scatter grain for hens in a busy farmyard.",
    136: "A small stick figure boy in an oversized apron chops a turnip with a big knife in a stone kitchen, a stern cook watches, a cloth bandage on his finger.",
    137: "{CARD}ten small stick figures in a row with one of them colored blue and wearing an apron, the hand-lettered words \"1 IN 10\".",
    138: "{C} and a small stick figure boy with a small book in his hand walk toward a small stone building with a cross, hopeful faces.",
    139: "{LORD} sits at a table stamping a parchment with a big wax seal while {C} stands in front of him holding his cap in both hands.",
    140: "{C} and a small stick figure boy stand in front of {R}, a clerk writes on a roll, a purse with three coins sits on the table.",
    141: "{CARD}a rolled parchment with a red wax seal, the hand-lettered words \"3 PENCE\".",
    142: "{CARD}a stack of small parchment scrolls with the hand-lettered number \"17\" and the words \"17 LICENCES\".",
    143: "A small stick figure boy with a book under his arm walks away along a long road from a village, {C} waves from the distance with a sad smile.",
    # 10. Quanto você vive
    144: "{C} looks at a long road stretching to the horizon with a big question mark above his head.",
    145: "{CARD}a small tombstone with the hand-lettered number \"30\" and a big red question mark.",
    146: "A simple wooden rocking cradle with a small baby stick figure tucked in a blanket, a soft golden glow, plain cream background.",
    147: "{CARD}a baby cradle icon with an arrow pointing to the hand-lettered number \"31\" and the words \"AT BIRTH\".",
    148: "{CARD}a seesaw with many small cradles on the heavy left side tipping it down and a few adult stick figures on the right side up in the air, the hand-lettered word \"AVERAGE\".",
    149: "An older stick figure man with grey hair, a walking stick and a wrinkled smile stands in front of his house surrounded by grandchildren, sunset.",
    150: "{C} lies under a blanket with a pale face and coughs, a small bowl of herbs beside him, grey mood.",
    151: "{C} spreads his empty hands toward the viewer with a questioning look and a question mark above his head, plain cream background.",
    152: "A stick figure official in a green hood writes a list on a long parchment roll next to a small house, a man's belongings piled on the ground, cloudy day.",
    153: "A small house with a field of ten rows, a brown mare with a foal, two cows, three sheep and a pink pig in the yard, neat arrangement.",
    154: "A round brass pot, a flat pan, two wooden chests with iron bands and a sack of oats arranged in a row, plain cream background.",
    155: "{C} stands next to his small pile of belongings with his hands on his hips, plain cream background.",
    156: "A hand-drawn parchment list with many items trailing off into a dotted line and a question mark at the bottom, a stick figure historian shrugs beside it.",
    157: "{CARD}a house, a field and a pot with an equals sign and a small coin purse, the hand-lettered words \"NET WORTH\".",
    # 11. A chuva
    158: "{C} stands in his field looking at the sky which is half sunny on the left and half dark clouds on the right, hands on hips.",
    159: "{S}On the left a golden field of ripe wheat under a shining sun, on the right a field of wheat flattened by rain under heavy grey clouds.",
    160: "A stick figure in a hooded cloak stands on a muddy road in heavy rain looking at the sky, thatched houses behind him, puddles everywhere.",
    161: "A field of pale soggy wheat with drooping stalks and wet heaps of hay under grey rain clouds.",
    162: "{CARD}two sheaves of thin sad wheat each with a red X, the hand-lettered numbers \"1315\" and \"1316\".",
    163: "{W} pours the last handful of seed grain from a nearly empty sack into a cooking pot, {K} watch with hungry eyes, dim room.",
    164: "{CARD}a row of ten cows with six of them faded to grey outlines and a sad face, the hand-lettered words \"6 IN 10 COWS\".",
    165: "A single ox stands alone in a field next to a wooden plough waiting for a team, sad face, grey sky.",
    166: "{CARD}a dark grey cloud over a small village, the hand-lettered number \"1348\" and the words \"BLACK DEATH\".",
    167: "{CARD}a round pie chart with a third to a half of the circle shaded dark grey, the hand-lettered words \"1/3 TO 1/2\".",
    168: "A quiet village with only a few thin lines of smoke rising from the thatched houses and many closed doors, a lonely stick figure stands at a crossroads, grey sunset.",
    169: "A wide green countryside with a handful of tiny stick figure farmers and huge open fields stretching all around them, golden light, hopeful mood.",
    170: "{C} stands with crossed arms and his chin up in front of {LORD}, who nervously holds out a bigger purse of coins, bright confident colors.",
    171: "{CARD}an official scroll with a red wax seal and a heavy weight pressing down a pile of coins, the hand-lettered words \"1351\" and \"WAGES CAPPED\".",
    172: "{CARD}a scroll torn in half with a thick red X, the hand-lettered word \"FAILED\".",
    173: "{C} hands a purse of coins to {LORD} at a small table and gets a rolled parchment with a green check in return, sunny and relaxed mood.",
    174: "A big crowd of determined stick figures with hoes and wooden staffs march along a road toward a walled city with towers and banners.",
    175: "{C} points a finger toward a dark rain cloud above his head with a serious face, plain cream background.",
    176: "{CARD}a tall stack of tiny stick figures standing on a tiny strip of land with rain falling on them, the hand-lettered words \"MORE PEOPLE, LESS LAND\".",
    177: "{CARD}a thin tightrope between a full wheat sheaf and an empty bowl with a tiny stick figure balancing on it, the hand-lettered words \"THIN MARGIN\".",
    178: "{C} climbs a small hill from a dark valley with a storm cloud on the left toward a bright sunrise on the right.",
    179: "{CARD}a small gold star with a dark cloud passing over it, the hand-lettered words \"GRIM PROGRESS\".",
    180: "A cheerful family of stick figures sits around a table loaded with bread, cheese, a roast bird and jugs, warm candlelight, everyone smiling.",
    181: "A modern stick figure in a T-shirt frowns at a paper tax form while {C} stands behind him in his tunic holding up a big pie chart with half of it colored red, smiling smugly.",
    182: "{CARD}a speech bubble with the hand-lettered words \"WHICH LIFE NEXT?\", a small hourglass and a small bell doodle.",
}


def prompt(n: int) -> str:
    t = P[n]
    for k, v in T.items():
        t = t.replace("{" + k + "}", v)
    t = t[0].upper() + t[1:]
    return f"{BASE} {BONECO} {t}" if "stick figure" in t else f"{BASE} {t}"


def cartao(n: int) -> bool:
    return P[n].startswith("{CARD}")
