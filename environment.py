import random
import time

import animations
from thing import Thing
from inventory import Inventory
from expand import find_vicinity
from windows import game_win, msg_win, debug_win
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
        world.grow_crops()   # Use updateAll here
        world.redraw()
        player.draw()

	game_win.refresh()

	ship_box.sell(player)



class Shipbox(Thing):


    def __init__(self, Ystart, Xstart, graphics):

	self.name = 'Shipbox'

	self.inventory = Inventory(self.name)

	Thing.__init__(self, Ystart, Xstart, graphics)

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
	for cls in self.inventory.contents:

	    for item in reversed(self.inventory.contents[cls]):

		earnings += item.value
		self.inventory.contents[cls].remove(item)

	player.money += earnings

	if earnings > 0:
	    msg_win.clear()
	    msg_win.refresh() 
	    msg_win.addstr(1, 5, "Total shipment value:")
	    msg_win.addstr(2, 5, "$")
	    msg_win.addstr(2, 6, str(earnings))
	    msg_win.refresh()

	else:
	    pass 


class Pond(Thing):


    def __init__(self, Ystart, Xstart, graphics):

	self.name = 'Pond'

	Thing.__init__(self, Ystart, Xstart, graphics)

	self.vicinity = find_vicinity(self.boundries)

    
    def interact(self, player):

	random.seed

	msg_win.clear()
	msg_win.addstr(1, 5, "Fishing...")
	msg_win.refresh()

        seconds = random.randrange(2, 15)
	debug_win.prnt("Fishing for " + str(seconds) + " seconds")
	
	# Comment out if you don't want to wait while debugging
	#time.sleep(seconds) 

	for second in xrange(seconds):
	    self.animate()
	    self.graphics = 'GRAPHICS/pond1'
	    self.draw()
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


    def iscatch(self, percent):

	return random.random() > percent


    def animate(self):

	time.sleep(1)

	if self.graphics == 'GRAPHICS/pond1':
	    self.graphics = 'GRAPHICS/pond2'
	    world.redraw()

	else:
	    self.graphics = 'GRAPHICS/pond1'
	    world.redraw()

class Crop(Thing):
	
    @classmethod
    def create(cls, Ystart, Xstart, graphics):
    	crop = Crop(Ystart, Xstart, graphics)
    	return crop

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


    # I don't think I need this...
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

	# Sometimes it easier to hard code it in
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
	

class Stone(Thing):

    @classmethod
    def create(cls):
	stone = Stone()
	return stone

    def __init__(self):

	self.name = 'Stone'

	self.value = 5
	

class Fish(Thing):

    @classmethod
    def create(cls):
	fish = Fish()
	return fish


    def __init__(self):

	self.name = 'Fish'

	self.value = 20
	
	

#----- SINGLETONS ----------------------------------	

house = House(1, 1, 'GRAPHICS/house')

ship_box = Shipbox(4, 12, 'GRAPHICS/ship_box')

pond = Pond(28, 40, 'GRAPHICS/pond1')
