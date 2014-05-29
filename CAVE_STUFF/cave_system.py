import curses


room = open('room', 'r'). readlines()
hall_vert = open('hall_vert', 'r').readlines()
hall_horz = open('hall_horz', 'r').readlines()


# ------- CLASSES --------------

class Cave(object):

	def __init__(self):

		self.rooms = []

		self.halls = []

		self.open_list = []
		self.closed_list = []


	def draw(self, win):

		for room in self.rooms:

			room.draw(win)

		for hall in self.halls:

			hall.draw(win)


	def find_hall(self):

	    #TODO: Use A star algorithm here

	def make_hall(self):

		y = self.rooms[0].Ystart + 1

		length = self.rooms[1].Xstart - (self.rooms[0].Xstart + 5)

		for i in range(length - 1):

			Hall.create(y, ((self.rooms[0].Xstart + 6) + i), self)

			self.rooms[1].door_pos = [y + 1, self.rooms[1].Xstart]
			self.rooms[0].door_pos = [y + 1, self.rooms[0].Xstart + 5]


class Node(object):

	def __init__(self, Ystart, Xstart, cave):

		self.Ystart = Ystart
		self.Xstart = Xstart
		self.Y = Ystart
		self.X = Xstart

		self.boundaries = []
		self.find_boundaries()

		for coor in self.boundaries:
			cave.closed_list.append(coor)

		cave.rooms.append(self)


	def find_boundaries(self):
		
		# Starting from Ystart, Xstart add them accordingly
		# with each new line (add to Ystart) or character (add to Xstart)

		for line in self.graphics:

			for char in line:

				if char == '\n':
					pass

				elif char == ' ':
					self.X += 1

				else:
					self.boundaries.append([self.Y, self.X])
					self.X += 1

			self.Y += 1
			self.X = self.Xstart

		self.Y = self.Ystart
		self.X = self.Xstart



class Room(Node):

	def __init__(self, Ystart, Xstart, cave):

		self.graphics = room

		Node.__init__(self, Ystart, Xstart, cave)


	def draw(self, win):

		[y, x] = [self.Ystart, self.Xstart]

		for line in self.graphics:

			line = line.strip().rstrip()

			for char in line:

				if [y, x] == self.door_pos:
					x += 1

				else:
					win.addstr(y, x, char)
					x += 1

			y += 1
			x = self.Xstart


class Hall(Node):

	@classmethod
	def create(cls, Ystart, Xstart, cave):
		hall = Hall(Ystart, Xstart, cave)
		return hall


	def __init__(self, Ystart, Xstart, cave):

		self.graphics = hall_horz

		Node.__init__(self, Ystart, Xstart, cave)


	def draw(self, win):

		y = self.Ystart
		x = self.Xstart

		for line in self.graphics:

			line = line.strip().rstrip()

			win.addstr(y, x, line)

			y += 1
			x = self.Xstart


# --------- MAIN ---------------

scr = curses.initscr()
curses.curs_set(0)

win = curses.newwin(50, 100, 0, 0)

cave = Cave()

room1 = Room(5, 5, cave)
room2 = Room(5, 20, cave)

cave.make_hall()

cave.draw(win)
win.refresh()

win.getch()

curses.endwin()
