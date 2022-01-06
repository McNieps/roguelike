import pygame

from random import randint

from src_client.engine.engine import Engine
from src_client.engine.handlers.loop_handler import LoopHandler

from src_client.engine.world.tile import Tile
from src_client.engine.world.cluster import Cluster
from src_client.engine.world.camera import Camera


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

        self.tile_height_map = [[3, 3, 3, 0, 0, 0, 0, 0],
                                [3, 3, 3, 2, 1, 1, 1, 0],
                                [3, 3, 3, 0, 0, 0, 1, 0],
                                [2, 2, 2, 0, 0, 0, 1, 0],
                                [1, 1, 1, 1, 1, 1, 1, 0],
                                [0, 0, 0, 0, 0, 1, 1, 0],
                                [0, 0, 0, 0, 0, 1, 1, 0],
                                [0, 0, 0, 0, 0, 1, 1, 0]]

        self.tiles = []
        self.clusters = [Cluster()]

        self.fill_tiles_list()

    def fill_tiles_list(self):
        for y in range(len(self.tile_index_map)):
            for x in range(len(self.tile_index_map[0])):
                if self.tile_index_map[y][x]:
                    val = randint(0, 2)
                    if val == 0:
                        self.tiles.append(Tile(self.engine, (x, y), self.tile_height_map[y][x], self.engine.ressources_handler.images["terrain"]["cube1"]))
                    elif val == 1:
                        self.tiles.append(Tile(self.engine, (x, y), self.tile_height_map[y][x], self.engine.ressources_handler.images["terrain"]["cube2"]))
                    elif val == 2:
                        self.tiles.append(Tile(self.engine, (x, y), self.tile_height_map[y][x], self.engine.ressources_handler.images["terrain"]["cube3"]))
                    self.clusters[0].tiles.append(self.tiles[-1])  # TODO A changer plus tard :)

    def render_tiles(self):
        for tile in self.tiles:
            tile.render()

    def render_tiles_in_rect(self, rect):
        rect_offset = -rect.left, -rect.top

        for cluster in self.clusters:
            if rect.colliderect(cluster.rect):
                for tile in cluster.tiles:
                    if rect.colliderect(tile.rect_render):
                        tile.render(rect_offset)

    def render_hitbox(self):
        for tile in self.tiles:
            tile.render_hitbox()


if __name__ == "__main__":
    loop_handler = LoopHandler(120)

    engine = Engine()
    world = World(engine)
    camera = Camera(engine, (0, 0), world)

    while loop_handler.is_running():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop_handler.stop_loop()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop_handler.stop_loop()
                if event.key == pygame.K_DOWN:
                    Tile.height_multiplicator -= 1
                if event.key == pygame.K_UP:
                    Tile.height_multiplicator += 1

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_KP_8]:
            camera.move(0, -0.1)
        if key_pressed[pygame.K_KP_2]:
            camera.move(0, 0.1)
        if key_pressed[pygame.K_KP_4]:
            camera.move(-0.1, 0)
        if key_pressed[pygame.K_KP_6]:
            camera.move(0.1, 0)

        cam_rect = camera.rect

        engine.window.fill((0, 0, 0))
        world.render_tiles_in_rect(cam_rect)

        pygame.display.flip()
    pygame.quit()
