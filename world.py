import random
from windows import game_win


class World(object):

    def __init__(self):

        # Each key in the dictionary is the name of some class (e.g. 'Crop' or 'Tree').
	# Each newly created object is appended to a sublist under it's respective key
	# in this dictionary during it's __init__() routine via the add() function 
	# below.
	
	self.contents = {}	

  
    def add(self, thing):

	if thing.name in self.contents:
	    self.contents[thing.name].append(thing)

	else:
	    # Create a new key with the class name and an empty list,
	    self.contents.update(zip([thing.name], [[]]))
	    # then append 'thing' to that list.
	    self.contents[thing.name].append(thing)


    def remove(self, thing):

	self.contents[thing.name].remove(thing)
	    


    def redraw(self):

	for key in self.contents:
	    for thing in self.contents[key]:

		thing.draw()

	game_win.refresh()


    def populate(self, obj, graphics, number):
	
	random.seed()

	for i in xrange(number):
	    # 26 is maximum y value
	    y = random.randrange(1, 26)
	    # 60 is maximum x value
	    x = random.randrange(1, 60)
	    thing = obj.create(y, x, graphics)	

	    if thing.intersection:
	        n = 0

	        while thing.intersection and n < 3:    # Retry up to 3 times
	            y = random.randrange(1, 26)
	            x = random.randrange(1, 60)
	            obj.create(y, x, graphics)	
		    n += 1


    def updateAll(self, key, function):   # TODO: finish this

	if key not in self.contents:
	    return

	else:
		
	    try:
	        for obj in self.contents[key]:
		    obj.function()	
		    
	    except:
	    	return


    def grow_crops(self):     # THIS IS WHAT updateAll() SHOULD DO. GET RID OF THIS

	try:

	    for crop in self.contents['Crop']:
	        crop.grow()

	except:
	    return


world = World()
