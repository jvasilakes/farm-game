import plant


class List(object):

    def __init__(self):

	self.things = {'plants' : [], 'doors' : [], 'misc' : []}


    def append(self, thing):

	if isinstance(thing, plant.Plant):
	    self.things['plants'].append(thing)

	else:
	    self.things['misc'].append(thing)  #if not an explicit
				 	       #subclass of Thing,
					       #append it to 'misc',
					       #else, append it to
					       #its respective entry

    def redraw(self, window):

	for clas in self.things:
	    for thing in self.things[clas]:

 	        thing.draw()

	window.refresh()



list = List()
