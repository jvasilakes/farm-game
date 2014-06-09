import random

from pathfinding import Astar, wrapper
from node import Node
from singletons import world


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

	    while pos in doors:
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

	msg_win.clear()
	msg_win.addstr(1, 5, "Leave the cave? [y/n]")
	msg_win.refresh()

	ans = msg_win.getch()

	while ans != 'y' and ans != 'n':
	    ans = msg_win.getch()

	if ans = 'n':
	    return

	elif ans = 'y':

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

