import pygame

from random import randint

from src_client.engine.engine import Engine
from src_client.engine.handlers.loop_handler import LoopHandler

from src_client.engine.world.tile import Tile
from src_client.engine.world.camera import Camera
from src_client.engine.world.library import get_tile_index_from_iso_xy, get_tile_list_in_rect_by_order


class World:
    def __init__(self, _engine: Engine):
        self.engine = _engine

        self.tile_index_map = []
        self.tile_height_map = []
        self.create_tile_and_height_map()

        self.tiles = {}

        self.fill_tiles_list()

    def create_tile_and_height_map(self):
        size = 32
        for i in range(size):
            liste = []
            for j in range(size):
                liste.append(1)
            self.tile_index_map.append(liste)

        for i in range(size):
            liste = []
            for j in range(size):
                liste.append(0)
            self.tile_height_map.append(liste)

    def fill_tiles_list(self):
        for y in range(len(self.tile_index_map)):
            for x in range(len(self.tile_index_map[0])):
                if self.tile_index_map[y][x]:
                    tile_height = self.tile_height_map[y][x]
                    tile_image = self.engine.ressources_handler.images["terrain"][f"cube{randint(3, 3)}"]
                    tile = Tile(self.engine, (x, y), tile_height, tile_image)

                    self.tiles[(x, y)] = tile

    def render_tiles(self, rect: pygame.Rect):
        """
        le rectangle correspond à la zone de vue. Obtenable via la camera normalement
        """

        rect_offset = -rect.left, -rect.top

        for _index in self.tiles:
            tile = self.tiles[_index]
            if rect.colliderect(tile.render_rect):
                tile.render(rect_offset)


if __name__ == "__main__":
    loop_handler = LoopHandler(12000)

    engine = Engine()
    world = World(engine)
    camera = Camera(engine, (0, 0), world)

    while loop_handler.is_running():
        delta = loop_handler.limit_and_get_delta()
        # loop_handler.print_fps()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop_handler.stop_loop()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop_handler.stop_loop()
                if event.key == pygame.K_RETURN:
                    world.fill_tiles_list()

        key_pressed = pygame.key.get_pressed()
        cam_speed = 100 * delta
        if key_pressed[pygame.K_z]:
            camera.move(0, -cam_speed)
        if key_pressed[pygame.K_s]:
            camera.move(0, cam_speed)
        if key_pressed[pygame.K_q]:
            camera.move(-cam_speed, 0)
        if key_pressed[pygame.K_d]:
            camera.move(cam_speed, 0)

        engine.window.fill((0, 0, 0))

        cam_rect = camera.rect
        offset = -cam_rect.left, -cam_rect.top

        tile_list = get_tile_list_in_rect_by_order(cam_rect)
        for tile_index in tile_list:
            if tile_index in world.tiles:
                world.tiles[tile_index].render(offset)

        """mouse_x, mouse_y = pygame.mouse.get_pos()
        tile_index = get_tile_index_from_iso_xy(mouse_x, mouse_y, cam_rect)
        tile_index = (floor(tile_index[0]), floor(tile_index[1]))
        if tile_index in world.tiles:
            world.tiles[tile_index].render_hitbox(offset)"""

        pygame.display.flip()
    pygame.quit()
