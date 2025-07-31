TILESIZE = 32

# Window
WIN_WIDTH = 35 * TILESIZE
WIN_HEIGHT = 20 * TILESIZE
FPS = 60

# Positions
SCORE_X = WIN_WIDTH - 4 * TILESIZE
SCORE_Y = TILESIZE / 2
GOLD_X = SCORE_X - 2 * TILESIZE
GOLD_Y = SCORE_Y

# Game Variables
PLAYER_LAYER = 5
ENEMY_LAYER = 3
BLOCKS_LAYER = 2
GROUND_LAYER = 1
HEALTH_LAYER = 6
WEAPON_LAYER = 4

PLAYER_STEPS = 3
ENEMY_STEPS = 1
PROJECTILE_STEPS = 5

ISLAND_SIDE_EDGE = 2
ISLAND_TB_EDGE = 3

PLAYER_HEALTH = 10
ENEMY_HEALTH = 6
FRUIT_HEAL = 1

PROJECTILE_DAMAGE = 1

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
|   S    | sword                                         |
|   C    | coin                                          |
|   F    | fruit                                         |
'''
tilemap = [
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'WBBBBBBBBBBBBBBBBBWWWWBBBBBBBBBBBBBBBBBW',
    'WB.................WWW................BW',
    'WB......E......F....WW................BW',
    'WB...................WW...............BW',
    'WBB.................WWWW..............BW',
    'WWWB...S.......P....WWWW..............BW',
    'WWWB....MMMMM.......WWWW..............BW',
    'WBB.....MMMMM.........................BW',
    'WB......MMMMM............E............BW',
    'WB....................................BW',
    'WB..E.......H.........................BW',
    'WB...................C................BW',
    'WB......F.............................BW',
    'WB....................................BW',
    'WB....................................BW',
    'WB...T.........................F......BW',
    'WB...TT................S..............BW',
    'WB...TTT..............................BW',
    'WB...TTTTT............................BW',
    'WB...TTTTT............................BW',
    'WB...TTTT.............................BW',
    'WB...TT...............................BW',
    'WB...TT...............F...............BW',
    'WB...T........................H.......BW',
    'WB....................................BW',
    'WB....................................BW',
    'WB.............E......................BW',
    'WB.....F..............................BW',
    'WB....................E...............BW',
    'WB....................................BW',
    'WB....................................BW',
    'WB..................W...........F.....BW',
    'WB.................WWW................BW',
    'WB................WWWWW...............BW',
    'WBBBBBBBBBBBBBBBBBWWWWWBBBBBBBBBBBBBBBBW',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW'
]

tilemapTest = ['WBBBBBBBBBBW',
           'BWWWWWWWWWWB',
           'BWBBBBBBBBWB',
           'BWB...P..BWB',
           'BWBBBBBBBBWB',
           'BWWWWWWWWWWB',
           'WBBBBBBBBBBW'
           ]

BLACK = (0, 0, 0)
OCEAN = (55, 138, 209)
GREEN = (0, 255, 0)
RED = (255, 0, 0)