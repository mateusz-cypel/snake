import pygame

MAP_SIZE = (600, 600)
MAP_BACKGROUND_COLOR = (176, 18, 18)
GRID_BORDER_COLOR = (0, 0, 0)
GRID_BORDER_THICKNESS = 1
GRID_SIZE = (60, 60)


class Map(pygame.Surface):
    def __init__(self):
        super().__init__(MAP_SIZE)
        self.fill(MAP_BACKGROUND_COLOR)
        for x in range(0, MAP_SIZE[0], GRID_SIZE[0]):
            for y in range(0, MAP_SIZE[1], GRID_SIZE[0]):
                rect = pygame.Rect(x, y, GRID_SIZE[0], GRID_SIZE[1])
                pygame.draw.rect(self, GRID_BORDER_COLOR, rect, GRID_BORDER_THICKNESS)
