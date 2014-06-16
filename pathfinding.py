
def find_best_tile(list, start, end, tile_count):

    try:

	best = list[0]

	for tile in list:

	    if calc_score(tile, start, end, tile_count) < \
	       calc_score(best, start, end, tile_count):

		best = tile

	return best

    except:
	return 'None'


def calc_score(tile, start, end, tile_count):

    # Movement cost from start tile to current tile
    G = tile_count

    # Movement cost from current tile to destination tile
    H = abs(end[0] - tile[0]) + abs(end[1] - tile[1])

    score = G + H

    return score


def wrapper(Astar):

    """
    When wrapped, Astar takes a list of
    coordinates through which it will
    find a path.

    Example:
	from Astar import Astar, wrapper

	Astar = wrapper(Astar)

	rooms = [[2, 2], [4, 9], [1, 6]]

	Astar(rooms)
    """

    def find_paths(rooms_list, closed_list):

	paths = []

	for room, next_room in zip(rooms_list, rooms_list[1:]):
	    path = Astar(room, next_room, closed_list) 
	    paths.extend(path)

	return paths

    return find_paths


def RoomWrapper(Astar):

    def connect_doors(rooms_list, closed_list):

	halls = []

	for i in xrange(len(rooms_list) - 1):

	    if 'exit' not in rooms_list[i].doors:

		pass
	
	    else:

		hall = Astar(rooms_list[i].doors['exit'], 
		       rooms_list[i+1].doors['entrance'],
		       closed_list)

		halls.extend(hall)

	return halls

    return connect_doors


def Astar(start, end, closed_list):

    """
    A* pathfinding algorithm.

    This algorithm finds a path from start to end
    avoiding objects whose coordinates are stored
    in closed_list.

    """

    path = []

    complete = False

    current = start

    tile_count = 0

    while not complete:

	open_list = [] 

	walkable = [[current[0] - 1, current[1]],
		    [current[0] + 1, current[1]],
		    [current[0], current[1] - 1],
		    [current[0], current[1] + 1]]
		    #[current[0] - 1, current[1] - 1],
		    #[current[0] - 1, current[1] + 1],
		    #[current[0] + 1, current[1] - 1],
		    #[current[0] + 1, current[1] + 1]]

	for tile in walkable:

	    if tile[0] <= 0 or \
	       tile[1] <= 0 or \
	       tile in closed_list:

		pass

	    else:
		open_list.append(tile)

	best = find_best_tile(open_list, start, end, tile_count)

	if best == 'None':

	    closed_list.append(current)

	    last_good_place = path[len(path) - 2]

	    current = last_good_place

	elif best == end:

	    complete = True

	else:

	    path.append(best)
	    current = best
	    tile_count += 1
	    closed_list.append(current)

    return path

