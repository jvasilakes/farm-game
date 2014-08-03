from header import *
from environment import World
from cave_system import Cave
from character import Player, NPC
from space import Space

# ----------- CREATE SPACES -------------------------

world = World()

cave = Cave()

#------------- CHARACTERS ---------------------------

farmer = Player(PLAYER_1_START_POS, PLAYER_1_GRAPHIC, Space.members['World'])

dog = NPC(DOG_START_POS, DOG_GRAPHIC, Space.members['World'])

