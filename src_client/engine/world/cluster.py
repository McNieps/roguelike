import pygame


class Cluster:
    def __init__(self, rect=None):
        self.rect = pygame.Rect(0, 0, 640, 480)
        self.tiles = []
