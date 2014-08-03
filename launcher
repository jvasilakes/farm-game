#!/usr/bin/python2.7

from os import system
import curses

import screenInfo


def main():

    (max_y, max_x) = get_screen_info()

    if max_y != screenInfo.max_y or max_x != screenInfo.max_x:
	write_screen_info(max_y, max_x)

    start_game()
    

def get_screen_info():

    scr = curses.initscr()

    (max_y, max_x) = scr.getmaxyx()

    curses.endwin()

    return (max_y, max_x)


def write_screen_info(max_y, max_x):

    try:
	with open('screenInfo.py', 'w') as file:
	    file.write(
		    "max_y=" + str(max_y) + '\n' \
		    "max_x=" + str(max_x)
		    )

    except:
	print "Failed to write screen info..."
        return


def start_game():

    try:
	system("./game.py")

    except:
	curses.endwin()
	print "Something went wrong..."
	return


if __name__ == '__main__':
    main()

