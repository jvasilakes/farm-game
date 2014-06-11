import random

from header import *
from startup import game_win, msg_win, debug_win
from pathfinding import Astar, wrapper
from node import Node
from space import Space


class Cave(Space):

    def __init__(self):

	debug_win._print("Cave created.")

	self.name = 'Cave'

	Space.__init__(self)

	# Used only by Astar
	self.closed_list = []

	self.seed(Room, CAVE_GRAPHICS_DIR + 'room', 5)

	debug_win._print("Rooms seeded.")

	entrance = Entrance(0,
			    10,
			    CAVE_GRAPHICS_DIR + 'entrance_internal',
			    self)

	doors = []

	for room in self.contents['Room']:
	    
	    doors.extend(room.doors)

	self.Astar = wrapper(Astar)
	halls = self.Astar(doors, self.closed_list)

	for coor in halls:

	    Hall.create(coor[0], coor[1], CAVE_GRAPHICS_DIR + 'hall', self)

	debug_win._print("Halls created.")


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

	msg_win.clear()
	msg_win.addstr(1, 5, "Leave the cave? [y/n]")
	msg_win.refresh()

	ans = msg_win.getch()

	while ans != ord('y') and ans != ord('n'):
	    ans = msg_win.getch()

	if ans == ord('n'):
	    return

	elif ans == ord('y'):

	    player.current_space = Space.members['World']
	    player.pos = PLAYER_1_START_POS


class Hall(Node):

    @classmethod
    def create(cls, Ystart, Xstart, graphics_file, space):
	hall = Hall(Ystart, Xstart, graphics_file, space)
	return hall

    def __init__(self, Ystart, Xstart, graphics_file, space):

	self.name = 'Hall'

	Node.__init__(self, Ystart, Xstart, graphics_file, space)

