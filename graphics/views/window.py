import pygame

from graphics.views.map import Map
from graphics.views.scoreboard import Scoreboard


class Window:
    def __init__(self, config: dict):
        self.display_surface = pygame.display.set_mode(config["window"]["size"])
        pygame.display.set_caption(config["window"]["title"])
        self.map = Map(config=config["window"]["map"])
        self.scoreboard = Scoreboard(config=config["window"]["scoreboard"])
        self.refresh()

    def refresh(self):
        self.display_surface.blit(self.map, self.map.left_top)
        self.display_surface.blit(self.scoreboard, self.scoreboard.left_top)