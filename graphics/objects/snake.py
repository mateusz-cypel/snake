import pygame

import utils


class SnakePart(pygame.Rect):
    color: utils.Color = None

    def __init__(self, left: float, top: float, width: float, height: float):
        if not self.color:
            raise ValueError(f"Color {utils.Color.__class__} must be defined")
        super().__init__(left, top, width, height)

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill(self.color, self)


class SnakeBody(SnakePart):
    color = (225, 175, 209)


class SnakeHead(SnakePart):
    color = (173, 136, 198)
