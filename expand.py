def find_min(coor, list):

    min = list[0][coor]

    for set in list:
	if set[coor] < min:
	    min = set[coor]

    return min


def find_max(coor, list):

    max = list[0][coor]

    for set in list:
	if set[coor] > max:
	    max = set[coor]

    return max


def find_corners(ymin, ymax, xmin, xmax):

    A = [ymin - 1, xmin - 1]
    B = [ymin - 1, xmax + 1]
    C = [ymax + 1, xmax + 1]
    D = [ymax + 1, xmin - 1]

    corners = [A, B, C, D, A]

    return corners



def fill(corners_list):

    vicinity = []


    for i in xrange((len(corners_list) - 1)):

	if corners_list[i][0] == corners_list[i+1][0]:

	    y = corners_list[i][0]

	    if corners_list[i+1][1] > corners_list[i][1]:
	        for x in xrange(corners_list[i][1], corners_list[i+1][1]):
	            vicinity.append([y, x])

	    else:
		for x in xrange(corners_list[i+1][1], corners_list[i][1]):
		    vicinity.append([y, x])

	    vicinity.append(corners_list[i+1])


	elif corners_list[i][1] == corners_list[i+1][1]:    

	    x = corners_list[i][1]

	    if corners_list[i+1][0] > corners_list[i][0]:
	        for y in xrange(corners_list[i][0], corners_list[i+1][0]):
	            vicinity.append([y, x])

	    else:
		for y in xrange(corners_list[i+1][0], corners_list[i][0]):
		    vicinity.append([y, x])

	    vicinity.append(corners_list[i+1])


    return vicinity


def find_vicinity(list):

    ymin = find_min(0, list)
    ymax = find_max(0, list)
    xmin = find_min(1, list)
    xmax = find_max(1, list)

    corners = find_corners(ymin, ymax, xmin, xmax)

    vicinity = fill(corners) 

    return vicinity
