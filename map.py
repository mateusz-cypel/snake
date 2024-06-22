import pygame

MAP_SIZE = (600, 600)
MAP_BACKGROUND_COLOR = (176, 18, 18)


class Map(pygame.Surface):
    def __init__(self):
        super().__init__(MAP_SIZE)
        self.fill(MAP_BACKGROUND_COLOR)
