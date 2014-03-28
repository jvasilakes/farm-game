from windows import msg_win


class Inventory(object):


    def __init__(self):

	self.contents = {}



    def add(self, item):

	if item.name in self.contents:
	    self.contents[item.name].append(item)

	else:
	    self.contents.update(zip([item.name], [[]]))
	    self.contents[item.name].append(item)

	msg_win.clear()
	msg_win.addstr(1, 20, item.name + " added.")
	msg_win.refresh()



    def remove(self):

	item_type = self.view(1)

	if item_type == 'Nothing':
	    return item_type

	else:
	    msg_win.clear()
	    msg_win.addstr(2, 20, item_type + " removed.")
	    msg_win.refresh()

	    return self.contents[item_type].pop(0)



    def view(self, *args):
	
	if len(self.contents) > 0:

	    for item_type in self.contents:

	        count = len(self.contents[item_type])

		if count > 0:

		    num = str(count)		

	            msg_win.addstr(1, 5, "Inventory: ")
	            msg_win.addstr(1, 18, item_type + " x" + num)
	            msg_win.refresh()
	
		    if len(args) == 0:	    # If default calling environment
	                msg_win.getch()	    # just iterate through inventory

		    else:

		        c = msg_win.getch()	    # If other than default calling
						    # environment, the user is being
					            # asked to make a selection. 

		        if c == ord('y'):	    
		            return item_type        # Return that selection

		        else:
		  	    c = msg_win.getch()

	 	        #return 'Nothing'


		else:
		    pass


		msg_win.clear()
		msg_win.refresh()


        else:
  	    msg_win.addstr(2, 18, "Nothing here.")
	    msg_win.refresh()
	    msg_win.getch()

	    return 'Nothing'

	msg_win.clear()
	msg_win.refresh()
