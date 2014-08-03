def find_min(coor, list):

    """ coor is 0 or 1, which 
	are the y and x coordinates,
	respectively.

    """

    min = list[0][coor]

    for set in list:
	if set[coor] < min:
	    min = set[coor]

    return min


def find_max(coor, list):

    """ coor is 0 or 1, which 
	are the y and x coordinates,
	respectively.

    """

    max = list[0][coor]

    for set in list:
	if set[coor] > max:
	    max = set[coor]

    return max


def find_corners(ymin, ymax, xmin, xmax):

    A = [ymin, xmin]
    B = [ymin, xmax]
    C = [ymax, xmax]
    D = [ymax, xmin]

    corners = [A, B, C, D]

    return corners


def expand_corners(corners_list):

    A = corners_list[0]
    B = corners_list[1]
    C = corners_list[2]
    D = corners_list[3]

    A[0] -= 1
    A[1] -= 1
    B[0] -= 1
    B[1] += 1
    C[0] += 1
    C[1] += 1
    D[0] += 1
    D[1] -= 1

    expanded = [A, B, C, D, A]

    return expanded

def fill(corners_list):

    vicinity = []


    # for each corner in corners_list, w/o the final value (i.e. [A, B, C, D])
    for i in xrange((len(corners_list) - 1)):

	# E.g. if y value of A is equal to y value of B,
	# then we are dealing with a horizontal line.
	if corners_list[i][0] == corners_list[i+1][0]:

	    y = corners_list[i][0]

	    # if x value of B is greater than the x value of A,
	    # then we are moving left to right (A is to the left of B)
	    if corners_list[i+1][1] > corners_list[i][1]:

	        for x in xrange(corners_list[i][1], corners_list[i+1][1]):

	            vicinity.append([y, x])

	    else:

	    	# Else, we are moving from right to left (B is to the left of A)
		for x in xrange(corners_list[i+1][1], corners_list[i][1]):

		    vicinity.append([y, x])

	    vicinity.append(corners_list[i+1])


	# Else if x value of A is equal to the x value of B,
	# then we are dealing with a vertical line.
	elif corners_list[i][1] == corners_list[i+1][1]:    

	    x = corners_list[i][1]

	    if corners_list[i+1][0] > corners_list[i][0]:

	        for y in xrange(corners_list[i][0], corners_list[i+1][0]):

	            vicinity.append([y, x])

	    else:

		for y in xrange(corners_list[i+1][0], corners_list[i][0]):

		    vicinity.append([y, x])

	    vicinity.append(corners_list[i+1])

	# TODO: Need an else statement here. This function so far assumes that
	# is is dealing with a rectangular object. It works for now...


    return vicinity


def find_vicinity(list):

    ymin = find_min(0, list)
    ymax = find_max(0, list)
    xmin = find_min(1, list)
    xmax = find_max(1, list)

    corners = find_corners(ymin, ymax, xmin, xmax)

    expanded = expand_corners(corners)

    vicinity = fill(expanded)

    return vicinity

