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
        window = self.engine.window
        for y in range(len(self.tile_index_map)):
            for x in range(len(self.tile_index_map[0])):
                if self.tile_index_map[y][x]:
                    window.blit(self.engine.ressources_handler.images["terrain"]["cube1"], 150 + x * 16 - y * 16, 150 + x * 10 + y * 10)
