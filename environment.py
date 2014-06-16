import random
import time

import windows
import animations

from header import *
from expand import find_vicinity
from pathfinding import Astar, wrapper
from inventory import Inventory
from node import Node
from space import Space



class World(Space):

    def __init__(self):

	windows.debug_win._print("World created.")

	self.name = 'World'

	Space.__init__(self)

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

	windows.debug_win._print("World populated.")

	self.sort_contents()

	windows.debug_win._print("World contents sorted.")


    
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

	windows.msg_win.clear()
	windows.msg_win.addstr(1, 5, "Go to sleep? [y/n]")
	windows.msg_win.refresh()

	ans = windows.msg_win.getch()

	if ans == ord('y'):

	    windows.msg_win.clear()
	    windows.msg_win.refresh()

	    windows.game_win.clear()

	    animations.sunrise(windows.game_win)

	    windows.game_win.clear()

	    self.space.grow_crops()
	    self.space.redraw()

	    player.draw()

	    windows.game_win.refresh()

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

	windows.msg_win.clear()
	windows.msg_win.addstr(0, 5, "Shipping box: ")
	windows.msg_win.addstr(0, 25, "1. Add items.")
	windows.msg_win.addstr(1, 25, "2. Remove items.")
	windows.msg_win.addstr(2, 25, "3. Nevermind.")
	windows.msg_win.refresh()

	ans = windows.msg_win.getch()
	
	while ans != ord('1') and ans != ord('2') and ans != ord('3'):
	    ans = windows.msg_win.getch()

	windows.msg_win.clear()

	if ans == ord('1'):

	    windows.msg_win.addstr(1, 10, "What would you like to add?")
	    windows.msg_win.refresh()
	    windows.msg_win.getch()

	    windows.msg_win.clear()
	    windows.msg_win.refresh()

	    item_list = player.inventory.view()

	    if item_list == 'None':
		return

	    else:
	        self.inventory.add(item_list)

	elif ans == ord('2'):

	    windows.msg_win.addstr(1, 10, "What would you like to remove?")
	    windows.msg_win.refresh()
	    windows.msg_win.getch()

	    windows.msg_win.clear()
	    windows.msg_win.refresh()
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
	    windows.msg_win.clear()
	    windows.msg_win.refresh() 
	    windows.msg_win.addstr(1, 5, "Total shipment value:")
	    windows.msg_win.addstr(2, 5, "$")
	    windows.msg_win.addstr(2, 6, str(earnings))
	    windows.msg_win.refresh()

	else:
	    pass 


class Pond(Node):


    def __init__(self, Ystart, Xstart, graphics_file, space):

	self.name = 'Pond'

	Node.__init__(self, Ystart, Xstart, graphics_file, space)

	self.vicinity = find_vicinity(self.boundaries)


    def interact(self, player):

	random.seed

	windows.msg_win.clear()
	windows.msg_win.addstr(1, 5, "Fishing...")
	windows.msg_win.refresh()

        seconds = random.randrange(2, 15)
	
	self.animate(seconds)

        windows.game_win.refresh()

	if self.iscatch(0.6):

	    windows.msg_win.clear()
	    windows.msg_win.addstr(1, 5, "You caught a fish!")
	    windows.msg_win.refresh()
	    windows.msg_win.getch()

	    temp = []
	    temp.append(Fish.create())
	    player.inventory.add(temp)

	    return

	else:
	
	    windows.msg_win.clear()
	    windows.msg_win.addstr(1, 5, "No bites this time...")
	    windows.msg_win.refresh()
	    windows.msg_win.getch()

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

	windows.msg_win.clear()
	windows.msg_win.addstr(1, 5, "Enter the cave? [y/n]")
	windows.msg_win.refresh()

	ans = windows.msg_win.getch()

	while ans != ord('y') and ans != ord('n'):
	    ans = windows.msg_win.getch()

	if ans == ord('n'):

	    windows.msg_win.clear()	    

	    return

	elif ans == ord('y'):

	    windows.msg_win.clear()	    
	    windows.msg_win.addstr(1, 5, "The cave entrance is blocked off...")
	    windows.msg_win.refresh()

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

        windows.msg_win.clear()
        windows.msg_win.addstr(1, 10, "Chop down this tree? [y/n]")
        windows.msg_win.refresh()
    
        ans = windows.msg_win.getch()

        if ans == ord('y'):

	    temp = []
	
	    self.space.contents[self.name].remove(self)
	    windows.game_win.clear()
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

	self.vicinity = find_vicinity(self.boundaries)

	self.resource_qty = 1

	
    def interact(self, farmer):

        windows.msg_win.clear()
        windows.msg_win.addstr(1, 10, "Break this rock? [y/n]")
        windows.msg_win.refresh()
    
        ans = windows.msg_win.getch()

        if ans == ord('y'):

	    temp = []
	
	    self.space.contents[self.name].remove(self)
	    windows.game_win.clear()
	    farmer.draw()
	    self.space.redraw()

	    for i in xrange(self.resource_qty):
		temp.append(Stone.create())

  	    farmer.inventory.add(temp)

	else:
	    return


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
	

class Cave(Space):

    def __init__(self):

	Space.__init__(self)

	# Used only by Astar
	self.closed_list = []

	self.seed(Room, CAVE_GRAPHICS_DIR + 'room', 3)

	entrance = Entrance(0,
			    10,
			    CAVE_GRAPHICS_DIR + 'entrance_internal',
			    self)

	doors = []

	for room in self.contents['Room']:
	    
	    doors.extend(room.doors)

	Asta = wrapper(Astar)
	halls = Asta(doors, self.closed_list)

	for coor in halls:

	    Hall.create(coor[0], coor[1], CAVE_GRAPHICS_DIR + 'hall', self)


class Room(Node):

    @classmethod
    def create(cls, Ystart, Xstart, graphics_file, space):
	room = Room(Ystart, Xstart, graphics_file, space)
	return room

    def __init__(self, Ystart, Xstart, graphics_file, space):

	self.name = 'Room'

	Node.__init__(self, Ystart, Xstart, graphics_file, space)

	self.doors = []
	self.find_doors()


    def find_doors(self):

	random.seed()

	num_doors = random.randint(1, 2)

	for i in xrange(num_doors):

	    pos = random.choice(self.boundaries)

	    while pos in self.doors:
		pos = random.choice(self.boundaries)

	    self.doors.append(pos)


class Entrance(Node):

    def __init__(self, Ystart, Xstart, graphics_file, space):

	self.name = 'Entrance'

	Node.__init__(self, Ystart, Xstart, graphics_file, space)

	self.doors = [[Ystart + 4, Xstart + 2]]

	self.vicinity = [[Ystart + 1, Xstart + 2]]

	# Make sure the entrance is the first passed to Astar pathfinder
	self.space.contents['Room'].insert(0, self)


    def interact(self, player):

	windows.msg_win.clear()
	windows.msg_win.addstr(1, 5, "Leave the cave? [y/n]")
	windows.msg_win.refresh()

	ans = windows.msg_win.getch()

	while ans != 'y' and ans != 'n':
	    ans = windows.msg_win.getch()

	if ans == 'n':
	    return

	elif ans == 'y':

	    player.current_space = world
	    player.pos = PLAYER_1_START_POS


class Hall(Node):

    @classmethod
    def create(cls, Ystart, Xstart, graphics_file, space):
	hall = Hall(Ystart, Xstart, graphics_file, space)
	return hall

    def __init__(self, Ystart, Xstart, graphics_file, space):

	self.name = 'Hall'

	Node.__init__(self, Ystart, Xstart, graphics_file, space)

