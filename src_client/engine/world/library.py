def get_xy_coords_from_tile_index(tile_index, cube_size):
    half = cube_size / 2
    quarter = cube_size / 4
    return tile_index[0] * half - tile_index[1] * half, tile_index[0] * quarter + tile_index[1] * quarter
