import os
import time

from header import *


# NOTE: MUST USE A READLINES OBJECT
def display(graphic, window, y, x):

    for line in graphic:
	line = line.rstrip()
	window.addstr(y, x, line)
	y += 1


def sunrise(window):

    files = os.listdir(SUNRISE_DIR)
    files.sort()

    for file in files:
	graphic = open(SUNRISE_DIR + file).readlines()
	window.clear()
	display(graphic, window, 0, 0)
	time.sleep(0.5)
	window.refresh()

    display(graphic, window, 0, 0)
    time.sleep(3)
    window.refresh()
