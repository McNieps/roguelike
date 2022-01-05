import pygame

from src_client.engine.engine import Engine


class World:
    def __init__(self, engine: Engine):
        self.engine = engine

        self.tile_index_map = [[0, 0, 0, 0, 0, 0, 0, 0],
                               [1, 1, 1, 1, 1, 1, 1, 0],
                               [1, 1, 1, 0, 0, 0, 1, 0],
                               [1, 1, 1, 0, 0, 0, 1, 0],
                               [1, 1, 1, 1, 1, 1, 1, 0],
                               [1, 1, 1, 1, 1, 1, 1, 0],
                               [1, 1, 1, 1, 1, 1, 1, 0],
                               [1, 1, 1, 1, 1, 1, 1, 0]]

    def render(self, rect_to_render: pygame.Rect):
        pass

