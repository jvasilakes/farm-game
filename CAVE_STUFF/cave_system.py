import curses


room = open('room', 'r'). readlines()
hall_vert = open('hall_vert', 'r').readlines()
hall_horz = open('hall_horz', 'r').readlines()


# ------- CLASSES --------------

class Cave(object):

    def __init__(self):

	self.rooms = []

	self.halls = []

	self.walls = []


    def draw(self, win):

	for room in self.rooms:

	    room.draw(win)

	for hall in self.halls:

	    hall.draw(win)


    def build_hall(self):

	log = open('logfile', 'a')

	complete = False	

	start = self.rooms[0].door_pos = [self.rooms[0].Ystart + 1, self.rooms[0].Xstart + 5]

	end = self.rooms[1].door_pos = [self.rooms[1].Ystart + 1, 20]

	current = start

	log.write("current: ")
	log.write(str(current))
	log.write('\n')

	log.write("end: ")
	log.write(str(end))
	log.write('\n')
	
	self.rooms[0].closed_list.append(start)
	self.rooms[0].closed_list.append([start[0], start[1] - 1])
	self.rooms[0].closed_list.append([start[0] + 1, start[1]])
	self.rooms[0].closed_list.append([start[0] - 1, start[1]])

	self.rooms[0].open_list.append([start[0], start[1] + 1])

	log.write("Initial closed list: ")
	log.write(str(self.rooms[0].closed_list))
	log.write('\n')

	log.write("Initial open list: ")
	log.write(str(self.rooms[0].open_list))
	log.write('\n')

	while not complete:
	
	    best = self.find_best_tile(self.rooms[0].open_list, start, end) 
	
	    log.write("Open list: ")
	    log.write(str(self.rooms[0].open_list))
	    log.write('\n')
	    log.write("Best in list: " + str(best) + '\n')

	    if best[0] == current[0]:
		Hall.create('H', best[0], best[1], self)
		log.write("Horz hall created at X %d!\n" % best[1])

	    else:
		Hall.create('V', best[0], best[1], self)
		log.write("Vert hall created! at Y %d!\n" % best[0])

	    current = best
	    log.write("Current tile updated!\n")

	    walkable = [[current[0] - 1, current[1]],
			[current[0] + 1, current[1]],
			[current[0], current[1] - 1],
			[current[0], current[1] + 1]]

	    index = self.rooms[0].open_list.index(current)
	
	    log.write("Index: " + str(index) + '\n')

	    tile = self.rooms[0].open_list.pop(index)

	    self.rooms[0].closed_list.append(tile)

	    log.write("NEW Open list: ")
	    log.write(str(self.rooms[0].open_list))
	    log.write('\n')
	    log.write("NEW closed list: ")
	    log.write(str(self.rooms[0].closed_list))
	    log.write('\n')

	    log.write("current: ")
	    log.write(str(current))
	    log.write('\n')
	
	    for tile in walkable:

		log.write(str(tile))
		log.write('\n')

		if tile == end:
		    complete = True

		if tile in self.rooms[0].closed_list:
		    pass

		if tile not in self.rooms[0].open_list:
		    self.rooms[0].open_list.append(tile) 
							
	log.close()

    def calc_score(self, tile, start, end):

	# Movement cost from start tile to current tile
	G = abs((tile[0] - start[0]) + (tile[1] - start[1]))

	# Movement cost from current tile to destination tile
	H = abs((end[0] - tile[0]) + (end[1] - start[1]))

	score = G + H

	return score


    def find_best_tile(self, list, start, end):

	min = self.calc_score(list[0], start, end)

	for tile in list:
	    if self.calc_score(tile, start, end) < min:
		min = self.calc_score(tile, start, end)
		best = tile

	return tile


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
	    cave.walls.append(coor)

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

	self.open_list = []
	self.closed_list = []



    def draw(self, win):

	[y, x] = [self.Ystart, self.Xstart]

	for line in self.graphics:

	    line = line.strip().rstrip()

	    for char in line:

		#if [y, x] == self.door_pos:
		    #x += 1

		#else:
		win.addstr(y, x, char)
		x += 1

	    y += 1
	    x = self.Xstart


class Hall(Node):

    @classmethod
    def create(cls, dir, Ystart, Xstart, cave):
	hall = Hall(dir, Ystart, Xstart, cave)
	return hall


    def __init__(self, dir, Ystart, Xstart, cave):

	if dir == 'H':
	    self.graphics = hall_horz

	elif dir == 'V':
	    self.graphics == hall_vert

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

win.addstr(0, 0, "CAVE!")
win.refresh()

cave = Cave()

room0 = Room(5, 5, cave)
room1 = Room(7, 20, cave)

cave.build_hall()

cave.draw(win)
win.refresh()

win.getch()

curses.endwin()
