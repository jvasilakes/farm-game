import random

from header import *
from startup import game_win
from world import world



class Node(object):

    list = []

    @classmethod
    def drawAll(cls):

	for node in Node.list:
	    node.draw()


    def __init__(self, Ystart, Xstart, graphics_file):

	# y, x coordinates of the top left corner of the graphic
	self.Ystart = Ystart
	self.Xstart = Xstart
	self.Y = Ystart
	self.X = Xstart

	self.graphics = self.load_graphics(graphics_file)

	self.boundries = []
	self.find_boundries()

	self.vicinity = []

	self.intersection = self.intersects()

	if ALL_VISIBLE:
	    self.visible = True

	else:
	    self.visible = False

	# If it intersects with something else, delete it's boundries
	# and don't add it to the world.
	if self.intersection:
	    del self.boundries

	else:
	    Node.list.append(self)
	    world.add(self)


    def find_boundries(self):
	
	# Starting from Ystart, Xstart add them accordingly
	# with each new line (add to Ystart) or character (add to Xstart)

	for line in self.graphics:

	    for char in line:

		if char == '\n':
		    pass

		elif char == ' ':
		    self.X += 1

		else:
	            self.boundries.append([self.Y, self.X])
		    self.X += 1

	    self.Y += 1
	    self.X = self.Xstart

	self.Y = self.Ystart
	self.X = self.Xstart


    def intersects(self):
	
	for node in Node.list:

	    for n in xrange(len(self.boundries)):

		if self.boundries[n] in node.boundries \
		    or self.boundries[n] == PLAYER_1_START_POS \
		    or self.boundries[n] == DOG_START_POS: 

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

