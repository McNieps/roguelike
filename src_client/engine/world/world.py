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
        self.clusters = {}

        self.fill_tiles_list()

    def fill_tiles_list(self):
        cluster_size = self.engine.ressources_handler.fetch_data(["world", "settings", "cluster", "size"])

        for y in range(len(self.tile_index_map)):

            for x in range(len(self.tile_index_map[0])):

                if self.tile_index_map[y][x]:
                    tile_height = self.tile_height_map[y][x]
                    tile_image = self.engine.ressources_handler.images["terrain"][f"cube{randint(1, 3)}"]
                    tile = Tile(self.engine, (x, y), tile_height, tile_image)

                    # TODO AJOUTER RECT MARGIN POUR PREVENIR LES DEPLACEMENTS
                    min_x = tile.render_rect.left
                    max_x = tile.render_rect.right
                    min_y = tile.render_rect.top
                    max_y = tile.render_rect.bottom

                    cluster_left = min_x // cluster_size[0]
                    cluster_right = max_x // cluster_size[0]
                    cluster_top = min_y // cluster_size[1]
                    cluster_bottom = max_y // cluster_size[1]

                    for cluster_x in range(cluster_left, cluster_right+1):
                        for cluster_y in range(cluster_top, cluster_bottom+1):
                            cluster_index = (cluster_x, cluster_y)
                            if cluster_index not in self.clusters:
                                cluster_pos = (cluster_x * cluster_size[0], cluster_y * cluster_size[1])
                                cluster_rect = pygame.Rect(cluster_pos, cluster_size)
                                self.clusters[cluster_index] = Cluster(cluster_rect)
                            self.clusters[cluster_index].tiles.append(tile)

                    self.tiles.append(tile)

        for key in self.clusters:
            print(self.clusters[key].rect)

    def render_tiles(self, rect: pygame.Rect):
        """
        le rectangle correspond à la zone de vue. Obtenable via la camera normalement
        """

        rect_offset = -rect.left, -rect.top
        for key in self.clusters:
            cluster = self.clusters[key]
            cluster_adjusted_rect = pygame.Rect((cluster.rect.left - rect.left, cluster.rect.top - rect.top), cluster.rect.size)
            pygame.draw.rect(self.engine.window, (255, 255, 255), cluster_adjusted_rect)
            if rect.colliderect(cluster.rect):
                for tile in cluster.tiles:
                    if rect.colliderect(tile.render_rect):
                        # tile.show_rect(rect_offset)
                        tile.render(rect_offset)
                        # tile.render_hitbox(rect_offset)


if __name__ == "__main__":
    loop_handler = LoopHandler(120)

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
                if event.key == pygame.K_DOWN:
                    Tile.height_multiplicator -= 1
                    for _tile in world.tiles:
                        _tile.update_tile()
                        _tile.update_hitbox()
                if event.key == pygame.K_UP:
                    Tile.height_multiplicator += 1
                    for _tile in world.tiles:
                        _tile.update_tile()
                        _tile.update_hitbox()

        key_pressed = pygame.key.get_pressed()
        cam_speed = 100 * delta
        if key_pressed[pygame.K_KP_8]:
            camera.move(0, -cam_speed)
        if key_pressed[pygame.K_KP_2]:
            camera.move(0, cam_speed)
        if key_pressed[pygame.K_KP_4]:
            camera.move(-cam_speed, 0)
        if key_pressed[pygame.K_KP_6]:
            camera.move(cam_speed, 0)

        cam_rect = camera.rect

        engine.window.fill((0, 0, 0))
        world.render_tiles(cam_rect)

        pygame.display.flip()
    pygame.quit()
