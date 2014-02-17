from things import Thing


class Plant(Thing):

    def __init__(self, Ystart, Xstart, graphics):

	Thing.__init__(self, Ystart, Xstart, graphics)

	self.name = 'Crop'

        self.stage = 1


    def grow(self):


	if self.stage < 3:
	    self.stage += 1
	    self.graphics = 'GRAPHICS/plant' + str(self.stage)

	else:
	    return


    def get_stage(self):

	return self.stage
