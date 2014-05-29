import time
import curses

from header import *
from farm_config import *

from animations import display, intro



#--------GAME WIN-------------------------------


def start_gamewin():

    game_win = curses.newwin(
	GAME_WIN_SIZE_Y,
	GAME_WIN_SIZE_X,
	GAME_WIN_POS_Y,
	GAME_WIN_POS_X
	)

    game_win.keypad(1)

    return game_win


#----------MSG WIN--------------------------------------

def start_msgwin():

    win = curses.newwin(
	MSG_WIN_SIZE_Y,
	MSG_WIN_SIZE_X,
	MSG_WIN_POS_Y,
	MSG_WIN_POS_X
	)

    win.keypad(1)

    if HELP_SCREEN:

	win.addstr(1, 23, "Press [ENTER] to play.")
	win.addstr(2, 28, "'?' for help.")
	win.refresh()
	ans = win.getch()

	if ans == ord('?'):
	    win.clear()
	    show_help_screen()

	else:
	    pass

	win.clear()
	win.refresh()

    return win



#--------- HELP_WIN -------------------------------------

def show_help_screen():
	
    help_win = curses.newwin(
	HELP_WIN_SIZE_Y,
	HELP_WIN_SIZE_X,
	HELP_WIN_POS_Y,
	HELP_WIN_POS_X
	)

    help_win.addstr(1, 6, "CONTROLS")
    help_win.addstr(3, 1, "'wasd': move")
    help_win.addstr(4, 1, "'k': interact")
    help_win.addstr(5, 1, "'p': plant a crop")
    help_win.addstr(6, 1, "'h': harvest a crop")
    help_win.addstr(7, 1, "'i': inventory")
    help_win.addstr(8, 1, "'q': quit")

    help_win.box()

    help_win.refresh()

    help_win.getch()

    help_win.clear()
    help_win.refresh()


#----------DEBUG WIN-------------------------------------

class debug_console(object):

    def __init__(self):
        self.win = curses.newwin(
	    DEBUG_WIN_SIZE_Y,
	    DEBUG_WIN_SIZE_X,
	    DEBUG_WIN_POS_Y,
	    DEBUG_WIN_POS_X
	    )

        self.win.keypad(1)

	self.header = curses.newwin(
	    DEBUG_TITLE_SIZE_Y,
	    DEBUG_TITLE_SIZE_X,
	    DEBUG_TITLE_POS_Y,
	    DEBUG_TITLE_POS_X
	    )

	self.header.addstr(0, 1, "DEBUGGING CONSOLE")
	self.header.refresh()

	self.ynow = 0


    def prnt(self, message):
    
	if self.ynow >= DEBUG_WIN_SIZE_Y:
	    self.clear()
	    self.ynow = 0

	self.win.addstr(self.ynow, 0, message)

	count = 0
	for char in message:
	    count += 1

	if count >= DEBUG_WIN_SIZE_X:
	    self.ynow += 1

	self.win.refresh()
	self.ynow += 1	


    def clear(self):
	self.win.clear()
	self.win.refresh()


#---------- INITIALIZATION ----------------------------

curses.initscr()
curses.noecho()
curses.curs_set(0)

game_win = start_gamewin()

if INTRO:
    intro(game_win)

msg_win = start_msgwin()

if DEBUG_WIN:
    debug_win = debug_console()

