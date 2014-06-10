#!/usr/bin/python2.7


import curses
from Astar import Astar, wrapper

def main():

    scr = curses.initscr()
    curses.noecho()
    curses.curs_set(0)

    win = curses.newwin(30, 50, 0, 0)

    win.addstr(0, 0, "CAVE!")
    win.refresh()

    rooms = [[9, 1], [3, 20]]

    closed_list = [[3, 5], [8, 1], [3, 15], [4, 16], [2, 16], [3, 16], [3, 17]]

    for item in closed_list:
	win.addstr(item[0], item[1], 'O')

    for room in rooms:
	win.addstr(room[0], room[1], '$')

    win.refresh()

    new = wrapper(Astar)
    halls = new(rooms, closed_list)

    for hall in halls:
	win.addstr(hall[0], hall[1], '#')
	win.refresh()
	win.getch()

    curses.endwin()


if __name__ == '__main__':
    main()

