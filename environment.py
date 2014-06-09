import random
import time

import animations

from header import *
from startup import game_win, msg_win
from node import Node
from inventory import Inventory
from expand import find_vicinity


class House(Node):


    def __init__(self, Ystart, Xstart, graphics_file, space):

	self.name = 'House'

	Node.__init__(self, Ystart, Xstart, graphics_file, space)

	# Visible from the start
	self.visible = True

	# Location of the front door
	self.vicinity.append([(Ystart + 5), (Xstart + 5)])


    def interact(self, player):

        # go into your house and sleep until the next day
        # plants grow one stage while you sleep

        game_win.clear()
        animations.sunrise(game_win)
        game_win.clear()
        self.space.grow_crops()
        self.space.redraw()
        player.draw()

	game_win.refresh()

	self.space.ship_box.sell(player)



class Shipbox(Node):


    def __init__(self, Ystart, Xstart, graphics_file, space):

	self.name = 'Shipbox'

	self.inventory = Inventory(self.name)

	Node.__init__(self, Ystart, Xstart, graphics_file, space)

	self.visible = True

	self.vicinity = find_vicinity(self.boundaries)


    def interact(self, player):

	msg_win.clear()
	msg_win.addstr(0, 5, "Shipping box: ")
	msg_win.addstr(0, 25, "1. Add items.")
	msg_win.addstr(1, 25, "2. Remove items.")
	msg_win.addstr(2, 25, "3. Nevermind.")
	msg_win.refresh()

	ans = msg_win.getch()
	
	while ans != ord('1') and ans != ord('2') and ans != ord('3'):
	    ans = msg_win.getch()

	msg_win.clear()

	if ans == ord('1'):

	    msg_win.addstr(1, 10, "What would you like to add?")
	    msg_win.refresh()
	    msg_win.getch()

	    msg_win.clear()
	    msg_win.refresh()

	    item_list = player.inventory.view()

	    if item_list == 'None':
		return

	    else:
	        ship_box.inventory.add(item_list)

	elif ans == ord('2'):

	    msg_win.addstr(1, 10, "What would you like to remove?")
	    msg_win.refresh()
	    msg_win.getch()

	    msg_win.clear()
	    msg_win.refresh()
	    item_list = ship_box.inventory.view()

	    if item_list == 'None':
		return

	    else:
	        player.inventory.add(item_list)

	elif ans == ord('3'):

	    return


    def sell(self, player):
	
	earnings = 0
	for key in self.inventory.contents:

	    for item in reversed(self.inventory.contents[key]):

		earnings += item.value
		self.inventory.contents[key].remove(item)

	player.inventory.money += earnings

	if earnings > 0:
	    msg_win.clear()
	    msg_win.refresh() 
	    msg_win.addstr(1, 5, "Total shipment value:")
	    msg_win.addstr(2, 5, "$")
	    msg_win.addstr(2, 6, str(earnings))
	    msg_win.refresh()

	else:
	    pass 


class Pond(Node):


    def __init__(self, Ystart, Xstart, graphics_file, space):

	self.name = 'Pond'

	Node.__init__(self, Ystart, Xstart, graphics_file, space)

	self.vicinity = find_vicinity(self.boundaries)


    def interact(self, player):

	random.seed

	msg_win.clear()
	msg_win.addstr(1, 5, "Fishing...")
	msg_win.refresh()

        seconds = random.randrange(2, 15)
	
	self.animate(seconds)

        game_win.refresh()

	if self.iscatch(0.6):

	    msg_win.clear()
	    msg_win.addstr(1, 5, "You caught a fish!")
	    msg_win.refresh()
	    msg_win.getch()

	    temp = []
	    temp.append(Fish.create())
	    player.inventory.add(temp)

	    return

	else:
	
	    msg_win.clear()
	    msg_win.addstr(1, 5, "No bites this time...")
	    msg_win.refresh()
	    msg_win.getch()

	    return


    def animate(self, duration):

        graphics1 = self.graphics
        graphics2 = self.load_graphics('GRAPHICS/pond2')

	for second in xrange(duration):

	    time.sleep(1)

	    if self.graphics == graphics1:
		self.graphics = graphics2
		self.space.redraw()

	    else:
		self.graphics = graphics1
		self.space.redraw()

	self.graphics = graphics1


    def iscatch(self, percent):

	return random.random() > percent


