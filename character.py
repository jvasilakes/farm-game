import random

from header import *
from world import world
from startup import game_win, msg_win
from inventory import Inventory
from environment import Crop
from environment import ship_box


class Character(object):

    list = []

    @classmethod
    def drawAll(cls):
	
	for character in Character.list:
	    character.draw()


    def __init__(self, start_pos, graphics):

	self.pos = start_pos	
	self.graphics = graphics
	self.dirs = [
	    KEY_UP,
	    KEY_DOWN, 
	    KEY_LEFT, 
	    KEY_RIGHT, 
	    NULL
	    ]

	Character.list.append(self)

	world.add(self)


    def draw(self):

	game_win.addstr(self.pos[0], self.pos[1], self.graphics)


    def obstructed(self, dir): 

	# Checks if the space to which the player is moving is
	# occupied by something.

	pos = []

	if dir == KEY_UP:
	    pos = [self.pos[0] - 1, self.pos[1]] 
	elif dir == KEY_DOWN:
	    pos = [self.pos[0] + 1, self.pos[1]]
	elif dir == KEY_LEFT:
	    pos = [self.pos[0], self.pos[1] - 1]
	elif dir == KEY_RIGHT:
	    pos = [self.pos[0], self.pos[1] + 1]

	for key in world.contents:
	    for obj in world.contents[key]:
		if pos in obj.boundries:
		    
		    return True

	for key in world.characters:
	    for character in world.characters[key]:

		if pos == character.pos:

		    # If a character is in the way of the Player, move it out of the way.
		    if isinstance(self, Player):
			self.displace(character, dir)
			return False

		    else:
			return True

        return False


    def move(self, dir):

	if isinstance(self, Player):
		
	    for key in world.contents:
	        for obj in world.contents[key]:

		    # Make visible objects within the Player's view distance
		    if abs(obj.Ystart - self.pos[0]) <= self.view_distance_y:
			if abs(obj.Xstart - self.pos[1]) <= self.view_distance_x:
			    obj.visible = True

		    # Check to see if we can interact with anything
		    if self.pos in obj.vicinity:
	    	        msg_win.clear()
	    	        msg_win.addstr(1, 20, "Press " + chr(KEY_INTERACT) + " to interact.")
	    	        msg_win.refresh()
	    
	if dir == NULL:
	    return

	if self.obstructed(dir):
	    return

	else:

	    if dir == KEY_UP:
	    	
	    	# if character's y position is all the way at the top.
	        if self.pos[0] == 0:
		    pass

	        else:
		    self.pos[0] -= 1

	    elif dir == KEY_DOWN:
	    	
	    	# if character's y position is all the way at the bottom.
	        if self.pos[0] == (GAME_WIN_SIZE_Y-2):
		    pass

	        else:
		    self.pos[0] += 1

	    elif dir == KEY_LEFT: 
	    	
	    	# if character's x position is all the way to the left
	        if self.pos[1] == 0:
		    pass

	        else:
		    self.pos[1] -= 1

	    elif dir == KEY_RIGHT:
	    	# if character's x position is all the way to the right
	        if self.pos[1] == (GAME_WIN_SIZE_X-1):
		    pass

	        else:
		    self.pos[1] += 1
	
	    msg_win.clear()
	    msg_win.refresh()



class Player(Character):

    def __init__(self, start_pos, graphics):

	self.name = 'Player'

	self.actions = [
	    KEY_INTERACT,
	    KEY_PLANT,
	    KEY_HARVEST,
	    KEY_INVENTORY
	    ]

	self.view_distance_y = VIEW_DISTANCE_Y
	self.view_distance_x = VIEW_DISTANCE_X

	self.inventory = Inventory(self.name)
	
	Character.__init__(self, start_pos, graphics)


    # Moves another character if it is the way of the Player
    def displace(self, character, dir): 
	character.move(dir)


    def plant(self):

	msg_win.clear()

	msg_win.addstr(1, 20, "In which direction? [wasd] ")
	ans = msg_win.getch()

	msg_win.clear()
	msg_win.refresh()

	if ans == KEY_UP:
	    ypos = self.pos[0] - 1
	    xpos = self.pos[1]

	elif ans == KEY_DOWN:
	    ypos = self.pos[0] + 1
	    xpos = self.pos[1]

	elif ans == KEY_LEFT:
	    ypos = self.pos[0]
	    xpos = self.pos[1] - 1

	elif ans == KEY_RIGHT:
	    ypos = self.pos[0]
	    xpos = self.pos[1] + 1

	else:
	    return
	
	if self.obstructed(ans):
	    return

	else:
	    new = Crop.create(ypos, xpos, 'GRAPHICS/crop1')
	    new.insert()

        msg_win.clear()
        msg_win.refresh()


    def harvest(self):

	try:

	    for crop in world.contents['Crop']:

	    	# if there is a crop directly above the player
	        if [(self.pos[0] - 1), self.pos[1]] in crop.boundries:

		    if crop.stage == 3:

			temp = []

		        i = world.contents['Crop'].index(crop)
	
		        plant = world.contents['Crop'].pop(i)
			temp.append(plant)

		        self.inventory.add(temp)

		    else:
		        return

	        else:
		    pass

	except:
	    return


class NPC(Character):

    def __init__(self, start_pos, graphics):

	self.name = 'NPC'

	Character.__init__(self, start_pos, graphics)

	self.last_dir = NULL


    def is_same_dir(self, percent):

	return random.random() > percent


    def AI_move(self):

	if self.is_same_dir(0.8):
	    dir = self.last_dir

	else:
	    dir = random.choice(self.dirs)
	    self.last_dir = dir

	self.move(dir)



#------------- SINGLETONS ---------------------------

farmer = Player(PLAYER_1_START_POS, PLAYER_1_GRAPHIC)

dog = NPC(DOG_START_POS, DOG_GRAPHIC)
