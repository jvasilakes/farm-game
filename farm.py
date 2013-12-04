import curses

scr = curses.initscr()

# ---------GAME WIN DIMENSIONS ----------

vert = 33
hor = 68

# ---------------------------------------
# --------- CHARACTER POSITION ----------

y = 5
x = 5

# ---------------------------------------

win = curses.newwin(35, 70, 10, 30)
win.box()
win.refresh()
game_win = curses.newwin(33, 68, 11, 31)
game_win.keypad(1)

game_win.addstr(y, x, "@")
game_win.refresh()
ch = game_win.getch()
while True:
    if ch == curses.KEY_UP:
	if y == 0:
	    pass
	else:
	    y -= 1
	    game_win.clear()
	    game_win.addstr(y, x, "@")
	    game_win.refresh() 
	ch = game_win.getch()
    elif ch == curses.KEY_DOWN:
	if y == (vert - 1):
	    pass
	else:
	    y += 1
	    game_win.clear()
	    game_win.addstr(y, x, "@")
	    game_win.refresh() 
	ch = game_win.getch()
    elif ch == curses.KEY_RIGHT:
	if x == (hor - 2):
	    pass
	else:
	    x += 1
	    game_win.clear()
	    game_win.addstr(y, x, "@")
	    game_win.refresh() 
	ch = game_win.getch()
    elif ch == curses.KEY_LEFT:
	if x == 0:
	    pass
	else:
	    x -= 1
	    game_win.clear()
	    game_win.addstr(y, x, "@")
	    game_win.refresh() 
	ch = game_win.getch()
    elif ch == ord("q"):
	break
    else:
	pass 

curses.endwin()
