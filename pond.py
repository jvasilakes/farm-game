import random

from things import Thing


class Pond(Thing):


    def __init__(self, Ystart, Xstart, graphics):

	Thing.__init__(Ystart, Xstart, graphics)

	self.name = 'Pond'


    def catch_fish(self):

	random.seed

	result = random.randrange(0, 5)

	if result == fish_caught:
	    return fish #############NOT DONE######YETTTT#####
