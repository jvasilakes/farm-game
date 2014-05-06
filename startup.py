import curses
import time

from header import *
from farm_config import *

from animations import display


# TODO finish this
def writeScreenInfo(max_height, max_width):

    if GAME_WIN_SIZE_Y > max_height or GAME_WIN_SIZE_X > max_width \
	or GAME_WIN_SIZE_Y < INTRO_ANIM_SIZE_Y or GAME_WIN_SIZE_X < INTRO_ANIM_SIZE_X:

	curses.endwin()
	print("Incompatible game_win size!")    

    MSG_WIN_SIZE_Y = GAME_WIN_POS_Y - 1
    if MSG_WIN_SIZE_Y < 3:
	curses.endwin()
	print("incompatible msg_win size!")

    file = open('screenInfo.conf', 'w')


#--------GAME WIN-------------------------------


def start_gamewin():

    stdscr = curses.initscr()
    curses.noecho()
    curses.curs_set(0)

    game_win = curses.newwin(
	GAME_WIN_SIZE_Y,
	GAME_WIN_SIZE_X,
	GAME_WIN_POS_Y,
	GAME_WIN_POS_X
	)

    game_win.keypad(1)

    return game_win


def intro(win):

    tree1 = open('GRAPHICS/INTRO/tree1').readlines()
    tree2 = open('GRAPHICS/INTRO/tree2',).readlines()
    farm_logo = open('GRAPHICS/INTRO/farm_logo',).readlines()

    for i in xrange(3):
        display(tree1, win, 3, 1)
        win.refresh()
        time.sleep(1)
        win.clear()
        display(tree2, win, 3, 1)
        win.refresh()
        time.sleep(1)
        win.clear()

    txt_win = curses.newwin(
	TXT_WIN_SIZE_Y,
	TXT_WIN_SIZE_X,
	TXT_WIN_POS_Y,
	TXT_WIN_POS_X
	)

    display(farm_logo, txt_win, 0, 0)
    txt_win.refresh()
    time.sleep(2)



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
        self.win = curses.newwin(200, 90, 3, 80)
        self.win.keypad(1)
	self.header = curses.newwin(2, 20, 0, 100)
	self.header.addstr(0, 1, "DEBUGGING CONSOLE")
	self.header.refresh()

	self.ynow = 0

    def prnt(self, message):
	if self.ynow >= 40:
	    self.clear()
	    self.ynow = 0

	else:
	    self.win.addstr(self.ynow, 0, message)
	    self.win.refresh()
	    self.ynow += 1	


    def clear(self):
	self.win.clear()
	self.win.refresh()


#---------- INITIALIZATION ----------------------------

game_win = start_gamewin()

if INTRO:
    intro(game_win)

msg_win = start_msgwin()

if DEBUG_WIN:
    debug_win = debug_console()

