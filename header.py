import math
import curses
from sys import exit

from farm_config import DEBUG_WIN
from screenInfo import max_y, max_x


# ----CONTROL KEYS-------

KEY_UP = ord('w')
KEY_DOWN = ord('s')
KEY_LEFT = ord('a')
KEY_RIGHT = ord('d')
NULL = 'NULL'

KEY_INTERACT = ord('k')
KEY_PLANT = ord('p')
KEY_HARVEST = ord('h')
KEY_INVENTORY = ord('i')
KEY_FIND_PLAYER = ord('f')

KEY_QUIT = ord('q')


# ----WINDOW SIZES & POSITIONS -----

MIN_GAME_WIN_SIZE_Y = 26
MIN_GAME_WIN_SIZE_X = 63

GAME_WIN_POS_Y = 4
GAME_WIN_POS_X = 0

if DEBUG_WIN:
    GAME_WIN_SIZE_Y = max_y - GAME_WIN_POS_Y
    GAME_WIN_SIZE_X = max_x / 2
else:
    GAME_WIN_SIZE_Y = max_y - GAME_WIN_POS_Y - 3
    GAME_WIN_SIZE_X = max_x - 2

MSG_WIN_SIZE_Y = GAME_WIN_POS_Y - 1
MSG_WIN_SIZE_X = GAME_WIN_SIZE_X
MSG_WIN_POS_Y = 0
MSG_WIN_POS_X = 0

INTRO_ANIM_POS_Y = (GAME_WIN_SIZE_Y - MIN_GAME_WIN_SIZE_Y) / 2
INTRO_ANIM_POS_X = (GAME_WIN_SIZE_X - MIN_GAME_WIN_SIZE_X) / 2

LOGO_WIN_SIZE_Y = 6
LOGO_WIN_SIZE_X = 29
LOGO_WIN_POS_Y = INTRO_ANIM_POS_Y + 9
LOGO_WIN_POS_X = INTRO_ANIM_POS_X + 18

HELP_WIN_SIZE_Y = 10
HELP_WIN_SIZE_X = 22
HELP_WIN_POS_Y = INTRO_ANIM_POS_Y + 18
HELP_WIN_POS_X = INTRO_ANIM_POS_X + 21

DEBUG_WIN_SIZE_Y = max_y - 3
DEBUG_WIN_SIZE_X = (max_x - GAME_WIN_SIZE_X - 2)
DEBUG_WIN_POS_Y = 3
DEBUG_WIN_POS_X = GAME_WIN_SIZE_X + 2

DEBUG_TITLE_SIZE_Y = 2
DEBUG_TITLE_SIZE_X = 20
DEBUG_TITLE_POS_Y = 0
DEBUG_TITLE_POS_X = DEBUG_WIN_POS_X + ((DEBUG_WIN_SIZE_X / 2) - 10)

if GAME_WIN_SIZE_Y > max_y or GAME_WIN_SIZE_X > max_x \
    or GAME_WIN_SIZE_Y < MIN_GAME_WIN_SIZE_Y \
    or GAME_WIN_SIZE_X < MIN_GAME_WIN_SIZE_X:

    print "Incompatible game_win size!"
    print "game_y: %d  game_x: %d" %(GAME_WIN_SIZE_Y, GAME_WIN_SIZE_X)
    exit(1)

if DEBUG_WIN_SIZE_X < 40:

    print("Incompatible debug win size!")


# ---- ENVIRONMENT VARIABLES ----

VIEW_DISTANCE_Y = 5
VIEW_DISTANCE_X = 8

SUNRISE_DIR = 'GRAPHICS/SUNRISE/'
HOUSE_GRAPHIC = 'GRAPHICS/house'
SHIP_BOX_GRAPHIC = 'GRAPHICS/ship_box'
POND_GRAPHIC = 'GRAPHICS/pond1'
CAVE_GRAPHICS_DIR = 'GRAPHICS/CAVE/'

NUMBER_TREES = int(math.sqrt(GAME_WIN_SIZE_Y * GAME_WIN_SIZE_X))
NUMBER_ROCKS = int(math.sqrt(GAME_WIN_SIZE_Y * GAME_WIN_SIZE_X))
NUMBER_BUSHES = int(math.sqrt((GAME_WIN_SIZE_Y * GAME_WIN_SIZE_X) / 2))

PLAYER_1_GRAPHIC = '@'
PLAYER_1_START_POS = [6, 6]
PLAYER_1_START_POS_CAVE = [2, 11]

DOG_GRAPHIC = 'd'
DOG_START_POS = [7, 8] 
