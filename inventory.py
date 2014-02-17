from windows import msg_win


class Inventory(object):


    def __init__(self):

	self.contents = {}



    def add(self, item):

	if item.name in self.contents:
	    self.contents[thing.name].append(thing)

	else:
	    self.contents.update(zip([thing.name], [[]]))
	    self.contents[thing.name]append(thing)

	msg_win.addstr(1, 20, item.name + " added.")
	msg_win.refresh()



    def remove(self):

	item = self.view(1)

	msg_win.addstr(2, 18, item + " removed from inventory.")
	msg_win.refresh()
	msg_win.getch()

	if item == 'Nothing':
	    return

	else:
	    return self.items[item].pop(0)



    def view(self, *args):
	
	for item_type in self.items:
	    if len(self.items[item_type]) > 0:

		count = str(len(self.items[item_type]))

	        msg_win.addstr(1, 5, "Inventory: ")
	        msg_win.addstr(1, 18, item_type + " x" + count)
	        msg_win.refresh()
	
		if len(args) == 0:	    # If default calling environment
	            msg_win.getch()	    # just iterate through inventory

		else:
		    c = msg_win.getch()	    # If other than default calling
		    if c == ord('y'):	    # environment, the user is being
			return item_type    # asked to make a selection. 
					    # Return that selection

		    else:
		 	return 'Nothing'

	    else:
		msg_win.addstr(2, 18, "Nothing in inventory.")
		msg_win.refresh()
		msg_win.getch()

		return 'Nothing'

	msg_win.clear()
	msg_win.refresh()
