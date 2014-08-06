import random
import collections

import debug_console
from header import *


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
	if 'Character' in obj.get_base():
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


    def redraw(self, window):

	window.clear()

	for key in self.characters:
	    for character in self.characters[key]:

	        character.draw(window)

	for key in self.contents:
	    for obj in self.contents[key]:

		obj.draw(window)

	window.refresh()


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

	    for pet in self.characters['Pet']:
		debug_console.get()._print("Moving pet.")
		pet.AI_move(self.characters['Player'][0])

	    for npc in self.characters['NPC']:
		debug_console.get()._print("Moving npc.")
		npc.AI_move()

	except Exception as e:
	    debug_console.get()._print(str(e))
	    return


    def sort_contents(self):

	self.contents = collections.OrderedDict(sorted(self.contents.items()))

	for key in self.contents:

	    for n in xrange(len(self.contents[key]) - 1):

		for i in xrange(len(self.contents[key]) - 1, 0, -1):

		    node = self.contents[key][i]
		    prev_node = self.contents[key][i - 1]

		    # If prev_node is in front of node
		    if node.Ystart < prev_node.Ystart:

			# Swap them so node is drawn first
			temp = node
			self.contents[key][i] = prev_node
			self.contents[key][i - 1] = temp
			
		    else:
			pass

