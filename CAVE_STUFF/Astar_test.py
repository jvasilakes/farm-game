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

    rooms = [[1, 7], [9, 1], [4, 17]]

    closed_list = []

    for room in rooms:
	closed_list.append(room)
	win.addstr(room[0], room[1], '$')

    win.refresh()

    new = wrapper(Astar)
    halls = new(rooms, closed_list)

    for hall in halls:
	win.addstr(hall[0], hall[1], '#')

    win.getch()
    curses.endwin()


if __name__ == '__main__':
    main()

