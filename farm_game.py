import random
import curses

import windows
from windows import game_win, msg_win

from world import world

import animations
import character
import thing
import plant

from environment import house, ship_box, pond, Tree, Rock
from character import farmer


def main():

    world.populate(Tree, 'GRAPHICS/tree', 12)
    world.populate(Rock, 'GRAPHICS/rock', 9)


    # --------------------- GAMEPLAY --------------------------------

    c = game_win.getch()

    while True:

        if c in farmer.dirs:

            farmer.move(c)
	    world.redraw()
            c = game_win.getch()


        elif c in farmer.actions:

	    if c == ord('k'):

	 	for key in world.contents:
		    for thing in world.contents[key]:
	        	if farmer.pos in thing.vicinity:

			    msg_win.clear()
			    msg_win.refresh()
			    thing.interact(farmer)

		game_win.refresh()

	        c = msg_win.getch()


	    elif c == ord('p'):

	        farmer.plant()
	        world.redraw()
                c = game_win.getch()


	    elif c == ord('h'):

	        farmer.harvest()
	        game_win.clear()
	        world.redraw()
	        farmer.draw()
	        c = game_win.getch()


	    elif c == ord('i'):

	        msg_win.clear()
	        msg_win.refresh()
	        farmer.inventory.view()
	        c = game_win.getch()


	    elif c == ord('j'):
	    
	        farmer.inventory.remove()
	        #msg_win.clear()
	        #msg_win.refresh()
	        c = game_win.getch()


        elif c == ord('q'):

	    break

        else:

            c = game_win.getch()


    curses.endwin()
    
    
if __name__ == '__main__':
    main()
