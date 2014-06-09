import random

from header import *
from farm_config import ALL_VISIBLE
from startup import game_win



class Node(object):

    # Add new parameter 'space' which will be the space to which
    # the new Node instance will be added.
    def __init__(self, Ystart, Xstart, graphics_file, space):

	self.space = space

	# y, x coordinates of the top left corner of the graphic
	self.Ystart = Ystart
	self.Xstart = Xstart
	self.Y = Ystart
	self.X = Xstart

	self.graphics = self.load_graphics(graphics_file)

	self.boundaries = []
	self.find_boundaries()

	self.vicinity = []

	if ALL_VISIBLE:
	    self.visible = True

	else:
	    self.visible = False

	self.intersection = self.intersects()  #Boolean

	# If it intersects with something else, delete it's boundaries
	# and don't add it to the world.
	if self.intersection:
	    del self.boundaries
	    return

	else:
	    space.add(self)


    def find_boundaries(self):
	
	# Starting from Ystart, Xstart add them accordingly
	# with each new line (add to Ystart) or character (add to Xstart)

	for line in self.graphics:

	    for char in line:

		if char == '\n':
		    pass

		elif char == ' ':
		    self.X += 1

		else:
	            self.boundaries.append([self.Y, self.X])
		    self.X += 1

	    self.Y += 1
	    self.X = self.Xstart

	self.Y = self.Ystart
	self.X = self.Xstart


    def intersects(self):
	
	for key in self.space.contents:

	    for obj in self.space.contents[key]: 

		for n in xrange(len(self.boundaries)):

		    if self.boundaries[n] in obj.boundaries \
			or self.boundaries[n] == PLAYER_1_START_POS \
			or self.boundaries[n] == DOG_START_POS: 

			return True

		    else:
			pass
	    
	return False
	    

    def load_graphics(self, graphics_file):

	graphics = open(graphics_file, 'r').readlines()

	return graphics


    def draw(self):

	if self.visible:

	    for line in self.graphics:

		for char in line:

		    # Check for leading whitespace
		    if char == ' ':
			self.X += 1

		    else:
			break

		line = line.strip().rstrip()

		game_win.addstr(self.Y, self.X, line)

		self.Y += 1
		self.X = self.Xstart

	    self.Y = self.Ystart


    def interact(self, player):

	""" Default interact function

	Will do nothing if not defined in 
	some subclass of node.

	"""
	
	pass
