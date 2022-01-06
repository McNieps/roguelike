import pygame

from src_client.engine.world.library import get_iso_xy_from_xyz


class Tile:
    height_multiplicator = 5

    def __init__(self, engine, tile_index, tile_height, tile_image):
        tile_top_size = engine.ressources_handler.fetch_data(["world", "settings", "tile", "top_size"])
        sim_tile_size = engine.ressources_handler.fetch_data(["world", "settings", "tile", "sim_tile_size"])

        self.engine = engine
        self.tile_index = tile_index
        self.image = tile_image
        self.height = tile_height

        self.x = tile_index[0] * sim_tile_size[0]
        self.y = tile_index[1] * sim_tile_size[1]
        self.z = -self.height * Tile.height_multiplicator

        self.render_position = get_iso_xy_from_xyz(self.x, self.y, self.z)

        self.rect_render = pygame.Rect(self.render_position, tile_top_size)
        self.rect_sim = pygame.Rect((self.x, self.y), sim_tile_size)

    def render(self, offset=None):
        self.z = -self.height * Tile.height_multiplicator
        self.render_position = get_iso_xy_from_xyz(self.x, self.y, self.z)
        render_pos = self.render_position
        if offset:
            render_pos = (render_pos[0]+offset[0], render_pos[1]+offset[1])

        self.engine.window.blit(self.image, render_pos)
