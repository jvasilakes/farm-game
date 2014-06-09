#!/usr/bin/python2.7

import random
import curses

from header import *
from startup import game_win, msg_win
from singletons import farmer, dog


def main():

    farmer.current_space.redraw()

    # --------------------- GAMEPLAY --------------------------------

    c = NULL

    while True:
        if c in farmer.dirs:
	    # 'w', 'a', 's', 'd', 'NULL'
            farmer.move(c)
            farmer.current_space.redraw()
            c = game_win.getch()


        elif c in farmer.actions:
            # 'k': interact
            # 'p': plant a crop
            # 'h': harvest a crop
            # 'i': view inventory

            if c == KEY_INTERACT:

	 	for key in farmer.current_space.contents:
		    for obj in farmer.current_space.contents[key]:
	        	if farmer.pos in obj.vicinity:

			    msg_win.clear()
			    msg_win.refresh()
			    obj.interact(farmer)

		game_win.refresh()

	        c = msg_win.getch()


	    elif c == KEY_PLANT:

	        farmer.plant()
	        farmer.current_space.redraw()
                c = game_win.getch()


	    elif c == KEY_HARVEST:

	        farmer.harvest()
	        farmer.current_space.redraw()
	        c = game_win.getch()


	    elif c == KEY_INVENTORY:

	        msg_win.clear()
	        msg_win.refresh()
	        farmer.inventory.view()
	        c = game_win.getch()

	    elif c == KEY_FIND_PLAYER:

		dog.find_player(farmer)
		c = game_win.getch()

		


        elif c == KEY_QUIT:

	    msg_win.clear()
	    msg_win.addstr(1, 10, "Really quit? [y/n]")
	    msg_win.refresh()

	    ans = msg_win.getch()

	    if ans == ord('y'):
		break

	    else:
		msg_win.clear()
		msg_win.refresh()
		c = game_win.getch()

        else:

            c = game_win.getch()


	farmer.current_space.updateNPCs()


    curses.endwin()
    
    
if __name__ == '__main__':
    main()

