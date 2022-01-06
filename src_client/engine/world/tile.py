import pygame

from src_client.engine.world.library import get_iso_xy_from_xyz


class Tile:
    height_multiplicator = 5

    def __init__(self, engine, tile_index, tile_height: float, tile_image: pygame.Surface):
        sim_tile_size = engine.ressources_handler.fetch_data(["world", "settings", "tile", "sim_tile_size"])

        self.engine = engine

        # Specific data
        self.tile_index = tile_index
        self.image = tile_image
        self.height = tile_height

        # Simulation
        self.x = tile_index[0] * sim_tile_size[0]
        self.y = tile_index[1] * sim_tile_size[1]
        self.z = -self.height * Tile.height_multiplicator
        self.sim_rect = pygame.Rect((self.x, self.y), sim_tile_size)

        # Rendering
        self.render_position = get_iso_xy_from_xyz(self.x, self.y, self.z, (-16, 0))
        self.render_rect = pygame.Rect(self.render_position, self.image.get_size())

        # Hitbox rendering
        self.p1 = get_iso_xy_from_xyz(self.sim_rect.left, self.sim_rect.top, self.z)
        self.p2 = get_iso_xy_from_xyz(self.sim_rect.right, self.sim_rect.top, self.z)
        self.p3 = get_iso_xy_from_xyz(self.sim_rect.right, self.sim_rect.bottom, self.z)
        self.p4 = get_iso_xy_from_xyz(self.sim_rect.left, self.sim_rect.bottom, self.z)

    def update_tile(self):
        self.z = -self.height * Tile.height_multiplicator
        self.render_position = get_iso_xy_from_xyz(self.x, self.y, self.z, (-16, 0))
        self.render_rect.topleft = self.render_position

    def update_hitbox(self):
        self.p1 = get_iso_xy_from_xyz(self.sim_rect.left, self.sim_rect.top, self.z)
        self.p2 = get_iso_xy_from_xyz(self.sim_rect.right, self.sim_rect.top, self.z)
        self.p3 = get_iso_xy_from_xyz(self.sim_rect.right, self.sim_rect.bottom, self.z)
        self.p4 = get_iso_xy_from_xyz(self.sim_rect.left, self.sim_rect.bottom, self.z)

    def show_rect(self, offset: tuple = (0, 0)):
        render_pos = (self.render_position[0]+offset[0], self.render_position[1]+offset[1])
        pygame.draw.rect(self.engine.window, (20, 20, 20), (render_pos, self.image.get_size()))

    def render(self, offset: tuple = (0, 0)):
        render_pos = (self.render_position[0]+offset[0], self.render_position[1]+offset[1])
        self.engine.window.blit(self.image, render_pos)

    def render_hitbox(self, offset: tuple = (0, 0)):
        p1 = self.p1[0] + offset[0], self.p1[1] + offset[1]   # TODO utiliser la fonction magic de Théo
        p2 = self.p2[0] + offset[0], self.p2[1] + offset[1]
        p3 = self.p3[0] + offset[0], self.p3[1] + offset[1]
        p4 = self.p4[0] + offset[0], self.p4[1] + offset[1]
        pygame.draw.line(self.engine.window, (50, 50, 255), p1, p2)
        pygame.draw.line(self.engine.window, (50, 50, 255), p2, p3)
        pygame.draw.line(self.engine.window, (50, 50, 255), p3, p4)
        pygame.draw.line(self.engine.window, (50, 50, 255), p4, p1)
