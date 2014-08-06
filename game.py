import random
import curses

import windows
import environment
import character

from header import *


class Game(object):

    _instance = None

    @classmethod
    def get_instance(cls):
	if not cls._instance:
	    cls._instance = cls()
	return cls._instance


    def __init__(self):

	self.game_win = windows.start_gamewin()
	self.msg_win = windows.start_msgwin()

	self.world = environment.World()

	self.pet = character.Pet(
	    DOG_START_POS,
	    DOG_GRAPHIC,
	    self.world
	)

	self.player = character.Player(
	    PLAYER_1_START_POS,
	    PLAYER_1_GRAPHIC,
	    self.world,
	    pet=self.pet
	)

	self.world.redraw(self.game_win)


    def run(self):

	self.player.current_space.redraw(self.game_win)

	# --------------------- GAMEPLAY --------------------------------

	c = NULL

	while True:
	    if c in self.player.dirs:
		# 'w', 'a', 's', 'd', 'NULL'
		self.player.move(c)
		self.player.current_space.redraw(self.game_win)
		c = self.game_win.getch()


	    elif c in self.player.actions:
		# 'k': interact
		# 'p': plant a crop
		# 'h': harvest a crop
		# 'i': view inventory

		if c == KEY_INTERACT:

		    for key in self.player.current_space.contents:
			for obj in self.player.current_space.contents.get(key):
			    if self.player.pos in obj.vicinity:

				self.msg_win.clear()
				self.msg_win.refresh()
				obj.interact(self.player)

		    self.game_win.refresh()

		    c = self.game_win.getch()


		elif c == KEY_PLANT:

		    self.player.plant()
		    self.player.current_space.redraw(self.game_win)
		    c = self.game_win.getch()


		elif c == KEY_HARVEST:

		    self.player.harvest()
		    self.player.current_space.redraw(self.game_win)
		    c = self.game_win.getch()


		elif c == KEY_INVENTORY:

		    self.msg_win.clear()
		    self.msg_win.refresh()
		    self.player.inventory.view()
		    c = self.game_win.getch()

		elif c == KEY_CALL_PET:

		    self.player.call_pet()
		    #self.pet.find_player(self.player)

		    c = self.game_win.getch()

		    
	    elif c == KEY_QUIT:

		self.msg_win.clear()
		self.msg_win.addstr(1, 10, "Really quit? [y/n]")
		self.msg_win.refresh()

		ans = self.msg_win.getch()

		if ans == ord('y'):
		    break

		else:
		    self.msg_win.clear()
		    self.msg_win.refresh()
		    c = self.game_win.getch()

	    else:

		c = self.game_win.getch()


	    self.player.current_space.updateNPCs()


	curses.endwin()
	


def get_instance():
    return Game.get_instance()

