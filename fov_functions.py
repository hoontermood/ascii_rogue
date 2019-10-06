import tcod as libtcod


def initialize_fov(game_map):
    """Initialize pc's field of view

    :game_map: game_map
    :returns: fov_map

    """
    fov_map = libtcod.map_new(game_map.width, game_map.height)


    for y in range(game_map.height):
        for x in range(game_map.width):
            libtcod.map_set_properties(fov_map, x, y, not game_map.tiles[x][y].block_sight, not game_map.tiles[x][y].blocked)

        return fov_map


def recompute_fov(fov_map, x, y, radius, light_walls=True, algorithm=0):
    """Helper function to modify fov_map based on player location, determin light
    radius, and whether or not walls are lit

    :fov_map: TODO
    :x: TODO
    :y: TODO
    :radius: TODO
    :light_walls: TODO
    :algorithm: TODO
    :returns: TODO

    """
    libtcod.map_compute_fov(fov_map, x, y, radius, light_walls, algorithm)
