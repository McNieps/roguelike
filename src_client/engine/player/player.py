import pygame

from src_client.engine.library.tools import add_tuples

class Player:
    def __init__(self, engine, player_image):
        self.engine = engine
        self.image = player_image

        self.position = self.engine.ressources_handler.fetch_data(["engine", "window", "size"])
        self.position = (self.position[0] / 2 - 10, self.position[1] / 2 - 16)
        self.x = self.position[0]
        self.y = self.position[1]

        self.offset = (0, 0)
        self.maxOffset = 40

        self.speed = 100

    def render(self,  offset = None):
        self.engine.window.blit(self.image, add_tuples(self.position, self.offset))

    def move_left(self, delta):
        self.offset = add_tuples(self.offset, (- self.speed * delta, 0))
        self.check_offset()

    def move_right(self, delta):
        self.offset = add_tuples(self.offset, (self.speed * delta, 0))
        self.check_offset()

    def move_up(self, delta):
        self.offset = add_tuples(self.offset, (0, - self.speed * delta))
        self.check_offset()

    def move_down(self, delta):
        self.offset = add_tuples(self.offset, (0, self.speed * delta))
        self.check_offset()

    def check_offset(self):
        if(self.offset[0] > self.maxOffset):
            self.offset = (self.maxOffset, self.offset[1])
        elif(self.offset[0] < - self.maxOffset):
            self.offset = (- self.maxOffset, self.offset[1])
        if(self.offset[1] > self.maxOffset):
            self.offset = (self.offset[0], self.maxOffset)
        elif (self.offset[1] < - self.maxOffset):
            self.offset = (self.offset[0], - self.maxOffset)