import curses
import start_scr
import character_class

# ---------GAME WIN DIMENSIONS ----------

vert = 33
hor = 68

# ---------------------------------------

start_scr.animation()

farmer = character_class.Character()

# ---------- GAMEPLAY --------------------

# win.refresh()
game_win = curses.newwin(vert, hor, 11, 31)
game_win.keypad(1)

game_win.addstr(farmer.pos['y'], farmer.pos['x'], "@")
game_win.refresh()
dir = game_win.getch()
while True:
    if dir in farmer.dirs:
	farmer.move(dir)
	game_win.getch()
    elif dir == ord("q"):
	break
    else:
	pass 

curses.endwin()
