from thing import Thing


class Plant(Thing):

    def __init__(self, Ystart, Xstart, graphics):

	self.name = 'Plant'

        self.stage = 1

	self.value = 5

	Thing.__init__(self, Ystart, Xstart, graphics)


    def grow(self):


	if self.stage < 3:
	    self.stage += 1
	    self.graphics = 'GRAPHICS/plant' + str(self.stage)

	else:
	    return


    def get_stage(self):

	return self.stage
