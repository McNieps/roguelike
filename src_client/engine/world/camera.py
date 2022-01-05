from src_client.engine.world.world import World


class Camera:
    def __init__(self, position: tuple, world: World):
        # Position and motion of camera
        self.position = position
        self.x = position[0]
        self.y = position[1]
        self.vx = 0
        self.vy = 0

        

