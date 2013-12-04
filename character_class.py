import curses

class Character(object):
    def __init__(self):
	self.player = "@"
	self.pos = {'y': 5, 'x': 5}
	self.dirs = {'UP': curses.KEY_UP, 'DOWN': curses.KEY_DOWN, 'LEFT': curses.KEY_LEFT, 'RIGHT': curses.KEY_RIGHT}

    def move(self, dir):
	key = self.dirs
	if dir == key['UP']:
	    if self.pos['y'] == 0:
		pass
	    else:
		self.pos['y'] -= 1
		game_win.clear()
		game_win.addstr(self.pos['y'], self.pos['x'], self.player)
		game_win.refresh()
	elif dir == key['DOWN']:
	    if self.pos['y'] == (33 - 1): # 33 will be a var 'vert'
		pass
	    else:
		self.pos['y'] += 1
		game_win.clear()
		game_win.addstr(self.pos['y'], self.pos['x'], self.player)
		game_win.refresh()
	elif dir == key['LEFT']:
	    if self.pos['x'] == 0:
		pass
	    else:
		self.pos['x'] -= 1
		game_win.clear()
		game_win.addstr(self.pos['y'], self.pos['x'], self.player)
		game_win.refresh()
	elif dir == key['RIGHT']:
	    if self.pos['x'] == (68 - 2): # 68 will be a var 'hor'
		pass
	    else:
		self.pos['x'] += 1
		game_win.clear()
		game_win.addstr(self.pos['y'], self.pos['x'], self.player)
		game_win.refresh()
	else:
	    pass
