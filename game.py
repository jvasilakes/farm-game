#!/usr/bin/python2.7

import random
import curses

from header import *
from startup import game_win, msg_win
from world import world
from node import Node
from character import Character, farmer, dog
from environment import house, ship_box, pond
from environment import Tree, Rock, Cave


def main():

    world.seed(Cave, CAVE_GRAPHICS_DIR + 'entrance_external', 1)
    world.seed(Tree, 'GRAPHICS/tree', NUMBER_TREES)
    world.seed(Rock, 'GRAPHICS/rock', NUMBER_ROCKS)

    world.redraw()

    # --------------------- GAMEPLAY --------------------------------

    c = NULL

    while True:
        if c in farmer.dirs:
	    # 'w', 'a', 's', 'd', 'NULL'
            farmer.move(c)
            world.redraw()
            c = game_win.getch()


        elif c in farmer.actions:
            # 'k': interact
            # 'p': plant a crop
            # 'h': harvest a crop
            # 'i': view inventory

            if c == KEY_INTERACT:

	 	for key in world.contents:
		    for obj in world.contents[key]:
	        	if farmer.pos in obj.vicinity:

			    msg_win.clear()
			    msg_win.refresh()
			    obj.interact(farmer)

		game_win.refresh()

	        c = msg_win.getch()


	    elif c == KEY_PLANT:

	        farmer.plant()
	        world.redraw()
                c = game_win.getch()


	    elif c == KEY_HARVEST:

	        farmer.harvest()
	        world.redraw()
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


	world.updateNPCs()


    curses.endwin()
    
    
if __name__ == '__main__':
    main()

