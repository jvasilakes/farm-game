import random

from pathfinding import Astar, wrapper
from world import World
from node import Node


class Cave(World):

    def __init(self):

	self.contents = {}

	self.characters = {}

	# Used only by Astar
	self.closed_list = []

	self.seed(room, CAVE_GRAPHICS_DIR + 'room', 3)
	
	Astar = wrapper(Astar)

	halls = Astar(self.contents['Room'], closed_list)



class Room(Node):

    @classmethod
    def create(cls, Ystart, Xstart, graphics_file):
	room = Room(Ystart, Xstart, graphics_file)
	return room

    def __init__(self, Ystart, Xstart, graphics_file):

	self.name = 'Room'

	Node.__init__(self, Ystart, Xstart, graphics_file)

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

    def __init__(self, Ystart, Xstart, graphics_file):

	self.name = 'Entrance'

	Node.__init__(self, Ystart, Xstart, graphics_file)

	self.doors = [[Ystart + 4, Xstart + 2]]

	self.vicinity = [[Ystart + 1, Xstart + 2]]


    def interact(self, player):

	pass

	# TODO:
	# Prompt user if they really want to exit the cave
	# If yes, exit cave.


class Hall(Node):

    @classmethod
    def create(cls, Ystart, Xstart, graphics_file):
	hall = Hall(Ystart, Xstart, graphics_file)
	return hall

    def __init__(self, Ystart, Xstart, graphics_file):

	self.name = 'Hall'

	Node.__init__(self, Ystart, Xstart, graphics_file)

