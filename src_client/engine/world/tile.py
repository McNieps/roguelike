class Tile:
    def __init__(self, position, image):
        self.position = position
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position
