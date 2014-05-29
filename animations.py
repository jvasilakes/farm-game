import os
import time
import curses

from header import *


# NOTE: MUST USE A READLINES OBJECT
def display(graphic, window, y, x):

    for line in graphic:
	line = line.rstrip()
	window.addstr(y, x, line)
	y += 1


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
