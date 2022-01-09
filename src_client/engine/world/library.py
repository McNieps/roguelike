import pygame
from collections import deque
from math import floor, ceil


def get_iso_xy_from_tile_index(tile_index: tuple, offset: tuple = None):
    tile_top_half_width = 16
    tile_top_half_height = 8

    projected_x = tile_index[0] * tile_top_half_width - tile_index[1] * tile_top_half_width
    projected_y = tile_index[0] * tile_top_half_height + tile_index[1] * tile_top_half_height

    if offset:
        projected_x += offset[0]
        projected_y += offset[1]

    return projected_x, projected_y


def get_tile_index_from_iso_xy(x: float, y: float, offset: tuple = None) -> tuple:
    tile_top_half_width = 16
    tile_top_half_height = 8

    if offset:
        x += offset[0]
        y += offset[1]

    index_x = x * tile_top_half_height + y * tile_top_half_width
    index_y = -x * tile_top_half_height + y * tile_top_half_width

    index_x /= 256
    index_y /= 256

    return index_x, index_y


def get_iso_xy_from_xyz(x: float, y: float, z: float, offset: tuple = None) -> tuple:
    sim_tile_width = 32
    sim_tile_height = 32
    tile_top_half_width = 16
    tile_top_half_height = 8

    simili_x_index = (x / sim_tile_width)
    simili_y_index = (y / sim_tile_height)

    x = simili_x_index * tile_top_half_width - simili_y_index * tile_top_half_width
    y = simili_x_index * tile_top_half_height + simili_y_index * tile_top_half_height

    if offset:
        x += offset[0]
        y += offset[1]
    y += z

    return x, y


def get_tile_list_in_rect_by_order(rect: pygame.Rect) -> deque:
    """Prend en moyenne 0.2 ms à tourner sans la vérification d'appartenance au monde, 0.4 ms sinon :("""
    # TODO peut-être passer en cython? Théo?

    bonus_top_row = -6
    bonus_bottom_row = 0

    top_left_index = get_tile_index_from_iso_xy(rect.left, rect.top)
    bottom_right_index = get_tile_index_from_iso_xy(rect.right, rect.bottom)

    left_column_dx = int((top_left_index[0] - top_left_index[1]) // 2)
    right_column_dx = int((bottom_right_index[0] - bottom_right_index[1]) // 2) + 2
    top_row_dy = floor(top_left_index[0] + top_left_index[1]) - 1 + bonus_top_row
    bottom_row_dy = ceil(bottom_right_index[0] + bottom_right_index[1]) + bonus_bottom_row

    tiles = deque()

    for row in range(top_row_dy, bottom_row_dy):
        row_base_index = (row // 2 + row % 2, row//2)
        for column in range(left_column_dx, right_column_dx):
            tiles.append((row_base_index[0] + column, row_base_index[1] - column))

    return tiles
