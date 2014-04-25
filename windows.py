import curses
import time

from farm_config import *

from animations import display



#--------GAME WIN-------------------------------


def start_gamewin():

    curses.initscr()
    curses.noecho()
    curses.curs_set(0)

    win = curses.newwin(33, 66, 4, 0)
    win.keypad(1)

    return win


def intro(win):

    tree1 = open('GRAPHICS/INTRO/tree1').readlines()
    tree2 = open('GRAPHICS/INTRO/tree2',).readlines()
    farm = open('GRAPHICS/INTRO/farm_logo',).readlines()

    i = 0
    while i <= 3:
        display(tree1, win, 3, 1)
        win.refresh()
        time.sleep(1)
        win.clear()
        display(tree2, win, 3, 1)
        win.refresh()
        time.sleep(1)
        win.clear()
        i += 1

    txt_win = curses.newwin(6, 29, 13, 20)
    display(farm, txt_win, 0, 0)
    txt_win.refresh()
    time.sleep(2)

    # TODO make this use msg_win
    start_win = curses.newwin(1, 25, 34, 23)
    start_win.addstr(0, 0, "Press any key to start.")
    start_win.refresh()
    start_win.getch()
    start_win.clear()
    start_win.refresh()



#----------MSG WIN--------------------------------------

def start_msgwin(HELP_SCREEN):

    win = curses.newwin(3, 68, 0, 0)
    win.keypad(1)

    if HELP_SCREEN:

	win.addstr(1, 25, "Welcome to Farm!")
	win.addstr(2, 30, "-->")
	win.refresh()
	win.getch()
        win.clear()

	win.addstr(1, 25, "'wasd' to move.")
	win.addstr(2, 30, "-->")
        win.refresh()
	win.getch()
	win.clear()

	win.addstr(1, 12, "'p' to plant a crop. 'h' to harvest it.")
	win.addstr(2, 30, "-->")
	win.refresh()
	win.getch()
	win.clear()

	win.addstr(1, 25, "'k' to interact.")
	win.addstr(2, 22, "Press any key to begin.")
	win.refresh()
	win.getch()
	win.clear()

	win.refresh()

    return win



#----------DEBUG WIN-------------------------------------

class debug_console(object):

    def __init__(self):
        self.win = curses.newwin(200, 90, 3, 80)
        self.win.keypad(1)
	self.header = curses.newwin(2, 20, 0, 100)
	self.header.addstr(0, 0, "DEBUGGING CONSOLE")
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

game_win = start_gamewin()

if INTRO:
    intro(game_win)

msg_win = start_msgwin(HELP_SCREEN)

if DEBUG_WIN:
    debug_win = debug_console()
