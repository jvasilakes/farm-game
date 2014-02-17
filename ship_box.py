from things import Thing
from inventory import Inventory


class Shipbox(Thing):


    def __init__(self, Ystart, Xstart, graphics):

	Thing.__init__(Ystart, Xstart, graphics)

	self.name = 'Shipbox'

	self.contents = Inventory()
