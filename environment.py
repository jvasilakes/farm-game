import random
import time

import game
import debug_console
import farm_config
import animations
import cave_system

from header import *
from expand import find_vicinity
from pathfinding import Astar, wrapper
from inventory import Inventory
from node import Node
from space import Space



class World(Space):

    def __init__(self):

	self.name = 'World'

	Space.__init__(self)

	if farm_config.DEBUG_WIN:
	    debug_console.get()._print("World created.")

	self.house = House(1, 1, HOUSE_GRAPHIC, self)
	self.ship_box = Shipbox(4, 12, SHIP_BOX_GRAPHIC, self)
	self.pond = Pond(GAME_WIN_SIZE_Y - 5,
			 GAME_WIN_SIZE_X - 16,
			 POND_GRAPHIC,
			 self
			 )

	self.seed(Cave_Entrance, CAVE_GRAPHICS_DIR + 'entrance_external', 1)
	self.seed(Tree, 'GRAPHICS/tree', NUMBER_TREES)
	self.seed(Rock, 'GRAPHICS/rock', NUMBER_ROCKS)
	self.seed(Bush, 'GRAPHICS/bush', NUMBER_BUSHES)

	if farm_config.DEBUG_WIN:
	    debug_console.get()._print("World populated.")

	self.sort_contents()

	if farm_config.DEBUG_WIN:
	    debug_console.get()._print("World contents sorted.")

    
    def grow_crops(self):

	try:

	    for crop in self.contents['Crop']:
	        crop.grow()

	except:
	    return


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

	game.get_instance().msg_win.clear()
	game.get_instance().msg_win.addstr(1, 5, "Go to sleep? [y/n]")
	game.get_instance().msg_win.refresh()

	ans = game.get_instance().msg_win.getch()

	if ans == ord('y'):

	    game.get_instance().msg_win.clear()
	    game.get_instance().msg_win.refresh()

	    game.get_instance().game_win.clear()

	    animations.sunrise(game.get_instance().game_win)

	    game.get_instance().game_win.clear()

	    self.space.grow_crops()
	    self.space.redraw(game.get_instance().game_win)

	    player.draw(game.get_instance().game_win)

	    game.get_instance().game_win.refresh()

	    self.space.ship_box.sell(player)

	else:
	    return


class Shipbox(Node):


    def __init__(self, Ystart, Xstart, graphics_file, space):

	self.name = 'Shipbox'

	self.inventory = Inventory(self.name)

	Node.__init__(self, Ystart, Xstart, graphics_file, space)

	self.visible = True

	self.vicinity = find_vicinity(self.boundaries)


    def interact(self, player):

	game.get_instance().msg_win.clear()
	game.get_instance().msg_win.addstr(0, 5, "Shipping box: ")
	game.get_instance().msg_win.addstr(0, 25, "1. Add items.")
	game.get_instance().msg_win.addstr(1, 25, "2. Remove items.")
	game.get_instance().msg_win.addstr(2, 25, "3. Nevermind.")
	game.get_instance().msg_win.refresh()

	ans = game.get_instance().msg_win.getch()
	
	while ans != ord('1') and ans != ord('2') and ans != ord('3'):
	    ans = game.get_instance().msg_win.getch()

	game.get_instance().msg_win.clear()

	if ans == ord('1'):

	    game.get_instance().msg_win.addstr(1, 10, "What would you like to add?")
	    game.get_instance().msg_win.refresh()
	    game.get_instance().msg_win.getch()

	    game.get_instance().msg_win.clear()
	    game.get_instance().msg_win.refresh()

	    item_list = player.inventory.view()

	    if item_list == 'None':
		return

	    else:
	        self.inventory.add(item_list)

	elif ans == ord('2'):

	    game.get_instance().msg_win.addstr(1, 10, "What would you like to remove?")
	    game.get_instance().msg_win.refresh()
	    game.get_instance().msg_win.getch()

	    game.get_instance().msg_win.clear()
	    game.get_instance().msg_win.refresh()
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
	    game.get_instance().msg_win.clear()
	    game.get_instance().msg_win.refresh() 
	    game.get_instance().msg_win.addstr(1, 5, "Total shipment value:")
	    game.get_instance().msg_win.addstr(2, 5, "$")
	    game.get_instance().msg_win.addstr(2, 6, str(earnings))
	    game.get_instance().msg_win.refresh()

	else:
	    pass 



