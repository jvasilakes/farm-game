from world import world

from windows import game_win 
from windows import msg_win
from list import list

import things
import plant
import inventory

class Character(object):	#TODO: make a player subclass


    def __init__(self, graphics):

	self.name = 'Character'

	self.graphics = graphics
	self.pos = [6, 6]    # y,x coordinates, not x,y coordinates
	self.dirs = [ord('w'), ord('s'), ord('a'), ord('d')]
	self.actions = [
			ord('p'), #plant
		        ord('o'), #open door
			ord('h'), #harvest
			ord('i'), #view inventory
			ord('j')  #drop an item
	 	       ]

	self.inventory = inventory.Inventory()

	world.add(self)


    def draw(self):

	game_win.addstr(self.pos[0], self.pos[1], self.graphics)


    def obstructed(self, dir): 

	pos = []

	if dir == ord('w'):
	    pos = [self.pos[0] - 1, self.pos[1]] 
	elif dir == ord('s'):
	    pos = [self.pos[0] + 1, self.pos[1]]
	elif dir == ord('a'):
	    pos = [self.pos[0], self.pos[1] - 1]
	elif dir == ord('d'):
	    pos = [self.pos[0], self.pos[1] + 1]

	for clas in list.things:
	    for thing in list.things[clas]:
		if pos in thing.get_boundries():
		    
		    return True

        return False


    def move(self, dir):

	if self.obstructed(dir):
	    return

	else:

	    if dir == ord('w'):
	        if self.pos[0] == 0:
		    pass

	        else:
		    self.pos[0] -= 1
		    game_win.clear()
		    game_win.addstr(self.pos[0], self.pos[1], self.graphics)

	    elif dir == ord('s'):
	        if self.pos[0] == (33 - 1):
		    pass

	        else:
		    self.pos[0] += 1
		    game_win.clear()
		    game_win.addstr(self.pos[0], self.pos[1], self.graphics)

	    elif dir == ord('a'): 
	        if self.pos[1] == 0:
		    pass

	        else:
		    self.pos[1] -= 1
		    game_win.clear()
		    game_win.addstr(self.pos[0], self.pos[1], self.graphics)

	    elif dir == ord('d'):
	        if self.pos[1] == (68 - 2): # 68 will be a var 'hor'
		    pass

	        else:
		    self.pos[1] += 1
		    game_win.clear()
		    game_win.addstr(self.pos[0], self.pos[1], self.graphics)
	
	    msg_win.clear()
	    msg_win.refresh()


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
	    pass

	else:
	    planting = plant.Plant(ypos, xpos, \
				  'GRAPHICS/plant1')

        msg_win.clear()
        msg_win.refresh()


    def harvest(self):

	for plant in list.things['plants']:
	    if [(self.pos[0] - 1), self.pos[1]] in plant.get_boundries():

		if plant.get_stage() == 3:

		    i = list.things['plants'].index(plant)
	
		    crop = list.things['plants'].pop(i)

		    self.inventory.add(crop)

		else:
		    return

	    else:
		pass
