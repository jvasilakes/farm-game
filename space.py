import random

from header import *
from startup import game_win


class Space(object):

    members = {}

    def __init__(self):

        # Each key in the dictionary is the name of some class (e.g. 'Crop', 
	# 'Tree', or 'Player').  Each newly created object is appended to a 
	# sublist under it's respective key in this dictionary via the add()
	# function below.
	
	self.contents = {}	

	self.characters = {}

	self.members.update({self.name: self})

  
    def add(self, obj):

	# First, choose which list to modify according
	# to what type of thing we're dealing with.
	if obj.name == 'Player' or obj.name == 'NPC':
	    list = self.characters

	else:
	    list = self.contents

	# Then update the list as necessary.
	if obj.name in list:
	    list[obj.name].append(obj)

	else:
	    # Create a new key with the class name and an empty list.
	    list.update(zip([obj.name], [[]]))

	    list[obj.name].append(obj)


    def remove(self, obj):

	# First, choose the list to modify according
	# to what type of obj we're dealing with.
	if obj.name == 'Player' or obj.name == 'NPC':
	    list = self.characters

	else:
	    list = self.contents


	# Then update the list as necessary
	try:
	    list[obj.name].remove(obj)

	except:
	    return


    def redraw(self):

	game_win.clear()

	for key in self.characters:
	    for character in self.characters[key]:

	        character.draw()

	for key in self.contents:
	    for obj in self.contents[key]:

		obj.draw()

	game_win.refresh()


    # Initializes <number> amount of <obj> objects
    # but does not draw them in the world.
    def seed(self, obj, graphics, number):
	
	random.seed()

	for i in xrange(number):
	    y = random.randrange(1, GAME_WIN_SIZE_Y-5)
	    x = random.randrange(1, GAME_WIN_SIZE_X-5)
	    thing = obj.create(y, x, graphics, self)	

	    if thing.intersection:

	        n = 0
	        while thing.intersection and n < 3:    # Retry up to 3 times
	            y = random.randrange(1, GAME_WIN_SIZE_Y-5)
	            x = random.randrange(1, GAME_WIN_SIZE_X-5)
	            obj.create(y, x, graphics, self)	
		    n += 1


    def updateNPCs(self):

	try:

	    for npc in self.characters['NPC']:
		npc.AI_move()

	except:
	    return


    # TODO: Fix this so that it actually works.
    # Sorts all objects by order of Ystart value (highest to lowest.)
    def sort_contents(self, key):

	for n in xrange(len(self.contents[key]) - 1):

	    for i in xrange(len(self.contents[key]), 1, -1):

		node = self.contents[key][i]
		prev_node = self.contents[key][i - 1]

		# If node is in front of prev_node
		if node.Ystart < prev_node.Ystart:

		    # Swap them so node is drawn first
		    temp = node
		    self.contents[key][i] = prev_node
		    self.contents[key][i - 1] = temp
		    
		else:
		    pass

