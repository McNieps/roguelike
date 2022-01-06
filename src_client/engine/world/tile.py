import pygame

from src_client.engine.world.library import get_tile_xy_coords_from_tile_index


class Tile:
    def __init__(self, engine, tile_index, tile_image):
        tile_top_size = engine.ressources_handler.fetch_data(["world", "settings", "tile", "top_size"])
        sim_tile_size = engine.ressources_handler.fetch_data(["world", "settings", "tile", "sim_tile_size"])

        self.engine = engine
        self.tile_index = tile_index
        self.image = tile_image

        self.sim_position = tile_index[0] * sim_tile_size[0], tile_index[1] * sim_tile_size[1]
        self.render_position = get_tile_xy_coords_from_tile_index(tile_index)

        self.rect_render = pygame.Rect(self.render_position, tile_top_size)
        self.rect_sim = pygame.Rect(self.sim_position, sim_tile_size)

        self.p1 = get_tile_xy_coords_from_tile_index(self.tile_index, (16, 0))
        self.p2 = get_tile_xy_coords_from_tile_index((self.tile_index[0] + 1, self.tile_index[1]), (16, 0))
        self.p3 = get_tile_xy_coords_from_tile_index((self.tile_index[0] + 1, self.tile_index[1] + 1), (16, 0))
        self.p4 = get_tile_xy_coords_from_tile_index((self.tile_index[0], self.tile_index[1] + 1), (16, 0))

    def render(self):
        self.engine.window.blit(self.image, self.render_position)

    def render_hitbox(self):
        pygame.draw.line(self.engine.window, (255, 0, 0), self.p1, self.p2)
        pygame.draw.line(self.engine.window, (255, 0, 0), self.p2, self.p3)
        pygame.draw.line(self.engine.window, (255, 0, 0), self.p3, self.p4)
        pygame.draw.line(self.engine.window, (255, 0, 0), self.p4, self.p1)
