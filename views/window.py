import pygame

from views.map import Map
from views.scoreboard import Scoreboard

WINDOW_SIZE = (800, 600)
WINDOW_TITLE = "Hungry Python"


class Window:
    def __init__(self):
        self.display_surface = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption(WINDOW_TITLE)
        self.map = Map()
        self.scoreboard = Scoreboard()
        self.display_surface.blit(self.map, (0, 0))
        self.display_surface.blit(self.scoreboard, (600, 0))