class Cave_Entrance(Node):

    @classmethod
    def create(cls, Ystart, Xstart, graphics_file, space):
	cave_entrance = Cave_Entrance(Ystart, Xstart, graphics_file, space)
	return cave_entrance

    def __init__(self, Ystart, Xstart, graphics_file, space):

	self.name = 'Cave_Entrance'

	Node.__init__(self, Ystart, Xstart, graphics_file, space)

	# Coordinates of cave entrance
	self.vicinity = [[Ystart + 3, Xstart + 2]]
	
	# So that nothing spawns in front of the entrance.
	self.boundaries.append(self.vicinity)


    def interact(self, player):
	pass

class Crop(Node):
	
    @classmethod
    def create(cls, Ystart, Xstart, graphics_file, space):
    	crop = Crop(Ystart, Xstart, graphics_file, space)
    	return crop

    def __init__(self, Ystart, Xstart, graphics_file, space):

	self.name = 'Crop'

	# Stage of growth out of 3
        self.stage = 1

	self.value = 5

	Node.__init__(self, Ystart, Xstart, graphics_file, space)


    def grow(self):


	if self.stage < 3:
	    self.stage += 1
	    self.graphics = self.load_graphics('GRAPHICS/crop' + str(self.stage))

	else:
	    return



class Tree(Node):

    @classmethod
    def create(cls, Ystart, Xstart, graphics_file, space):
	tree = Tree(Ystart, Xstart, graphics_file, space)
	return tree


    def __init__(self, Ystart, Xstart, graphics_file, space):

	self.name = 'Tree'

	Node.__init__(self, Ystart, Xstart, graphics_file, space)

	# Set boundaries so that characters can move behind trees.
	self.boundaries = [[Ystart + 2, Xstart + 2]]

	self.vicinity = [[Ystart + 2, Xstart + 1],
		        [Ystart + 2, Xstart + 3],
		        [Ystart + 3, Xstart + 2]]

	# How much wood the player gets
	self.resource_qty = 2


    def interact(self, farmer):

        msg_win.clear()
        msg_win.addstr(1, 10, "Chop down this tree? [y/n]")
        msg_win.refresh()
    
        ans = msg_win.getch()

        if ans == ord('y'):

	    temp = []
	
	    self.space.contents[self.name].remove(self)
	    game_win.clear()
	    farmer.draw()
	    self.space.redraw()

	    for i in xrange(self.resource_qty):
		temp.append(Wood.create())

  	    farmer.inventory.add(temp)

	else:
	    return



class Rock(Node):

    @classmethod
    def create(cls, Ystart, Xstart, graphics_file, space):
	rock = Rock(Ystart, Xstart, graphics_file, space)
	return rock

    def __init__(self, Ystart, Xstart, graphics_file, space):

	self.name = 'Rock'

	Node.__init__(self, Ystart, Xstart, graphics_file, space)

	

class Wood(Node):

    @classmethod
    def create(cls):
	wood = Wood()
	return wood


    def __init__(self):
	
	self.name = 'Wood'

	self.value = 10
	

class Stone(Node):

    @classmethod
    def create(cls):
	stone = Stone()
	return stone

    def __init__(self):

	self.name = 'Stone'

	self.value = 5
	

class Fish(Node):

    @classmethod
    def create(cls):
	fish = Fish()
	return fish


    def __init__(self):

	self.name = 'Fish'

	self.value = 20
	
