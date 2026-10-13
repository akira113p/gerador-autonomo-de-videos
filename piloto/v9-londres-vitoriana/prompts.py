"""Prompts de imagem do vídeo 9 (Londres vitoriana) para o Z-Image local, um por linha numerada do roteiro.md.

prompt() põe o estilo (BASE) e, se a cena tem stick figure, a descrição do boneco (BONECO).
{CARD} = cartão de fundo branco (palavras curtas, conferir a grafia).
Nada de lâmpada elétrica: Londres em 1854 tem lampiões a gás. A cólera aparece só como pessoas deitadas e a bomba
d'água, sem cadáveres. Objetos de época descritos pela forma (bomba de rua, ônibus a cavalo, locomotiva a vapor).
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
    "C": "the stick figure street seller in his thirties with short messy brown hair, a flat grey cloth cap, "
         "a red neckerchief, a brown waistcoat over a white shirt with rolled sleeves, baggy brown trousers and worn boots",
    "W": "his stick figure wife in a plain grey dress with a white apron and a dark shawl, her hair tied in a bun",
    "K": "two small stick figure children in patched grey clothes",
    "WG": "a small stick figure girl in a patched brown dress and a thin shawl, carrying a flat wicker basket full of "
          "green watercress bunches",
    "SN": "the stick figure doctor John Snow, a serious man in a dark frock coat and a tall black top hat, "
          "with a rolled paper map under his arm",
    "RW": "the stick figure curate Henry Whitehead in a long black coat with a white clerical collar and a black hat",
    "CH": "the stick figure civil servant Edwin Chadwick, a serious man with a high forehead in a dark frock coat",
    "FA": "the stick figure scientist Michael Faraday, an older man with grey side whiskers in a dark coat and a hat, "
          "holding a small notebook",
    "HA": "the stick figure doctor Arthur Hassall in round glasses and a dark coat",
    "MH": "the stick figure journalist Henry Mayhew in a dark coat and a top hat, holding a notebook and a pencil",
    "BZ": "the stick figure engineer Joseph Bazalgette, a man with a mustache in a dark-blue frock coat and a top hat, "
          "holding rolled blueprints",
    "DI": "the stick figure politician Benjamin Disraeli, a man with a curl of black hair on his forehead and a pointed goatee, "
          "in a black frock coat",
    "MP": "a stick figure gentleman in a black frock coat and a tall top hat holding a handkerchief over his nose",
    "PO": "a stick figure policeman in a long dark-blue coat with brass buttons and a tall black hat",
    "PP": "a sneaky stick figure pickpocket boy in a floppy cap and a ragged jacket",
    "GM": "a stick figure gentleman in a black frock coat and a tall top hat",
    "PUMP": "an old cast-iron street water pump with a long curved iron handle on top and a spout, standing on a cobblestone corner",
    "STUMP": "an old cast-iron street water pump whose long handle is gone, only a short stump on top, standing on a cobblestone corner",
    "LAMP": "a tall black iron street lamp with a glass lantern on top holding a small yellow gas flame",
    "BARROW": "a wooden two-wheeled hand barrow piled with apples and cabbages",
    "BUS": "a tall boxy two-level wooden horse-drawn bus painted red, with seats on the roof, a ladder at the back and two horses in front",
    "TRAIN": "a small black steam locomotive with a tall chimney pulling brown wooden carriages",
    "CARD": CARTAO,
    "S": "Split screen divided by a vertical black dashed line. ",
}

P = {
    # 0. Abertura
    1: "{C} holds up a glass of clear water to the light and squints at it curiously, plain cream background.",
    2: "{CARD}a simple skyline of rooftops with chimneys and one big domed cathedral, the hand-lettered black capital words \"LONDON 1854\" above it.",
    3: "A wide muddy-brown river with a stone bridge and a few sailing barges, a brick building with a tall chimney on the bank and a thick pipe running from the river into the building, hazy morning light.",
    4: "A big round sewer pipe pouring brown water into the same wide river, a small rowing boat nearby, brick houses along the bank, murky brown water.",
    5: "{CARD}a huge crowd of tiny stick figure dots filling a big circle shaped like a city map, the hand-lettered black capital words \"BIGGEST CITY ON EARTH\".",
    6: "A busy harbor on the river crowded with tall sailing ships and small steam tugboats with chimneys, brick warehouses and cranes on the quay, golden light.",
    7: "A stick figure lord in a top hat and a stick figure queen in a small gold crown and a wide dress stand side by side, a thick red X drawn over both of them, plain cream background.",
    8: "{C} pushes {BARROW} along a cobbled street, {W} and {K} walking behind him, tall brick houses, {LAMP} on the corner, hazy morning light.",
    9: "{CARD}three small icons in a row: a few copper coins, a folded map with red dots, and a street water pump with only a short stump on top, the hand-lettered words \"COINS, MAP, PUMP\".",
    10: "A grand hall with tall windows and long heavy curtains soaked and dripping with white liquid, stick figure gentlemen in top hats hold handkerchiefs over their noses, green wavy stink lines in the air.",
    11: "{CARD}the hand-lettered black capital words \"VICTORIAN LONDON\" with a small street lamp and a top hat doodle.",
    12: "A wide panorama of London rooftops packed with chimneys and a big domed cathedral on a hill, a long river curving through the city, smoky yellow-grey sky.",
    # 1. A cidade mais cheia
    13: "{CARD}a census paper form on a clipboard with a pencil and rows of tiny tally marks, a big hand-lettered \"2 MILLION+\" and the year \"1851\" above it.",
    14: "{CARD}three city silhouettes side by side growing from small to large with an upward arrow, the hand-lettered words \"+20% EVERY 10 YEARS\".",
    15: "A huge palace made entirely of glass and iron with a high curved glass roof, standing in a green park, flags on top, bright sunshine, tiny crowds walking toward it.",
    16: "Inside a gigantic glass hall with tall green trees growing under the curved glass roof, hundreds of tiny stick figure visitors in top hats and bonnets walking between display tables, warm light.",
    17: "A stick figure attendant stands at a small wooden door next to a coin box with a sign reading \"1 PENNY\", a line of stick figure visitors in top hats shifting from foot to foot while waiting, bright interior.",
    18: "{CARD}a big copper penny coin with a small white toilet icon next to it, the hand-lettered words \"800,000 PAID\".",
    19: "{CARD}a small gravestone with the hand-lettered number \"40\" and a big red question mark above it.",
    20: "A hand-drawn bar chart with many very short bars on the left, each topped with a tiny cradle, and a few tall bars on the right, a dashed horizontal line across the middle, plain cream background.",
    21: "A smiling old stick figure with white hair and a walking stick sitting on a park bench, a banner behind him reading \"60\", sunny day.",
    22: "{S}on the left a tall elegant house with a smiling stick figure gentleman in a top hat at the door, on the right a tiny crowded attic room with a worried stick figure in patched clothes.",
    23: "{CH} sits at a big desk piled with papers and a thick report, writing with a quill, a map of Britain with little pins hanging on the wall behind him.",
    24: "{CARD}two vertical bars side by side, a tall green one labeled \"RICH\" and a bar noticeably shorter labeled \"POOR\", a double arrow between their tops with the hand-lettered words \"20 YEARS\".",
    25: "A heavy bag of gold coins on one pan and a big pocket watch on the other pan of a balance scale, perfectly level, plain cream background.",
    26: "{C} points at himself with one thumb and a nervous smile, a smart stick figure gentleman in a top hat and with a briefcase looks down at him from the right, plain cream background.",
    # 2. O seu quarto
    27: "{C} climbs a narrow creaky wooden staircase inside a tall brick house with peeling wallpaper, a lit candle in his hand, seen from below.",
    28: "{C} and {W} and {K} lie together in one small attic room on a straw mattress under a thin blanket, a candle on a crate, a tiny window with rooftops outside.",
    29: "A cutaway view of a tall brick house with every floor packed with small rooms, each room full of beds, boxes and families, the top attic room cozy with a candle.",
    30: "A long narrow room with rows of narrow beds side by side, each with a thin blanket and a sleeping stick figure, a single hanging lamp, wooden floor.",
    31: "{CARD}a large narrow bed with the hand-lettered words \"3 PENCE\" and a small child bed next to it with the hand-lettered words \"1.5 PENCE\", the words \"PER NIGHT\" below.",
    32: "{CARD}a row of small house icons with a magnifying glass over them and a tall black policeman hat next to them, the hand-lettered number \"3,300\".",
    33: "{CARD}a huge cluster of tiny beds filling a circle, the hand-lettered number \"50,000\" and the words \"EVERY NIGHT\".",
    34: "A tiny room packed from wall to wall with dozens of stick figures lying and sitting on the floor, men, women and children squeezed together, a single small window, seen from above.",
    35: "{S}on the left a small plain living room with a sofa, a coffee table and a floor lamp and one stick figure sitting on the sofa, on the right the same room packed with thirty-seven tiny stick figures.",
    36: "A stick figure gentleman in a top hat reads a newspaper alone in a big quiet room with a velvet armchair and a tall bookshelf, a closed door behind him, a happy relaxed face.",
    37: "{C} walks down a narrow street carrying a metal bucket toward {PUMP}, tall brick houses on both sides.",
    38: "A stick figure lamplighter in a long coat lifts a long pole to light {LAMP}, cobblestone street at dusk, warm yellow glow.",
    39: "{W} puts a lump of black coal into a small iron fireplace in the dark room, orange glow on her face, {K} sitting nearby, thin smoke rising to the chimney.",
    # 3. O dinheiro
    40: "{CARD}a messy tangle of coins of different sizes with confused question marks around them, the hand-lettered word \"CHAOS\".",
    41: "{CARD}twelve small copper penny coins in a grid on the left, an equals sign, and one big silver coin on the right, the hand-lettered words \"12 PENCE = 1 SHILLING\".",
    42: "{C} scratches his head and stares with a confused face at a pile of coins of different sizes on a wooden table, question marks floating around him.",
    43: "{CARD}a hand-drawn calculator with the hand-lettered text \"x 140\" on its screen and a small copper coin next to it.",
    44: "{CARD}a copper penny coin, an arrow and the hand-lettered text \"$1\", below it a silver shilling coin, an arrow and the hand-lettered text \"$9\".",
    45: "A stick figure historian in round glasses and a tweed jacket shakes his head at a calculator on a desk, a big loaf of bread and a small flat television on the desk.",
    46: "{C} holds up a single big copper penny coin to the light with a curious face, plain cream background.",
    47: "Four bunches of green watercress tied with string lying on a wicker basket next to a single big copper penny coin, plain cream background.",
    48: "A tiny shabby stage in a pub back room with a red curtain, a stick figure clown dancing on it in front of a small cheering crowd, a copper penny coin floating above.",
    49: "{CARD}a copper penny coin beside a small wooden toilet cubicle door, the hand-lettered text \"1851\".",
    50: "{CARD}a narrow bed and three copper penny coins stacked beside it, the hand-lettered words \"3 PENCE\".",
    51: "{CARD}two stacks of silver shilling coins, a short stack labeled \"10\" and a tall stack labeled \"30\", the words \"PER WEEK\" below.",
    52: "{CARD}a snowflake next to a short stack of silver coins, the hand-lettered number \"8\" and the words \"JAN, FEB\".",
    53: "{C} stands miserable in heavy rain behind {BARROW} full of plums, a dripping cap, passers-by hurry away under umbrellas, gloomy grey sky.",
    # 4. O trabalho
    54: "{C} yawns at a small high window of a tall brick house, rooftops below under a dark blue pre-dawn sky with a crescent moon and a few stars.",
    55: "{C} pushes an empty wooden barrow down a dark cobbled street, {LAMP} glowing, long shadows, cold blue light.",
    56: "{S}on the left an open market square with piles of fruit and vegetables in baskets and stick figure sellers shouting, on the right a fish market by the river with tables of silver fish.",
    57: "{C} stands behind {BARROW}, shouting with his hands cupped around his open mouth, strangers hurry past him on a busy cobbled street.",
    58: "A crowd of tiny stick figures each pushing a small barrow, filling a London street from corner to corner, many caps and red neckerchiefs, seen from above.",
    59: "{MH} sits on a stool and listens, writing in his notebook, to a stick figure street seller who talks with a big gesture, an open book with a drawing of a street scene lies beside them.",
    60: "Two stick figure street sellers in neckerchiefs whisper to each other with their hands cupped around their mouths, a nosy policeman in the background, speech bubbles full of swirly scribbles.",
    61: "{CARD}a speech bubble with the hand-lettered word \"BOY\" and a curved arrow flipping it into another speech bubble with the hand-lettered word \"YOB\".",
    62: "{C} raises one eyebrow at the viewer, plain cream background.",
    63: "A stick figure in a ragged coat with a wooden bucket and a small scoop bends over a cobbled street where a small dog stands, a leather tannery with hides hung to dry in the background.",
    64: "{CARD}a hand-drawn job advertisement paper with the hand-lettered word \"JOB\" and a small bucket icon, a big green check mark.",
    65: "Three small stick figure children with rolled-up trousers wade in dark mud on a river shore at low tide, searching with their hands, a stone bridge and ships in the background.",
    66: "A stick figure in a long coat and tall boots wades through a dark brick sewer tunnel holding a lantern on a pole, water up to his knees, a small coin glinting in the water.",
    67: "{WG} stands in a London street holding up a bunch of watercress with a serious face, tall brick houses behind her.",
    68: "{WG} walks alone through a cold blue pre-dawn street with her basket, a distant street lamp, a market far away.",
    69: "{CARD}three copper penny coins in a row and a bigger silver shilling coin with a star, the hand-lettered text \"3-4 PENCE\" under the coins and \"1S 6D\" under the silver one.",
    70: "{WG} puts her hands on her hips with a defiant face, a speech bubble above her showing a tall woman's silhouette with the hand-lettered number \"20\".",
    71: "An empty playground with a swing, a ball and a hoop, and {WG} walks away from it toward a market with her basket.",
    72: "A small soot-black stick figure boy climbing up inside a narrow brick chimney, only his head and arms visible, one hand holding a brush, sooty smudges on the bricks.",
    73: "{CARD}a scroll of paper with a wax seal and the hand-lettered text \"LAW 1840\", beside a small chimney with a thick red X over it.",
    74: "{CARD}a hand-drawn timeline from left to right with a small chimney at the left end and a green check mark at the right end, the hand-lettered text \"1875\".",
    75: "An empty school classroom with rows of wooden desks and a chalkboard, a small stick figure child outside the window carrying a heavy basket.",
    # 5. Comida e névoa
    76: "{C} and {W} and {K} sit around a small wooden table in the morning light, a loaf of bread, a teapot and three cups on it, a small piece of butter on a plate.",
    77: "{W} squints suspiciously at a slice of bread through a magnifying glass, a worried face, plain cream background.",
    78: "{HA} looks through a brass microscope at a tiny sample, a table crowded with jars of coffee beans, tea leaves and flour, window light.",
    79: "{CARD}a microscope and a tall stack of small paper sample packets, the hand-lettered number \"2,500+\".",
    80: "A big round magnifying-lens circle showing a small pile of brown ground powder with odd little grains and specks mixed into it, plain cream background.",
    81: "A stick figure lawmaker in a top hat stamps a paper with a big stamp on a wooden desk, a stack of food packages beside it.",
    82: "{C} steps out of a doorway onto a foggy London street, coughing with a hand over his mouth.",
    83: "A row of London rooftops with dozens of brick chimneys all puffing thick dark smoke, a tall factory chimney in the middle, a grey-brown sky.",
    84: "Thick yellow-brown fog hanging low over a wide river, the outlines of a stone bridge and chimneys fading into the mist.",
    85: "{S}on the left a big bowl of thick green pea soup with a spoon standing in it and steam rising, on the right a street in thick yellow-green fog.",
    86: "A stick figure author with a beard and a dark coat looks out of a window at thick yellow fog, an open book, a pen and an ink bottle on the desk beside him.",
    87: "{CARD}a black lump of coal, an arrow, and a thick grey smoke cloud, the hand-lettered words \"COAL SMOKE\".",
    # 6. A água
    88: "{C} holds up a glass of water to the light and squints suspiciously, plain cream background.",
    89: "{CH} points at a big drawing of a filthy street with a pile of garbage, a thick report in his other hand, a serious face.",
    90: "A cutaway view of a house with a clean water pipe going into the kitchen and an egg-shaped sewer pipe leaving underneath toward a big main sewer under the street, bright blueprint colors.",
    91: "A cutaway of a street: an overflowing brick cesspool full of brown liquid under a house, a brown stream through a small drain into a bigger sewer pipe, and then pouring into a river, arrows showing the flow.",
    92: "A big pipe taking water from a river into a brick waterworks building with a tall chimney, smaller pipes leading from it to rows of houses, blue arrows.",
    93: "{FA} stands on the deck of a small steamboat on a brown river, a bridge behind him, the boat's chimney puffing smoke.",
    94: "{FA} leans over the side of the steamboat and drops small white pieces of paper into the brown water, ripples spreading.",
    95: "{CARD}a side view of a river of brown water with a small white paper square sinking and vanishing right below the surface, a small ruler marking \"1 INCH\".",
    96: "{CARD}an old newspaper page with a drawing of a brown river and a bold hand-lettered headline \"THE THAMES\".",
    97: "A wide brown river with a stone bridge, dark green stink waves rising from the water, a small steamboat on it, stick figure passengers holding handkerchiefs to their noses.",
    98: "{CARD}a paper law with a seal, a blue wavy line with an arrow pointing upriver from a city to the countryside, the hand-lettered text \"1852\".",
    99: "{CARD}two calendar pages side by side, the left one labeled \"1854\" with a brown water drop, the right one labeled \"1855\" with a clear blue water drop.",
    100: "{SN} looks at the viewer with a determined face, plain cream background.",
    # 7. Broad Street
    101: "A group of stick figure doctors in dark coats and top hats stand around a cloud of green smell rising from a dirty gutter, one holds a handkerchief to his nose, another points at the cloud.",
    102: "A narrow dirty street with a pile of rubbish and a gutter, green wavy smell lines rising, a stick figure sniffs with a disgusted face.",
    103: "{CARD}a tall hand-drawn bar with a small black ribbon on top, the hand-lettered number \"14,000\" above it and the years \"1848-49\" below.",
    104: "{CARD}a hand-drawn shorter bar with a small black ribbon on top, the hand-lettered number \"10,000+\" above it and the years \"1853-54\" below.",
    105: "{C} walks down a narrow street carrying a bucket, tall brick houses, {PUMP} on the corner, a small stone street sign reading \"BROAD STREET\".",
    106: "{CARD}a calendar page with the hand-lettered text \"31 AUGUST 1854\" circled in red.",
    107: "{CARD}a circle drawn around a small street corner with a tiny pump icon in the middle, the hand-lettered text \"500+ IN 10 DAYS\".",
    108: "{SN} stands on a street looking at the viewer with one finger raised and a thoughtful face, {PUMP} in the background.",
    109: "{SN} holds a small glass bottle of clear liquid beside a stick figure queen in a small gold crown resting in a big royal bed, a glass of water on the bedside table.",
    110: "{CARD}two arrows leaving a sick stick figure: a wavy air arrow crossed out by a red X, and a green arrow through a water drop, the hand-lettered words \"WATER, NOT AIR\".",
    111: "{SN} writes in a notebook while a worried {W} talks to him at the door of a tall brick house.",
    112: "A hand-drawn map of a few streets with many red dots clustered tightly around one small blue pump icon, cream paper, simple bold lines.",
    113: "A big grey brick building with a small courtyard well and its own pump, a crowd of stick figures in plain grey clothes standing safe inside, a green check mark in the sky.",
    114: "Stick figure brewery workers in aprons roll wooden barrels and drink foamy beer from big mugs between big copper vats, a green check mark above.",
    115: "A horse-drawn cart carries a big wooden barrel of water out of a narrow street toward a pretty house on a green hill, a stick figure widow in a black bonnet and long black dress waits at the gate.",
    116: "Two stick figures, an older woman in a black dress and a young woman in a grey dress, lie resting in two narrow beds in a dim room, a glass of water on the table between them, pale light through the window.",
    117: "A stick figure man in a long coat holds a long curved iron pump handle in his hands next to {STUMP}, a small crowd watching.",
    118: "A stick figure in a flowing cape blows a big golden trumpet in a heroic pose, sparkling stars and confetti around him, a small grey cloud above his head.",
    119: "A street where stick figure families carry bundles and boxes and walk away down the road, carts loaded with furniture heading out, shuttered windows, grey light.",
    120: "{RW} walks along a street holding a notebook and glancing at the houses, a church tower behind him.",
    121: "{RW} crosses his arms with a doubtful frown while {SN} unrolls a map in front of him, plain cream background.",
    122: "A cutaway view of an old brick house cellar where a bowl of dirty water is poured into a cesspool pit right next to a stone-lined well under {PUMP}, only a few feet apart.",
    123: "A cutaway of the ground under {PUMP}: a crack in the brick wall of the well with brown water dripping in from the cesspool beside it, arrows showing the leak.",
    124: "{CARD}two water taps side by side, one pouring brown water and one pouring clear water, a crowd of tiny dots below, the hand-lettered number \"300,000\".",
    125: "{CARD}two vertical bars, a very tall brown bar and a very short blue bar, the hand-lettered words \"MANY TIMES MORE\".",
    126: "A board of stick figure officials in black coats and top hats sit around a long table, one covers his ears with his hands, another waves away a paper, stiff stubborn faces.",
    127: "{CARD}a calendar page with the hand-lettered text \"JUNE 1858\" and a small black ribbon, a small top hat resting on top.",
    128: "A medical journal open on a desk with a short column crossed by a big red hand-drawn correction mark, the hand-lettered text \"2013\".",
    # 8. Como se locomover
    129: "A close-up of a pair of muddy worn boots walking on wet cobblestones, plain background above.",
    130: "{BUS} on a busy street, stick figure passengers in top hats and bonnets riding on top, a conductor hanging at the back.",
    131: "{CARD}a route line from the word \"PADDINGTON\" to the word \"BANK\" with a small horse bus icon and the year \"1829\".",
    132: "{CARD}the single hand-lettered word \"OMNIBUS\" in big clear letters with an arrow to the words \"FOR ALL\" below.",
    133: "A stable with many horses standing in stalls, one tired horse yawning, a horse bus parked outside, a stick figure stable hand with a bucket.",
    134: "A row of identical red horse buses lined up neatly in a yard, a stick figure manager with a clipboard stands in front, tidy and proud.",
    135: "{CARD}a calendar page with the hand-lettered text \"10 JAN 1863\" and a small train coming out of a tunnel arch.",
    136: "{CARD}a short route line between two dots, a small steam train on the line, and a crowd of tiny dots with the hand-lettered number \"38,000\".",
    137: "{TRAIN} coming out of a dark brick tunnel arch, thick grey smoke filling the tunnel mouth and the station platform, stick figure passengers coughing.",
    138: "A side view of a deep trench in a city street with brick walls being built, a big brown stream bursting through the side wall, stick figure workers running away, wooden planks.",
    # 9. Diversão e crime
    139: "{C} leaves work in the evening with {BARROW} and a few coins in his hand, an orange sky, street lamps being lit along the street, tired but smiling.",
    140: "{CARD}a single copper penny coin with an arrow to a small theatre curtain, the hand-lettered words \"PENNY GAFF\".",
    141: "A cramped pub back room turned into a theatre with a small wooden stage, a stick figure clown and a stick figure highwayman with a black mask and a wide hat acting on it, a noisy crowd with mugs, a lantern.",
    142: "A stick figure reformer in a black coat and white collar wags a finger at a group of stick figure children peeking through a theatre door.",
    143: "A big music hall with gas chandeliers, a singer in a fancy dress on a stage, an audience at long tables with mugs, a balcony, warm light.",
    144: "{PO} stands proudly on a cobbled corner under {LAMP}.",
    145: "{CARD}a small group of tall black policeman hats on the left, a huge crowd of tiny dots on the right, the hand-lettered number \"5,600\".",
    146: "{PP} slides his hand into the coat pocket of {GM} who is busy reading a newspaper on a crowded street, {C} watches wide-eyed from behind his barrow.",
    147: "A grand piano with its legs wrapped in frilly cloth skirts, a stick figure lady in a long dress stands next to it, plain cream background.",
    148: "A stick figure traveler in a blue coat writes in a thick travel book, a stick figure lady behind him winks at the viewer and hides a laugh behind her fan.",
    149: "{CARD}a timeline with two dots, the left dot labeled \"1854\" and a far dot on the right labeled \"1888\", a long arrow between them with the words \"34 YEARS LATER\".",
    # 10. O Grande Fedor
    150: "{CARD}a hand-drawn calendar page flying forward with the hand-lettered text \"SUMMER 1858\" and a big hot sun.",
    151: "A blazing yellow sun over a low river with cracked dry mud banks and a lonely boat resting on the mud, wavy heat lines.",
    152: "A wide brown muddy riverbank under a hot sun covered with brown sludge and flies, green wavy stink lines rising, a bridge in the distance.",
    153: "A big long stone Gothic palace with many pointed spires and tall windows right on the edge of a brown river, green wavy stink lines rising toward it.",
    154: "Stick figure servants on tall ladders hang heavy curtains soaked in white liquid at tall windows of a grand hall, buckets on the floor, lawmakers in top hats hold handkerchiefs over their noses.",
    155: "A group of stick figure lawmakers in top hats carry suitcases and boxes out of a palace door, a cart loaded with papers, green smell clouds behind them.",
    156: "{DI} stands at a wooden podium with a raised fist, dramatic pose, green stink lines in the air.",
    157: "A giant hand-drawn nose with green wavy stink lines curling around it, plain cream background.",
    158: "{FA} shouts through a big megaphone at a crowd of stick figure lawmakers in top hats who ignore him, one reads a newspaper, another looks away.",
    159: "A giant green smell cloud pushing through a window into a grand hall, stick figure lawmakers jump up from their seats in panic, papers flying.",
    160: "{CARD}a stack of gold coins with the hand-lettered text \"3 MILLION POUNDS\" and a small house icon with a coin arrow.",
    161: "{BZ} smiles confidently in front of a huge drawing of a sewer map on a table, plain cream background.",
    162: "{CARD}a hand-drawn underground map showing thick sewer pipes branching like a tree, the hand-lettered numbers \"82 MILES\" and \"1,100 MILES\".",
    163: "{CARD}a huge pile of red bricks forming a tall wall with the hand-lettered number \"318 MILLION\".",
    164: "A cutaway of a huge brick-arched sewer tunnel underground leading to a big pumping building with a tall chimney at the edge of the city, arrows showing the flow, bright blue and brown colors.",
    165: "A grand pumping station with tall arched windows and a tall chimney, a stick figure prince in a sash and top hat pulling a big lever, a crowd of stick figures in top hats clapping, flags.",
    166: "{BZ} stands in front of a blackboard where a big green stink cloud is drawn with an arrow pointing at a sewer pipe, he winks at the viewer.",
    167: "{S}on the left a brown sewage pipe leading away to the right, on the right clear blue water pouring from a tap into a glass, a green check mark above.",
    168: "{CARD}a green check mark and a red X side by side, the hand-lettered words \"RIGHT FIX, WRONG REASON\".",
    169: "{S}on the left a Victorian brick sewer tunnel under construction with stick figure workers, on the right the same tunnel today with a stick figure worker in an orange vest and a hard hat.",
    # 11. Fecho
    170: "{C} stands on a street at dusk with a gas lamp, hands on hips, looking at the viewer with a questioning raised eyebrow, faint fog.",
    171: "{CARD}a calendar page with the hand-lettered text \"1866\" and a simple city map with an arrow pointing to its east side.",
    172: "{CARD}a hand-drawn tall bar with the hand-lettered number \"5,000+\" and a water tap with a brown drip, the year \"1866\".",
    173: "A stick figure historian in glasses and a tweed jacket stands at a lectern pointing at a timeline on a chalkboard.",
    174: "{C} looks at the viewer thoughtfully with a finger to his chin, plain cream background.",
    175: "{CARD}three icons in a row: a thick report, a white paper card and a folded map with red dots, the hand-lettered words \"THREE WARNINGS\".",
    176: "{S}on the left a crowded poor street with sick stick figures resting on doorsteps, ignored, on the right a grand hall where lawmakers in top hats jump up holding their noses.",
    177: "{C} shrugs with open palms and a half smile, plain cream background.",
    178: "A bird's-eye view of a green smell cloud rising from a crowded slum street and floating over a wide river toward a grand palace, a stick figure in a top hat in a palace window holding his nose.",
    179: "A big white porcelain toilet with a flower wreath around it, and {BZ} bowing and tipping his top hat toward it, plain cream background.",
    180: "A single glass of clear water on a wooden table, bright sunlight shining through it, plain cream background.",
    181: "{CARD}five small icons in a row: a doctor's top hat, a priest's white collar, a scientist's flask, a rolled blueprint, and a green smell cloud, the hand-lettered words \"AND ONE SMELL\".",
    182: "{CARD}a speech bubble reading \"WHICH DAY IN HISTORY NEXT?\" and a small calendar with a question mark, plus a small subscribe bell doodle.",
}


def prompt(n: int) -> str:
    t = P[n]
    for k, v in T.items():
        t = t.replace("{" + k + "}", v)
    t = t[0].upper() + t[1:]
    return f"{BASE} {BONECO} {t}" if "stick figure" in t else f"{BASE} {t}"


def cartao(n: int) -> bool:
    return P[n].startswith("{CARD}")
