import curses

from header import *


class DebugConsole(object):

    _instance = None

    @classmethod
    def get(cls):
	if not cls._instance:
	    cls._instance = cls()
	return cls._instance

    def __init__(self):

	self.win = curses.newwin(
	    DEBUG_WIN_SIZE_Y,
	    DEBUG_WIN_SIZE_X,
	    DEBUG_WIN_POS_Y,
	    DEBUG_WIN_POS_X
	    )

	self.win.keypad(1)

	self.header = curses.newwin(
	    DEBUG_TITLE_SIZE_Y,
	    DEBUG_TITLE_SIZE_X,
	    DEBUG_TITLE_POS_Y,
	    DEBUG_TITLE_POS_X
	    )

	self.header.addstr(0, 1, "DEBUGGING CONSOLE")
	self.header.refresh()

	self.ynow = 0


    def _print(self, message):
    
	if self.ynow >= DEBUG_WIN_SIZE_Y:
	    self.clear()
	    self.ynow = 0

	self.win.addstr(self.ynow, 0, message)

	count = 0
	for char in message:
	    count += 1

	if count >= DEBUG_WIN_SIZE_X:
	    self.ynow += 1

	self.win.refresh()
	self.ynow += 1	


    def clear(self):
	self.win.clear()
	self.win.refresh()


def get():
    return DebugConsole.get()
