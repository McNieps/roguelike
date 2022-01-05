import pygame

from src_client.engine.handlers.ressource_handler import RessourceHandler


class Engine:
    def __init__(self):
        print("Initializing Engine")
        self.ressources_handler = RessourceHandler()
        self.ressources_handler.pre_init()

        print("Creating window")
        self.window = self.create_window()
        self.ressources_handler.init()

        print("Loading ressources")
        self.ressources_handler.init()

    def create_window(self):
        window_size = self.ressources_handler.fetch_data(["engine", "window", "size"])
        is_scaled = self.ressources_handler.fetch_data(["engine", "window", "scaled"])
        window_name = self.ressources_handler.fetch_data(["engine", "window", "name"])
        use_icon = self.ressources_handler.fetch_data(["engine", "window", "use_icon"])

        if is_scaled:
            window = pygame.display.set_mode(window_size, pygame.SCALED)
        else:
            window = pygame.display.set_mode(window_size)

        pygame.display.set_caption(window_name)

        if use_icon:
            print("Normalement il y aura une icone")

        return window


if __name__ == "__main__":
    engine = Engine()
