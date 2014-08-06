import os
import time
import curses

from header import *


def display(graphic, window, y, x):

    """ graphic must be a readlines list! """

    for line in graphic:
	line = line.rstrip()
	window.addstr(y, x, line)
	y += 1


def intro(win):

    tree1 = open('GRAPHICS/INTRO/tree1', 'r').readlines()
    tree2 = open('GRAPHICS/INTRO/tree2', 'r').readlines()
    farm_logo = open('GRAPHICS/INTRO/farm_logo', 'r').readlines()

    for i in xrange(3):
        win.clear()
        display(tree1, win, INTRO_ANIM_POS_Y, INTRO_ANIM_POS_X)
        win.refresh()
        time.sleep(1)
        win.clear()
        display(tree2, win, INTRO_ANIM_POS_Y, INTRO_ANIM_POS_X)
        win.refresh()
        time.sleep(1)

    """
    logo_win = curses.newwin(
	LOGO_WIN_SIZE_Y,
	LOGO_WIN_SIZE_X,
	LOGO_WIN_POS_Y,
	LOGO_WIN_POS_X
	)

    display(farm_logo, logo_win, 0, 0)
    logo_win.refresh()
    time.sleep(2)
    """


def sunrise(win):

    files = os.listdir(SUNRISE_DIR)
    files.sort()

    for file in files:
	graphic = open(SUNRISE_DIR + file).readlines()
	win.clear()
	display(graphic, win, 0, 0)
	time.sleep(0.5)
	win.refresh()

    display(graphic, win, 0, 0)
    time.sleep(3)
    win.refresh()

