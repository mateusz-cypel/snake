import pygame

SCOREBOARD_SIZE = (200, 600)
SCOREBOARD_BACKGROUND_COLOR = (18, 18, 176)


class Scoreboard(pygame.Surface):
    def __init__(self):
        super().__init__(SCOREBOARD_SIZE)
        self.fill(SCOREBOARD_BACKGROUND_COLOR)
