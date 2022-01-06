def get_iso_xy_from_tile_index(tile_index, offset: tuple = None):
    half = 16       # deduce from tile top size
    quarter = 8

    projected_x = tile_index[0] * half - tile_index[1] * half
    projected_y = tile_index[0] * quarter + tile_index[1] * quarter

    if offset:
        projected_x += offset[0]
        projected_y += offset[1]

    return projected_x, projected_y


def get_iso_xy_from_xyz(x, y, z):
    sim_tile_size = [32, 32]
    simili_x_index = x / sim_tile_size[0]   # x >> 5
    simili_y_index = y / sim_tile_size[1]   # x >> 5
    x, y = get_iso_xy_from_tile_index(simili_x_index, simili_y_index)
    y += z
    return x, y
