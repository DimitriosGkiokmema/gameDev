TILESIZE = 32

# Window
WIN_WIDTH = 35 * TILESIZE
WIN_HEIGHT = 20 * TILESIZE
FPS = 60

# Main Menu
BTN_WIDTH = 100
BTN_HEIGHT = 30
BTN_X = WIN_WIDTH / 2 - BTN_WIDTH / 2
PLAY_BTN_Y = WIN_HEIGHT / 3
LEAD_BTN_Y = PLAY_BTN_Y + 2 * BTN_HEIGHT
CONT_BTN_Y = LEAD_BTN_Y + 2 * BTN_HEIGHT

# Leaderboard
NAME_X = WIN_WIDTH / 5
POINTS_X = WIN_WIDTH / 6 * 4
NAME_Y = WIN_HEIGHT / 4
BACK_BTN_WIDTH = 28
BACK_BTN_X = WIN_WIDTH - 100 - BACK_BTN_WIDTH
BACK_BTN_Y = 100
BOARD_X = 100
BOARD_Y = 100
BOARD_HEIGHT = WIN_HEIGHT - 200
BOARD_WIDTH = WIN_WIDTH - 200

# Pause Menu
PAUSE_X = WIN_WIDTH / 3
PAUSE_Y = WIN_HEIGHT / 4
PAUSE_WIDTH = WIN_WIDTH / 3
PAUSE_HEIGHT = WIN_HEIGHT / 2
PAUSE_CLOSE_X = PAUSE_X + PAUSE_WIDTH - BACK_BTN_WIDTH
RESUME_X = WIN_WIDTH / 2 - 35
RESUME_Y = PAUSE_Y + 2 * BTN_HEIGHT
QUIT_Y = RESUME_Y + 2 * BTN_HEIGHT

# Controls
CONTROL_X = WIN_WIDTH / 2 - 35
CONTROL_Y = WIN_HEIGHT / 3
KEY_X = PAUSE_X + BTN_WIDTH
KEY_Y = CONTROL_Y + 2 * BTN_HEIGHT

# Positions
SCORE_X = WIN_WIDTH - 4 * TILESIZE
SCORE_Y = TILESIZE / 2
GOLD_X = SCORE_X - 2 * TILESIZE
GOLD_Y = SCORE_Y
MANA_BAR_X = WIN_WIDTH / 2 - 4 * TILESIZE
MANA_BAR_Y = SCORE_Y

# Game Variables
TITLE = "Land of The Lost"
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
BOSS_HEALTH = ENEMY_HEALTH * 5
FRUIT_HEAL = 1
PROJECTILE_DAMAGE = 1

# Mana
PLAYER_MANA_CAP = 5
PLAYER_MANA_REG_SPEED = FPS * 2
MANA_BAR_HEIGHT = TILESIZE / 2
MANA_BAR_WIDTH = 8 * TILESIZE

# Ranges
ENEMY_DETECTION_RANGE = 10
BOSS_DETECTION_RANGE = 15

# Points
ENEMY_KILL_POINTS = 1
BOSS_KILL_POINTS = 5

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
|   Z    | boss                                          |
|   S    | fireball                                      |
|   C    | coin                                          |
|   F    | fruit                                         |
'''

# Maps
tilemap = [
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWW..........WWWW..............WWWWWWWWWWWWWWWWWW.......WWWWW......WW...WWW',
    'WWWWWW.............WWW...............WWWWWWWWWWWWWWWW.........WWW........W....WW',
    'W.......E......F....WW.................WWWWWWWWWWWW............WW........WW...WW',
    'W...................WWW.................WWWWWWWWWW.............W..........W..WWW',
    'W...................WWWW.................WWWWWWWW.........................W.WWWW',
    'WWW............P...WWWWW..................WWWWW...........................WWWWWW',
    'WWW......M.........WWWWW.................WWWWWWW.......................WWWWWWWWW',
    'W.......MMM......................T.......WWWWW.......................WWWWWWWWWWW',
    'W........M...............E......TTT.....WWWWWW..............WWW....WWWWWWWWWWWWW',
    'W...E.......H..................TTT.....WWWWWW...............WWWWWWWWWWWWWWWWWWWW',
    'W....................C.........T.......WWWWWWW..............WWWW....WWWWWWWWWWWW',
    'W.......F..............................WWWWW.............................WWWWWWW',
    'W....T.........................F......BBBBBBB...............................WWWW',
    'W....TT................S..............BBBBBBB.................................WW',
    'W....TTT...............................WWWWW..................................WW',
    'W....TTTTT......F......................WWWWWWWW..............W...............WWW',
    'W....TTTTT.............................WWWWWWW..............WWW...........Z...WW',
    'W....TTTT..............................WWWWWW................W.................W',
    'W....TT......................W.........WWWWWWW................................WW',
    'W....TT........E......F.....WWW........WWWWWWWW.............................WWWW',
    'W....T.......................W.........WWWWWWWWWWWW.......................WWWWWW',
    'W...................W...........F......WWWWWWWWWW.....................WWWWWWWWWW',
    'W..................WWW..............WWWWWWWWW......................WWWWWWWWWWWWW',
    'WWW...............WWWWW..........WWWWWWWWWWWWWW..................WWWWWWWWWWWWWWW',
    'WWWWWW............WWWWW......WWWWWWWWWWWWWWWWWWWWWW..........WWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW'
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