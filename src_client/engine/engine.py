import pygame


from src_client.engine.handlers.ressource_handler import RessourceHandler


class Engine:
    def __init__(self):
        print("Initializing Engine")
        self.ressources_handler = RessourceHandler()
        self.ressources_handler.pre_init()
        print(self.ressources_handler.data)
        self.window = self.create_window()

    def create_window(self):
        window_size = self.ressources_handler.fetch_data(["engine", "window", "size"])
        is_scaled = self.ressources_handler.fetch_data(["engine", "window", "scaled"])

        if is_scaled:
            window = pygame.display.set_mode(window_size, pygame.SCALED)
        else:
            window = pygame.display.set_mode(window_size)

        return window


if __name__ == "__main__":
    engine = Engine()
