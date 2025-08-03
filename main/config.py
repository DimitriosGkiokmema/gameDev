TILESIZE = 32

# Window
WIN_WIDTH = 35 * TILESIZE
WIN_HEIGHT = 20 * TILESIZE
FPS = 60

# Buttons
BTN_WIDTH = 100
BTN_HEIGHT = 30
BTN_X = WIN_WIDTH / 2 - BTN_WIDTH / 2
PLAY_BTN_Y = WIN_HEIGHT / 3
LEAD_BTN_Y = PLAY_BTN_Y + 2 * BTN_HEIGHT

# Leaderboard
NAME_X = WIN_WIDTH / 5
POINTS_X = WIN_WIDTH / 6 * 4
NAME_Y = WIN_HEIGHT / 4
BACK_BTN_WIDTH = 28
BACK_BTN_X = WIN_WIDTH - 100 - BACK_BTN_WIDTH
BACK_BTN_Y = 100

# Positions
SCORE_X = WIN_WIDTH - 4 * TILESIZE
SCORE_Y = TILESIZE / 2
GOLD_X = SCORE_X - 2 * TILESIZE
GOLD_Y = SCORE_Y
MANA_BAR_X = WIN_WIDTH / 2 - 4 * TILESIZE
MANA_BAR_Y = SCORE_Y

# Game Variables
TITLE = "Land of Lost"
# Layers
PLAYER_LAYER = 5
ENEMY_LAYER = 3
BLOCKS_LAYER = 2
GROUND_LAYER = 1
HEALTH_LAYER = 6
WEAPON_LAYER = 4

# Speed
PLAYER_STEPS = 3
ENEMY_STEPS = 1
PROJECTILE_STEPS = 5

# Health
PLAYER_HEALTH = 10
ENEMY_HEALTH = 6
FRUIT_HEAL = 1
PROJECTILE_DAMAGE = 1

# Mana
PLAYER_MANA_CAP = 5
PLAYER_MANA_REG_SPEED = FPS * 2
MANA_BAR_HEIGHT = TILESIZE / 2
MANA_BAR_WIDTH = 8 * TILESIZE

# Ranges
ENEMY_DETECTION_RANGE = 10

# Points
ENEMY_KILL_POINTS = 1

'''
| Symbol | Meaning                                       |
| ------ | --------------------------------------------- |
|   W    | ocean / deep water (impassable)               |
|   B    | rocky coastline / cliffs (slow or impassable) |
|   .    | grass / walkable ground                       |
|   R    | river / shallow water                         |
|   M    | mountain ridge                                |
|   T    | tree / forest tile                            |
|   H    | building (restaurant, house)                  |
|   P    | player start                                  |
|   E    | enemy                                         |
|   S    | fireball                                      |
|   C    | coin                                          |
|   F    | fruit                                         |
'''

# Maps
tilemap = [
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWW..........WWWW..............WWWW',
    'WWWWWW.............WWW...............WWW',
    'W.......E......F....WW.................W',
    'W...................WWW................W',
    'W...................WWWW...............W',
    'WWW............P...WWWWW...............W',
    'WWW......M.........WWWWW...............W',
    'W.......MMM......................T.....W',
    'W........M...............E......TTT....W',
    'W...E.......H..................TTT.....W',
    'W....................C.........T.......W',
    'W.......F..............................W',
    'W....T.........................F......BBBBBBB',
    'W....TT................S..............BBBBBBB',
    'W....TTT...............................W',
    'W....TTTTT......F......................W',
    'W....TTTTT.............................W',
    'W....TTTT..............................W',
    'W....TT......................W.........W',
    'W....TT........E......F.....WWW........W',
    'W....T.......................W.........W',
    'W...................W...........F......W',
    'W..................WWW..............WWWW',
    'WWW...............WWWWW..........WWWWWWW',
    'WWWWWW............WWWWW......WWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW'
]

mapTest = ['WBBBBBBBBBBW',
           'BWWWWWWWWWWB',
           'BWBBBBBBBBWB',
           'BWB...P..BWB',
           'BWBBBBBBBBWB',
           'BWWWWWWWWWWB',
           'WBBBBBBBBBBW'
           ]

# Colours
BLACK = (0, 0, 0)
OCEAN = (55, 138, 209)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (210, 211, 210)
MANA = (248, 245, 235)
DARK_RED = (166, 4, 4)