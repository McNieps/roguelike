import pygame

from random import randint

from src_client.engine.engine import Engine
from src_client.engine.handlers.loop_handler import LoopHandler

from src_client.engine.world.tile import Tile
from src_client.engine.world.cluster import Cluster
from src_client.engine.world.camera import Camera
from src_client.engine.player.player import Player


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

    def render_tiles(self, rect: pygame.Rect):
        """
        le rectangle correspond à la zone de vue. Obtenable via la camera normalement
        """

        rect_offset = -rect.left, -rect.top

        for cluster in self.clusters:
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
    player = Player(engine, engine.ressources_handler.images["player"]["player"])
    camera.center_on_entity(player)

    while loop_handler.is_running():
        delta = loop_handler.limit_and_get_delta()
        #loop_handler.print_fps()

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
        cam_speed = player.speed * delta
        if key_pressed[pygame.K_KP_8]:
            player.move_up(delta)
            if(player.offset[1] <= - player.maxOffset):
                camera.move(0, - cam_speed)
        if key_pressed[pygame.K_KP_2]:
            player.move_down(delta)
            if(player.offset[1] >= player.maxOffset):
                camera.move(0, cam_speed)
        if key_pressed[pygame.K_KP_4]:
            player.move_left(delta)
            if(player.offset[0] <= - player.maxOffset):
                camera.move(- cam_speed, 0)
            #camera.move(-cam_speed, 0)
        if key_pressed[pygame.K_KP_6]:
            player.move_right(delta)
            if(player.offset[0] >= player.maxOffset):
                camera.move(cam_speed, 0)
            #camera.move(cam_speed, 0)

        #camera.center_on_entity(player)

        cam_rect = camera.rect

        engine.window.fill((0, 0, 0))
        world.render_tiles(cam_rect)
        player.render()

        pygame.display.flip()
    pygame.quit()
