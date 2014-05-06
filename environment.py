import random
import time

import animations

from header import *
from startup import game_win, msg_win
from world import world
from node import Node
from inventory import Inventory
from expand import find_vicinity


class House(Node):


    def __init__(self, Ystart, Xstart, graphics_file):

	self.name = 'House'

	Node.__init__(self, Ystart, Xstart, graphics_file)

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
        world.grow_crops()
        world.redraw()
        player.draw()

	game_win.refresh()

	ship_box.sell(player)



class Shipbox(Node):


    def __init__(self, Ystart, Xstart, graphics_file):

	self.name = 'Shipbox'

	self.inventory = Inventory(self.name)

	Node.__init__(self, Ystart, Xstart, graphics_file)

	self.visible = True

	self.vicinity = find_vicinity(self.boundries)


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


    def __init__(self, Ystart, Xstart, graphics_file):

	self.name = 'Pond'

	Node.__init__(self, Ystart, Xstart, graphics_file)

	self.vicinity = find_vicinity(self.boundries)


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
		world.redraw()

	    else:
		self.graphics = graphics1
		world.redraw()

	self.graphics = graphics1


    def iscatch(self, percent):

	return random.random() > percent



class Crop(Node):
	
    @classmethod
    def create(cls, Ystart, Xstart, graphics_file):
    	crop = Crop(Ystart, Xstart, graphics_file)
    	return crop

    def __init__(self, Ystart, Xstart, graphics_file):

	self.name = 'Crop'

	# Stage of growth out of 3
        self.stage = 1

	self.value = 5

	Node.__init__(self, Ystart, Xstart, graphics_file)


    def grow(self):


	if self.stage < 3:
	    self.stage += 1
	    self.graphics = self.load_graphics('GRAPHICS/crop' + str(self.stage))

	else:
	    return



class Tree(Node):

    @classmethod
    def create(cls, Ystart, Xstart, graphics_file):
	tree = Tree(Ystart, Xstart, graphics_file)
	return tree


    def __init__(self, Ystart, Xstart, graphics_file):

	self.name = 'Tree'

	Node.__init__(self, Ystart, Xstart, graphics_file)

	self.vicinity = [[Ystart + 2, Xstart],
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
	
	    world.contents[self.name].remove(self)
	    game_win.clear()
	    farmer.draw()
	    world.redraw()

	    for i in xrange(self.resource_qty):
		temp.append(Wood.create())

  	    farmer.inventory.add(temp)

	else:
	    return



class Rock(Node):

    @classmethod
    def create(cls, Ystart, Xstart, graphics_file):
	rock = Rock(Ystart, Xstart, graphics_file)
	return rock

    def __init__(self, Ystart, Xstart, graphics_file):

	self.name = 'Rock'

	Node.__init__(self, Ystart, Xstart, graphics_file)

	

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
	
	

#----- SINGLETONS ----------------------------------	

house = House(1, 1, HOUSE_GRAPHIC)

ship_box = Shipbox(4, 12, SHIP_BOX_GRAPHIC)

pond = Pond(GAME_WIN_SIZE_Y-5, GAME_WIN_SIZE_X-16, POND_GRAPHIC)
