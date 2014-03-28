import random
from windows import game_win


class World(object):

    def __init__(self):

	self.contents = {}

  
    def add(self, thing):

	if thing.name in self.contents:
	    self.contents[thing.name].append(thing)

	else:
	    self.contents.update(zip([thing.name], [[]]))
	    self.contents[thing.name].append(thing)


    def remove(self, thing):

	self.contents[thing.name].remove(thing)
	    


    def redraw(self):

	for cls in self.contents:
	    for thing in self.contents[cls]:

		thing.draw()

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


    def updateAll(self, thing, function):   # TODO: finish this

	if thing not in self.contents:
	    return

	else:
	    for instance in self.contents['thing']:
		instance.function()	


    def grow_crops(self):     # THIS IS ONLY TEMPORARY, DEPRECATE THIS

	try:

	    for crop in self.contents['Crop']:
	        crop.grow()

	except:
	    return


world = World()
