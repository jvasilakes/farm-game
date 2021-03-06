def find_best_tile(list, start, end, tile_count):

    best = list[0]

    for tile in list:

	if calc_score(tile, start, end, tile_count) < \
	   calc_score(best, start, end, tile_count):

	    best = tile

    return best


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


def Astar(start, end, closed_list):

    """
    A* pathfinding algorithm.

    Pass it a list of [y, x] coordinates and
    it will return a list of coordinates going from
    one point to the next.

    Example:
	from Astar import Astar
	points = [[2, 2], [5, 5]]
	path = Astar(points)	
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

	for tile in walkable:

	    if tile[0] <= 0 or \
	       tile[1] <= 0 or \
	       tile in closed_list:

		pass

	    #if tile not in open_list:
	    else:
		open_list.append(tile)

	best = find_best_tile(open_list, start, end, tile_count)


	if best == end:
	    complete = True

	else:
	    path.append(best)

	current = best
	tile_count += 1

	closed_list.append(current)

    return path

