from space import World, Cave
from character import Player, NPC


# ----------- CREATE SPACES -------------------------

world = World()

cave = Cave()

#------------- CHARACTERS ---------------------------

farmer = Player(PLAYER_1_START_POS, PLAYER_1_GRAPHIC, world)

dog = NPC(DOG_START_POS, DOG_GRAPHIC, world)

