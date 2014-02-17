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


    def redraw(self):

	for cls in self.contents:
	    for thing in self.contents[cls]:

		thing.draw()

	game_win.refresh()


    def populate(


world = World()
