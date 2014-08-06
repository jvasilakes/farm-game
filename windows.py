import time
import curses

from header import *
import farm_config

from animations import display, intro




#--------INTRO WIN-------------------------------


def start_introwin():

    intro_win = curses.newwin(
	GAME_WIN_SIZE_Y,
	GAME_WIN_SIZE_X,
	GAME_WIN_POS_Y,
	GAME_WIN_POS_X
    )

    intro_win.keypad(1)

    intro(intro_win)

    logo_win = curses.newwin(
	LOGO_WIN_SIZE_Y,
	LOGO_WIN_SIZE_X,
	LOGO_WIN_POS_Y,
	LOGO_WIN_POS_X
	)

    display(open('GRAPHICS/INTRO/farm_logo', 'r').readlines(), logo_win, 0, 0)
    logo_win.refresh()
    time.sleep(2)

    menu_win = curses.newwin(
	4,
	17,
	INTRO_ANIM_POS_Y - 1,
	INTRO_ANIM_POS_X + 25
	)

    menu_win.addstr(0, 0, "1. Start playing")
    menu_win.addstr(1, 3, "2. Options")
    menu_win.addstr(2, 5, "3. Help")
    menu_win.addstr(3, 5, "4. Quit")
    menu_win.refresh()

    ans = menu_win.getch()

    while True:

	if ans == ord('1'):
	    break

	elif ans == ord('2'):
	    show_options_screen()

	elif ans == ord('3'):
	    show_help_screen()

	elif ans == ord('4'):
	    pass

	else:
	    pass

	intro_win.touchwin()
	intro_win.refresh()

	logo_win.touchwin()
	logo_win.refresh()

	menu_win.touchwin()
	menu_win.refresh()

	ans = menu_win.getch()

	del intro_win
	del logo_win
	del menu_win


#-------- OPTIONS_WIN ----------------------------------

def show_options_screen():

    options_win = curses.newwin(
	7,
	25,
	HELP_WIN_POS_Y,
	HELP_WIN_POS_X
	)

    options_win.touchwin()

    options_win.addstr(1, 3, "GAME_OPTIONS")
    options_win.addstr(3, 1, "1. Debugging: %s" % farm_config.DEBUG_WIN)
    options_win.addstr(4, 1, "2. All visible: %s" % farm_config.ALL_VISIBLE)
    options_win.addstr(5, 1, "3. Go back")

    options_win.box()
    options_win.refresh()
    ans = options_win.getch()

    while ans != ord('3'):

	if ans == ord('1'):
	    pass

	elif ans == ord('2'):
	    farm_config.ALL_VISIBLE = not farm_config.ALL_VISIBLE

	    options_win.clear()

	    options_win.addstr(1, 3, "GAME_OPTIONS")
	    options_win.addstr(3, 1, "1. Debugging: %s" % farm_config.DEBUG_WIN)
	    options_win.addstr(4, 1, "2. All visible: %s" % farm_config.ALL_VISIBLE)
	    options_win.addstr(5, 1, "3. Go back")
	    options_win.box()

	    options_win.refresh()

	ans = options_win.getch()

    del options_win

    return


#--------- HELP_WIN -------------------------------------

def show_help_screen():
	
    help_win = curses.newwin(
	HELP_WIN_SIZE_Y,
	HELP_WIN_SIZE_X,
	HELP_WIN_POS_Y,
	HELP_WIN_POS_X
	)

    help_win.touchwin()

    help_win.addstr(1, 6, "CONTROLS")
    help_win.addstr(3, 1, "'wasd': move")
    help_win.addstr(4, 1, "'k': interact")
    help_win.addstr(5, 1, "'p': plant a crop")
    help_win.addstr(6, 1, "'h': harvest a crop")
    help_win.addstr(7, 1, "'i': inventory")
    help_win.addstr(8, 1, "'c': call your pet")
    help_win.addstr(9, 1, "'q': quit")

    help_win.box()

    help_win.refresh()

    help_win.getch()

    del help_win

    return


#---------GAME WIN --------------------------------------

def start_gamewin():

    game_win = curses.newwin(
	GAME_WIN_SIZE_Y,
	GAME_WIN_SIZE_X,
	GAME_WIN_POS_Y,
	GAME_WIN_POS_X
	)

    game_win.keypad(1)

    return game_win



#----------MSG WIN--------------------------------------

def start_msgwin():

    win = curses.newwin(
	MSG_WIN_SIZE_Y,
	MSG_WIN_SIZE_X,
	MSG_WIN_POS_Y,
	MSG_WIN_POS_X
	)

    win.keypad(1)

    return win


