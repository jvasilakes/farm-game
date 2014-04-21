import curses
from windows import msg_win


class Inventory(object):


    def __init__(self, owner):

	self.owner = owner

	self.contents = {}

	# Not sure where to put this...
	# self.money = 0


    # Pretty much the same as world.add()
    def add(self, item_list):

	count = 0	

	# a list is used so that multiple items can be added at once
	# for example, when the player cuts down a tree, they receive
	# two pieces of wood.
	for item in item_list:

	    count += 1

	    if item.name in self.contents:
	        self.contents[item.name].append(item)

	    else:
	        self.contents.update(zip([item.name], [[]]))
	        self.contents[item.name].append(item)

	msg_win.clear()
	msg_win.addstr(1, 5, str(count) + " " + item.name + \
		       " added to " + self.owner + "'s inventory.")
	msg_win.refresh()


    # Pretty much an interactive version of world.remove()
    def remove(self, item, num):

	curses.echo()

	msg_win.clear()
	msg_win.addstr(0, 5, "Remove how many?")
	msg_win.addstr(1, 5, "(Current quantity: " + num + ") ")
	
        ans = msg_win.getstr()

	curses.noecho()
	if int(ans) <= int(num):

	    temp = []

            msg_win.clear()
            msg_win.addstr(1, 5, str(ans) + " " + item + \
			   " removed from " + self.owner + "'s inventory.")

            msg_win.refresh()

	    for i in xrange(int(ans)):
		temp.append(self.contents[item][0])
                del self.contents[item][0]

	    msg_win.getch()
	    msg_win.clear()
	    msg_win.refresh()
	    return temp

	elif int(ans) > int(num):

	    msg_win.clear()
	    msg_win.addstr(1, 5, "You don't have that many in inventory.")
	    msg_win.refresh()

	    msg_win.getch()
	    msg_win.clear()
	    msg_win.refresh()
	    return 'None'

	else:
	    msg_win.clear()
	    msg_win.refresh()
	    return 'None'


    def view(self):

	if len(self.contents) > 0:

	    # This will flip to False if any dictionary key actually 
	    # has any ojects in it's sublist.
	    # Used to test for an empty list even when dicitonary keys are present.
	    empty = True

	    for item_type in self.contents:
		
		count = len(self.contents[item_type])

		if count > 0:

		    empty = False
		    num = str(count)

		    msg_win.addstr(0, 5, self.owner + "'s Inventory: ")
		    msg_win.addstr(0, 30, item_type + " x" + num)
		    msg_win.addstr(2, 5, "'t': take item    'n': next")
		    msg_win.refresh()

		    c = msg_win.getch()
		    while c != ord('t') and c != ord('n'):
			c = msg_win.getch()

		    if c == ord('t'):
			item_list = self.remove(item_type, num)
			return item_list

		    else:
		        msg_win.clear()
			msg_win.refresh()

		else:
		    pass

	    if empty:
	        msg_win.addstr(2, 18, "Nothing here.")
	        msg_win.refresh() 
	        msg_win.getch()
	        msg_win.clear()
	        msg_win.refresh()
	        return 'None'

	else:
	    msg_win.addstr(2, 18, "Nothing here.")
	    msg_win.refresh() 
	    msg_win.getch()
	    msg_win.clear()
	    msg_win.refresh()
	    return
