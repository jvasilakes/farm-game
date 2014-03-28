import random
from windows import game_win
from world import world



class Thing(object):

    def __init__(self, Ystart, Xstart, graphics):

	self.Ystart = Ystart
	self.Xstart = Xstart
	self.Y = Ystart
	self.X = Xstart

	self.graphics = graphics

	self.boundries = []
	self.find_boundries()

	self.vicinity = []

	self.intersection = True
	self.intersects()

	if self.intersection:
	    del self.boundries

	else:
	    world.add(self)
	    self.draw()
	

    def find_boundries(self):
	
	file = open(self.graphics, 'r')

	for line in file:

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

	self.X = self.Xstart
	self.Y = self.Ystart


    def get_boundries(self):

	return self.boundries


    def intersects(self):
	
	for clas in world.contents:

	    for thing in world.contents[clas]:

		for n in xrange(len(self.boundries)):

		    if self.boundries[n] in thing.get_boundries() \
		       or self.boundries[n] == [6, 6]:

		        self.intersection = True
		        return

		    else:
		         pass
	
	self.intersection = False
	    

    def draw(self):

        file = open(self.graphics, 'r')

        for line in file:

	    for char in line:

		if char == ' ':
		    self.X += 1

		else:
		    break

	    line = line.strip().rstrip()

            game_win.addstr(self.Y, self.X, line)

	    self.Y += 1
	    self.X = self.Xstart

	self.Y = self.Ystart

	file.close()
