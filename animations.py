import os
import time


def display(graphics, window, y, x):

    for line in graphics:
	line = line.rstrip()
	window.addstr(y, x, line)
	y += 1


def sunrise(window):

    files = os.listdir('GRAPHICS/SUNRISE/')
    files.sort()

    for file in files:
	pic = open('GRAPHICS/SUNRISE/' + file).readlines()
	window.clear()
	display(pic, window, 0, 0)
	time.sleep(0.5)
	window.refresh()
