from things import Thing


class House(Thing):


    def __init__(self, Ystart, Xstart, graphics):

	Thing.__init__(Ystart, Xstart, graphics)

	self.name = 'House'

	self.door = [(Ystart + 5), (Xstart + 5)]
