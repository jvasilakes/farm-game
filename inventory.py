import curses

import game


class Inventory(object):


    def __init__(self, owner):

	self.owner = owner

	self.contents = {}

	self.money = 0


    # Pretty much the same as world.add()
    def add(self, item_list):

	count = 0	

	# a list is used so that multiple items can be added at once.
	# For example, when the player cuts down a tree, they receive
	# two pieces of wood.
	for item in item_list:

	    count += 1

	    if item.name in self.contents:
	        self.contents[item.name].append(item)

	    else:
	        self.contents.update(zip([item.name], [[]]))
	        self.contents[item.name].append(item)

	game.get_instance().msg_win.clear()
	game.get_instance().msg_win.addstr(
	    1, 5, str(count) + " " + item.name + \
	    " added to " + self.owner + "'s inventory."
	    )

	game.get_instance().msg_win.refresh()

	game.get_instance().msg_win.getch()
	game.get_instance().msg_win.clear()
	game.get_instance().msg_win.refresh()


    # Pretty much an interactive version of world.remove()
    def remove(self, item, num):

	curses.echo()

	game.get_instance().msg_win.clear()
	game.get_instance().msg_win.addstr(0, 5, "Remove how many?")
	game.get_instance().msg_win.addstr(1, 5, "(Current quantity: " + num + ") ")
	
        ans = game.get_instance().msg_win.getstr()

	curses.noecho()

	if int(ans) <= int(num):

	    temp = []

            game.get_instance().msg_win.clear()
            game.get_instance().msg_win.addstr(
		1, 5, str(ans) + " " + item + \
		" removed from " + self.owner + "'s inventory."
		)

            game.get_instance().msg_win.refresh()

	    for i in xrange(int(ans)):
		temp.append(self.contents[item][0])
                del self.contents[item][0]

	    game.get_instance().msg_win.getch()
	    game.get_instance().msg_win.clear()
	    game.get_instance().msg_win.refresh()
	    return temp

	elif int(ans) > int(num):

	    game.get_instance().msg_win.clear()
	    game.get_instance().msg_win.addstr(1, 5, "You don't have that many in inventory.")
	    game.get_instance().msg_win.refresh()

	    game.get_instance().msg_win.getch()
	    game.get_instance().msg_win.clear()
	    game.get_instance().msg_win.refresh()
	    return 'None'

	else:
	    game.get_instance().msg_win.clear()
	    game.get_instance().msg_win.refresh()
	    return 'None'


    def view(self):

	game.get_instance().msg_win.clear()
	game.get_instance().msg_win.refresh()
	game.get_instance().msg_win.addstr(2, 50, "$" + str(self.money))

	if len(self.contents) > 0:

	    # This will flip to False if any dictionary key actually 
	    # has any objects in it's sublist.
	    # Used to test for an empty list even when dicitonary
	    # keys are present.

	    empty = True

	    for item_type in self.contents:
		
		count = len(self.contents[item_type])

		if count > 0:

		    empty = False
		    num = str(count)

		    game.get_instance().msg_win.addstr(2, 50, "$" + str(self.money))

		    game.get_instance().msg_win.addstr(0, 5, self.owner + "'s Inventory: ")
		    game.get_instance().msg_win.addstr(0, 25, item_type + " x" + num)
		    game.get_instance().msg_win.addstr(2, 5, "'t': take item    'n': next")
		    game.get_instance().msg_win.refresh()

		    c = game.get_instance().msg_win.getch()
		    while c != ord('t') and c != ord('n'):
			c = game.get_instance().msg_win.getch()

		    if c == ord('t'):
			item_list = self.remove(item_type, num)
			return item_list

		    else:
		        game.get_instance().msg_win.clear()
			game.get_instance().msg_win.refresh()

		else:
		    pass

	    if empty:
	        game.get_instance().msg_win.addstr(0, 18, "Nothing here.")
	        game.get_instance().msg_win.refresh() 
	        game.get_instance().msg_win.getch()
	        game.get_instance().msg_win.clear()
	        game.get_instance().msg_win.refresh()
	        return 'None'

	else:
	    game.get_instance().msg_win.addstr(0, 18, "Nothing here.")
	    game.get_instance().msg_win.refresh() 
	    game.get_instance().msg_win.getch()
	    game.get_instance().msg_win.clear()
	    game.get_instance().msg_win.refresh()
	    return 'None'

