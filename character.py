import thing
import inventory

from world import world
from windows import game_win, msg_win
from environment import Crop
from environment import ship_box


class Character(object):

    def __init__(self, graphics):

	self.graphics = graphics
	self.dirs = [ord('w'), ord('s'), ord('a'), ord('d')]

        world.add(self)

	self.draw()


    def draw(self):

	game_win.addstr(self.pos[0], self.pos[1], self.graphics)


    def obstructed(self, dir): 

	# Checks if the space to which the player is moving is
	# occupied by some object.

	pos = []

	if dir == ord('w'):
	    pos = [self.pos[0] - 1, self.pos[1]] 
	elif dir == ord('s'):
	    pos = [self.pos[0] + 1, self.pos[1]]
	elif dir == ord('a'):
	    pos = [self.pos[0], self.pos[1] - 1]
	elif dir == ord('d'):
	    pos = [self.pos[0], self.pos[1] + 1]

	for cls in world.contents:
	    for thing in world.contents[cls]:
		if pos in thing.get_boundries():
		    
		    return True

        return False


    def move(self, dir):

	if self.obstructed(dir):
	    return


	else:

	    if dir == ord('w'):
	    	
	    	# if character's y position is all the way at the top.
	        if self.pos[0] == 0:
		    pass

	        else:
		    self.pos[0] -= 1
		    #game_win.clear()
		    #self.draw()

	    elif dir == ord('s'):
	    	
	    	# if character's position is all the way at the bottom.
	        if self.pos[0] == 31:
		    pass

	        else:
		    self.pos[0] += 1
		    #game_win.clear()
		    #self.draw()

	    elif dir == ord('a'): 
	    	
	    	# if character's x position is all the way to the left
	        if self.pos[1] == 0:
		    pass

	        else:
		    self.pos[1] -= 1
		    #game_win.clear()
		    #self.draw()

	    elif dir == ord('d'):
	    	# if character's x position is all the way to the right
	        if self.pos[1] == 65:
		    pass

	        else:
		    self.pos[1] += 1
		    #game_win.clear()
		    #self.draw()
	
	    msg_win.clear()
	    msg_win.refresh()



	if isinstance(self, Player):
		
	    # if the character is a player,
	    # then prompt player if they are able
	    # to interact with something they are next to.

	    for key in world.contents:
	        for thing in world.contents[key]:
		    if self.pos in thing.vicinity:
	    	        msg_win.clear()
	    	        msg_win.addstr(1, 20, "Press 'k' to interact.")
	    	        msg_win.refresh()
	    


class Player(Character):

    def __init__(self, graphics):

	self.name = 'Player'

	self.pos = [6, 6]

	self.actions = [
	    ord('k'), #interact
	    ord('p'), #plant
	    ord('h'), #harvest
	    ord('i'), #view inventory
	    ]

	self.inventory = inventory.Inventory(self.name)
	
	self.money = 0

	Character.__init__(self, graphics)


    def plant(self):

	msg_win.clear()

	msg_win.addstr(1, 20, "In which direction? [wasd] ")
	ans = msg_win.getch()

	msg_win.clear()
	msg_win.refresh()

	if ans == ord('w'):
	    ypos = self.pos[0] - 1
	    xpos = self.pos[1]

	elif ans == ord('s'):
	    ypos = self.pos[0] + 1
	    xpos = self.pos[1]

	elif ans == ord('a'):
	    ypos = self.pos[0]
	    xpos = self.pos[1] - 1

	elif ans == ord('d'):
	    ypos = self.pos[0]
	    xpos = self.pos[1] + 1

	else:
	    return
	
	if self.obstructed(ans):
	    return

	else:
	    # TODO: make Crop.create() class method
	    planting = Crop(ypos, xpos, 'GRAPHICS/crop1')

        msg_win.clear()
        msg_win.refresh()


    def harvest(self):

	try:

	    for crop in world.contents['Crop']:
	    	
	    	# if there is a crop directly above the player
	        if [(self.pos[0] - 1), self.pos[1]] in crop.get_boundries():

		    if crop.get_stage() == 3:

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


farmer = Player('@')
