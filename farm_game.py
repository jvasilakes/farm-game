import curses
import random

import windows
from windows import game_win
from windows import msg_win

from world import world

import animations
import character
import things
import plant


farmer = character.Character("@") 

house = things.Thing(1, 1, 'GRAPHICS/house')
ship_box = things.Thing(4, 12, 'GRAPHICS/ship_box')
pond = things.Thing(28, 40, 'GRAPHICS/pond')

things.populate('trees', 'GRAPHICS/tree', 12)
things.populate('rocks', 'GRAPHICS/rock', 9)


# ---------- GAMEPLAY --------------------

c = game_win.getch()

while True:

    if c in farmer.dirs:

        farmer.move(c)
	list.redraw(game_win)
        c = game_win.getch()


    elif c in farmer.actions:

	if c == ord('p'):

	    farmer.plant()
	    list.redraw(game_win)
            c = game_win.getch()

	elif c == ord('o'):
	    if farmer.pos == [6, 6]:

	        # go into your house and sleep until the next day
	        # plants grow one stage while you sleep

	        game_win.clear()
	        animations.sunrise(game_win) 
	        game_win.clear()
	        list.grow_plants()
	        list.redraw(game_win)
	        farmer.render(game_win)
	        c = game_win.getch()

	    else:
		c = game_win.getch()

	elif c == ord('h'):

	    farmer.harvest()
	    game_win.clear()
	    list.redraw(game_win)
	    farmer.render(game_win)
	    c = game_win.getch()

	elif c == ord('i'):

	    msg_win.clear()
	    msg_win.refresh()
	    farmer.inventory.view()
	    c = game_win.getch()

	elif c == ord('j'):
	    
	    farmer.inventory.remove()
	    msg_win.clear()
	    msg_win.refresh()
	    c = game_win.getch()


    elif c == ord('q'):

	break

    else:

        c = game_win.getch()


curses.endwin()
