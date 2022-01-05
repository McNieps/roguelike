import pygame

from src_client.engine.engine import Engine
from src_client.engine.handlers.loop_handler import LoopHandler


class World:
    def __init__(self, engine: Engine):
        self.engine = engine

        self.tile_index_map = [[1, 1, 1, 0, 0, 0, 0, 0],
                               [1, 1, 1, 1, 1, 1, 1, 0],
                               [1, 1, 1, 0, 0, 0, 1, 0],
                               [1, 1, 1, 0, 0, 0, 1, 0],
                               [1, 1, 1, 1, 1, 1, 1, 0],
                               [1, 1, 1, 1, 1, 1, 1, 0],
                               [1, 1, 1, 1, 1, 1, 1, 0],
                               [1, 1, 1, 1, 1, 1, 1, 0]]

    def render(self):
        window = self.engine.window
        for y in range(len(self.tile_index_map)):
            for x in range(len(self.tile_index_map[0])):
                if self.tile_index_map[y][x]:
                    window.blit(self.engine.ressources_handler.images["terrain"]["cube1"], (150 + x * 16 - y * 16, 150 + x * 8 + y * 8))


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
        world.render()
        pygame.display.flip()
    pygame.quit()