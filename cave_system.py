import random

import farm_config
import expand

from header import *
import windows
from pathfinding import Astar, RoomWrapper
from node import Node
from space import Space


class Cave(Space):

    def __init__(self):

	if farm_config.DEBUG_WIN:
	    windows.debug_win._print("Cave created.")

	self.name = 'Cave'

	Space.__init__(self)

	# Used only by Astar
	self.closed_list = []

	self.seed(Room, CAVE_GRAPHICS_DIR + 'room', 5)

	if farm_config.DEBUG_WIN:
	    windows.debug_win._print("Rooms seeded.")

	entrance = Entrance(0,
			    10,
			    CAVE_GRAPHICS_DIR + 'entrance_internal',
			    self)

	rooms = self.contents['Room']

	self.Astar = RoomWrapper(Astar)
	halls = self.Astar(rooms, self.closed_list)

	if farm_config.DEBUG_WIN:
	    windows.debug_win._print("%d halls found." % len(halls))

	for coor in halls:

	    Hall.create(coor[0], coor[1], CAVE_GRAPHICS_DIR + 'hall', self)

	if farm_config.DEBUG_WIN:
	    windows.debug_win._print("Halls created.")


class Room(Node):

    @classmethod
    def create(cls, Ystart, Xstart, graphics_file, space):
	room = Room(Ystart, Xstart, graphics_file, space)
	return room

    def __init__(self, Ystart, Xstart, graphics_file, space):

	self.name = 'Room'

	Node.__init__(self, Ystart, Xstart, graphics_file, space)

	self.doors = {}
	self.find_doors()


    def find_doors(self):

	random.seed()

	num_doors = random.randint(1, 2)

	if num_doors == 1:
	
	    self.doors.update({'entrance': []})

	elif num_doors == 2:

	    self.doors.update({'entrance': [], 'exit': []})

	ymin = expand.find_min(0, self.boundaries)
	ymax = expand.find_max(0, self.boundaries)
	xmin = expand.find_min(1, self.boundaries)
	xmax = expand.find_max(1, self.boundaries)

	corners = expand.find_corners(ymin, ymax, xmin, xmax)

	for door in self.doors:

	    pos = random.choice(self.boundaries)

	    while pos in corners:

		pos = random.choice(self.boundaries)

	    self.doors[door].extend(pos)


    def draw(self):

	if self.visible:

	    for line in self.graphics:

		for char in line:

		    for door in self.doors:

			if [self.X, self.Y] == self.doors[door]:
			    char == '#'

		    # Check for leading whitespace
		    if char == ' ':
			self.X += 1

		    else:
			break

		line = line.strip().rstrip()

		windows.game_win.addstr(self.Y, self.X, line)

		self.Y += 1
		self.X = self.Xstart

	    self.Y = self.Ystart



class Entrance(Node):

    def __init__(self, Ystart, Xstart, graphics_file, space):

	self.name = 'Entrance'

	Node.__init__(self, Ystart, Xstart, graphics_file, space)

	self.doors = {'exit': [Ystart + 4, Xstart + 2]}

	self.vicinity = [[Ystart + 1, Xstart + 2]]

	# Make sure the entrance is the first passed to Astar pathfinder
	self.space.contents['Room'].insert(0, self)


    def interact(self, player):

	windows.msg_win.clear()
	windows.msg_win.addstr(1, 5, "Leave the cave? [y/n]")
	windows.msg_win.refresh()

	ans = windows.msg_win.getch()

	while ans != ord('y') and ans != ord('n'):
	    ans = windows.msg_win.getch()

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