class Pond(Node):


    def __init__(self, Ystart, Xstart, graphics_file, space):

	self.name = 'Pond'

	Node.__init__(self, Ystart, Xstart, graphics_file, space)

	self.vicinity = find_vicinity(self.boundaries)


    def interact(self, player):

	random.seed

	game.get_instance().msg_win.clear()
	game.get_instance().msg_win.addstr(1, 5, "Go fishing? [y/n]")
	game.get_instance().msg_win.refresh()

	ans = game.get_instance().msg_win.getch()

	if ans != ord('y'):
	    return

	game.get_instance().msg_win.clear()
	game.get_instance().msg_win.addstr(1, 5, "Fishing...")
	game.get_instance().msg_win.refresh()

        seconds = random.randrange(2, 15)
	
	self.animate(seconds)

        game.get_instance().game_win.refresh()

	if self.iscatch(0.6):

	    game.get_instance().msg_win.clear()
	    game.get_instance().msg_win.addstr(1, 5, "You caught a fish!")
	    game.get_instance().msg_win.refresh()
	    game.get_instance().msg_win.getch()

	    temp = []
	    temp.append(Fish.create())
	    player.inventory.add(temp)

	    return

	else:
	
	    game.get_instance().msg_win.clear()
	    game.get_instance().msg_win.addstr(1, 5, "No bites this time...")
	    game.get_instance().msg_win.refresh()
	    game.get_instance().msg_win.getch()

	    return


    def animate(self, duration):

        graphics1 = self.graphics
        graphics2 = self.load_graphics('GRAPHICS/pond2')

	for second in xrange(duration):

	    time.sleep(1)

	    if self.graphics == graphics1:
		self.graphics = graphics2
		self.space.redraw(game.get_instance().game_win)

	    else:
		self.graphics = graphics1
		self.space.redraw(game.get_instance().game_win)

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

	self.cave_system = cave_system.Cave()


    def interact(self, player):

	game.get_instance().msg_win.clear()
	game.get_instance().msg_win.addstr(1, 5, "Enter the cave? [y/n]")
	game.get_instance().msg_win.refresh()

	ans = game.get_instance().msg_win.getch()

	while ans != ord('y') and ans != ord('n'):
	    ans = game.get_instance().msg_win.getch()

	if ans == ord('n'):

	    game.get_instance().msg_win.clear()	    

	    return

	elif ans == ord('y'):

	    game.get_instance().msg_win.clear()	    
	    game.get_instance().msg_win.addstr(1, 5, "The cave entrance is blocked off...")
	    game.get_instance().msg_win.refresh()

	    return

	    #Space.members['Cave'].add(player)

	    #player.current_space = Space.members['Cave']

	    #player.pos = PLAYER_1_START_POS_CAVE

	else:
	
	    return
	    

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

        game.get_instance().msg_win.clear()
        game.get_instance().msg_win.addstr(1, 10, "Chop down this tree? [y/n]")
        game.get_instance().msg_win.refresh()
    
        ans = game.get_instance().msg_win.getch()

        if ans == ord('y'):

	    temp = []
	
	    self.space.contents[self.name].remove(self)
	    game.get_instance().game_win.clear()
	    farmer.draw(game.get_instance().game_win)
	    self.space.redraw(game.get_instance().game_win)

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

	self.vicinity = find_vicinity(self.boundaries)

	self.resource_qty = 1

	
    def interact(self, farmer):

        game.get_instance().msg_win.clear()
        game.get_instance().msg_win.addstr(1, 10, "Break this rock? [y/n]")
        game.get_instance().msg_win.refresh()
    
        ans = game.get_instance().msg_win.getch()

        if ans == ord('y'):

	    temp = []
	
	    self.space.contents[self.name].remove(self)
	    game.get_instance().game_win.clear()
	    farmer.draw(game.get_instance().game_win)
	    self.space.redraw(game.get_instance().game_win)

	    for i in xrange(self.resource_qty):
		temp.append(Stone.create())

  	    farmer.inventory.add(temp)

	else:
	    return


class Bush(Node):

    @classmethod
    def create(cls, Ystart, Xstart, graphics_file, space):
	bush = Bush(Ystart, Xstart, graphics_file, space)
	return bush

    def __init__(self, Ystart, Xstart, graphics_file, space):

	self.name = 'Bush'

	Node.__init__(self, Ystart, Xstart, graphics_file, space)

	self.vicinity = find_vicinity(self.boundaries)

	random.seed()
	self.resource_qty = random.randint(0, 2)


    def interact(self, farmer):

	game.get_instance().msg_win.clear()
	game.get_instance().msg_win.addstr(1, 10, "Forage in this bush? [y/n]")
	game.get_instance().msg_win.refresh()

	ans = game.get_instance().msg_win.getch()

	if ans == ord('y'):

	    if self.resource_qty > 0:

		temp = []

		for i in xrange(self.resource_qty):
		    temp.append(Berries.create())

		farmer.inventory.add(temp)

		self.resource_qty = 0

	    else:
		game.get_instance().msg_win.addstr(2, 10, "You find nothing.")
		game.get_instance().msg_win.refresh()

	else:
	    return


class Berries(Node):

    @classmethod
    def create(cls):
	berries = Berries()
	return berries


    def __init__(self):
	
	self.name = 'Berries'

	self.value = 2
	

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

	self.value = 2
	

class Fish(Node):

    @classmethod
    def create(cls):
	fish = Fish()
	return fish


    def __init__(self):

	self.name = 'Fish'

	self.value = 20

