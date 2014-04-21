import random
from windows import game_win
from character import Character 


class World(object):

    def __init__(self):

	self.contents = {}

	self.characters = {}

  
    def add(self, thing):

	# First, choose the list to modify according
	# to what type of thing we're dealing with.
	if isinstance(thing, Character):
	    list = self.characters

	else:
	    list = self.contents


	# Then update the list as necessary
	if thing.name in list:
	    list[thing.name].append(thing)

	else:
	    list.update(zip([thing.name], [[]]))
	    list[thing.name].append(thing)


    def remove(self, thing):

	# First, choose the list to modify according
	# to what type of thing we're dealing with.
	if isinstance(thing, Character):
	    list = self.characters

	else:
	    list = self.contents


	# Then update the list as necessary
	try:
	    list[thing.name].remove(thing)

	except:
	    return


    def redraw(self):

	game_win.clear()

	for cls in self.contents:
	    for thing in self.contents[cls]:

		thing.draw()

	#farmer.draw()

	game_win.refresh()


    def populate(self, thing, graphics, number):
	
	random.seed()

	for i in xrange(number):
	    y = random.randrange(1, 26)
	    x = random.randrange(1, 60)
	    obj = thing.create(y, x, graphics)	

	    if obj.intersection:
	        n = 0

	        while obj.intersection and n < 3:    # Retry up to 3 times
	            y = random.randrange(1, 26)
	            x = random.randrange(1, 60)
	            thing.create(y, x, graphics)	
		    n += 1


    def updateAll(self, function):  

	try:
	    for instance in self.contents['thing']:
		instance.function()	

	except:
	    return

    def grow_crops(self):     # THIS IS ONLY TEMPORARY, DEPRECATE THIS

	try:

	    for crop in self.contents['Crop']:
	        crop.grow()

	except:
	    return


world = World()
