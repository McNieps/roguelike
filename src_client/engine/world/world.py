import pygame

from random import randint

from src_client.engine.engine import Engine
from src_client.engine.handlers.loop_handler import LoopHandler
from src_client.engine.world.tile import Tile


class World:
    def __init__(self, _engine: Engine):
        self.engine = _engine

        self.tile_index_map = [[1, 1, 1, 0, 0, 0, 0, 0],
                               [1, 1, 1, 1, 1, 1, 1, 0],
                               [1, 1, 1, 0, 0, 0, 1, 0],
                               [1, 1, 1, 0, 0, 0, 1, 0],
                               [1, 1, 1, 1, 1, 1, 1, 0],
                               [1, 1, 1, 1, 1, 1, 1, 0],
                               [1, 1, 1, 1, 1, 1, 1, 0],
                               [1, 1, 1, 1, 1, 1, 1, 0]]

        self.tiles = []
        self.fill_tiles_list()

    def fill_tiles_list(self):
        for y in range(len(self.tile_index_map)):
            for x in range(len(self.tile_index_map[0])):
                if self.tile_index_map[y][x]:
                    val = randint(0, 2)
                    if val == 0:
                        self.tiles.append(Tile(self.engine, (x, y), self.engine.ressources_handler.images["terrain"]["cube1"]))
                    elif val == 1:
                        self.tiles.append(Tile(self.engine, (x, y), self.engine.ressources_handler.images["terrain"]["cube2"]))
                    elif val == 2:
                        self.tiles.append(Tile(self.engine, (x, y), self.engine.ressources_handler.images["terrain"]["cube3"]))

    def render(self):
        window = self.engine.window
        for y in range(len(self.tile_index_map)):
            for x in range(len(self.tile_index_map[0])):
                if self.tile_index_map[y][x]:
                    window.blit(self.engine.ressources_handler.images["terrain"]["cube1"], (150 + x * 16 - y * 16, 150 + x * 8 + y * 8))
        pygame.draw.rect(window, (0, 0, 255), (150, 150, 32, 32), 2)
        window.set_at((150, 150), (255, 0, 0))

    def render_bis(self):
        for tile in self.tiles:
            tile.render()
            # tile.render_hitbox()

    def render_hitbox(self):
        for tile in self.tiles:
            tile.render_hitbox()


if __name__ == "__main__":
    loop_handler = LoopHandler(120)

    engine = Engine()
    world = World(engine)

    while loop_handler.is_running():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop_handler.stop_loop()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop_handler.stop_loop()
        world.render_bis()
        # world.render_hitbox()
        pygame.display.flip()
    pygame.quit()
