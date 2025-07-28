TILESIZE = 32

WIN_WIDTH = 35 * TILESIZE
WIN_HEIGHT = 20 * TILESIZE
FPS = 60

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

PROJECTILE_DAMAGE = 1

ENEMY_DETECTION_RANGE = 10

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
'''
tilemap = [
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'WBBBBBBBBBBBBBBBBBWWWWBBBBBBBBBBBBBBBBBW',
    'WB.................WWW................BW',
    'WB......E...........WW................BW',
    'WB...................WW...............BW',
    'WB..................WWWW..............BW',
    'WB.....S.......P....WWWW..............BW',
    'WB......MMMMM.......WWWW..............BW',
    'WB......MMMMM.........................BW',
    'WB......MMMMM............E............BW',
    'WB....................................BW',
    'WB..E.......H.........................BW',
    'WB....................................BW',
    'WB....................................BW',
    'WB....................................BW',
    'WB....................................BW',
    'WB...T................................BW',
    'WB...TT................S..............BW',
    'WB...TTT..............................BW',
    'WB...TTTTT............................BW',
    'WB...TTTTT............................BW',
    'WB...TTTT.............................BW',
    'WB...TT...............................BW',
    'WB...TT...............................BW',
    'WB...T........................H.......BW',
    'WB....................................BW',
    'WB....................................BW',
    'WB.............E......................BW',
    'WB....................................BW',
    'WB....................E...............BW',
    'WB....................................BW',
    'WB....................................BW',
    'WB..................W.................BW',
    'WB.................WWW................BW',
    'WB................WWWWW...............BW',
    'WBBBBBBBBBBBBBBBBBWWWWWBBBBBBBBBBBBBBBBW',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
]

BLACK = (0, 0, 0)
OCEAN = (55, 138, 209)
GREEN = (0, 255, 0)
RED = (255, 0, 0)