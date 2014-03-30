import random

import animations
from thing import Thing
from inventory import Inventory
from expand import find_vicinity
from windows import game_win, msg_win
from world import world


class House(Thing):


    def __init__(self, Ystart, Xstart, graphics):

	self.name = 'House'

	Thing.__init__(self, Ystart, Xstart, graphics)

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


	earnings = 0	#Make all this into another function
	for cls in ship_box.inventory.contents:
	    for item in ship_box.inventory.contents[cls]:
		earnings += item.value

	player.money += earnings

	if earnings > 0:
	    msg_win.clear()
	    msg_win.refresh() 
	    msg_win.addstr(1, 5, "You earned %d dollars", earnings)
	    msg_win.addstr(2, 6, "from your shipments.")
	    msg_win.refresh()

	else:
	    pass 


class Shipbox(Thing):


    def __init__(self, Ystart, Xstart, graphics):

	self.name = 'Shipbox'

	self.inventory = Inventory()

	Thing.__init__(self, Ystart, Xstart, graphics)

	self.vicinity = find_vicinity(self.boundries)


    def interact(self, player):

	msg_win.clear()
	msg_win.addstr(0, 5, "Shipping box: ")
	msg_win.addstr(0, 25, "1. Add item.")
	msg_win.addstr(1, 25, "2. Remove item.")
	msg_win.addstr(2, 25, "3. View contents.")
	msg_win.refresh()

	ans = msg_win.getch()
	
	msg_win.clear()

	if ans == ord('1'):
	    msg_win.addstr(1, 10, "What would you like to add?")
	    msg_win.refresh()
	    msg_win.getch()

	    msg_win.clear()
	    msg_win.refresh()
	    thing = player.inventory.remove()

	    if thing == 'Nothing':
		return

	    else:
	        ship_box.inventory.add(thing)

	elif ans == ord('2'):
	    msg_win.addstr(1, 10, "What would you like to remove?")
	    msg_win.refresh()
	    msg_win.getch()

	    msg_win.clear()
	    msg_win.refresh()
	    thing = ship_box.inventory.remove()

	    if thing == 'Nothing':
		return

	    else:
	        player.inventory.add(thing)

	elif ans == ord('3'):
	    ship_box.inventory.view()

	else:
	    return


class Pond(Thing):


    def __init__(self, Ystart, Xstart, graphics):

	self.name = 'Pond'

	Thing.__init__(self, Ystart, Xstart, graphics)


#    def catch_fish(self):

#	random.seed

#	result = random.randrange(0, 5)

#	if result == fish_caught:
#	    return fish #############NOT DONE######YETTTT#####


class Crop(Thing):

    def __init__(self, Ystart, Xstart, graphics):

	self.name = 'Crop'

        self.stage = 1

	self.value = 5

	Thing.__init__(self, Ystart, Xstart, graphics)


    def grow(self):


	if self.stage < 3:
	    self.stage += 1
	    self.graphics = 'GRAPHICS/crop' + str(self.stage)

	else:
	    return


    def get_stage(self):

	return self.stage


class Tree(Thing):

    @classmethod
    def create(cls, Ystart, Xstart, graphics):
	tree = Tree(Ystart, Xstart, graphics)
	return tree


    def __init__(self, Ystart, Xstart, graphics):

	self.name = 'Tree'

	Thing.__init__(self, Ystart, Xstart, graphics)

	self.vicinity = [[Ystart + 2, Xstart],
		    [Ystart + 2, Xstart + 3],
		    [Ystart + 3, Xstart + 2]]

	#self.actable = vicinity

	self.resource_qty = 2


    def interact(self, farmer):

        msg_win.clear()
        msg_win.addstr(1, 10, "Chop down this tree? [y/n]")
        msg_win.refresh()
    
        ans = msg_win.getch()

        if ans == ord('y'):

	    world.contents[self.name].remove(self)
	    world.redraw()

	    for i in xrange(self.resource_qty):
		farmer.inventory.add(Wood.create())

	else:
	    return



class Rock(Thing):

    @classmethod
    def create(cls, Ystart, Xstart, graphics):
	rock = Rock(Ystart, Xstart, graphics)
	return rock

    def __init__(self, Ystart, Xstart, graphics):

	self.name = 'Rock'

	Thing.__init__(self, Ystart, Xstart, graphics)

	

class Wood(Thing):

    @classmethod
    def create(cls):
	wood = Wood()
	return wood


    def __init__(self):
	
	self.name = 'Wood'

	self.value = 10
	
	

#----- SINGLETONS ----------------------------------	

house = House(1, 1, 'GRAPHICS/house')

ship_box = Shipbox(4, 12, 'GRAPHICS/ship_box')

pond = Pond(28, 40, 'GRAPHICS/pond')
