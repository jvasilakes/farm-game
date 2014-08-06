#! /usr/bin/python2.7

import curses

import farm_config
import windows
import game
import debug_console


def main(): 

    curses.initscr()
    curses.noecho()
    curses.curs_set(0)

    if farm_config.INTRO:
	windows.start_introwin()

    if farm_config.DEBUG_WIN:
	debug_console.get()

    farm_game = game.get_instance()
    farm_game.run()


if __name__ == '__main__':
    main()

