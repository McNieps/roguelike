import pygame

from src_client.engine.engine import Engine


class Camera:
    def __init__(self, engine: Engine, position: tuple, world) -> None:
        # Position and motion of camera
        self.position = position
        self.x = position[0]
        self.y = position[1]
        self.vx = 0
        self.vy = 0

        # Other
        self.engine = engine
        self.world = world

        # Screen
        self.screen_size = self.engine.ressources_handler.fetch_data(["engine", "window", "size"])

        # Rect
        self.rect = pygame.Rect((0, 0), self.screen_size)
        self.rect.center = (self.x, self.y)

        # Object fellowing
        self.currently_fellowing = False
        self.linked_entity = None

    def move(self, x: float, y: float, increment: bool = True):
        if increment:
            self.x += x
            self.y += y
        else:
            self.x = x
            self.y = y

        self.rect.center = (self.x, self.y)
