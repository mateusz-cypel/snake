import pygame

import utils


class Fruit(pygame.Rect):
    color: utils.Color = None

    def __init__(self, left: float, top: float, width: float, height: float):
        if not self.color:
            raise ValueError(f"Color {utils.Color.__class__} must be defined")
        super().__init__(left, top, width, height)

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill(self.color, self)


class Apple(Fruit):
    color = (9, 154, 38)


class Orange(Fruit):
    color = (223, 111, 25)


class Strawberry(Fruit):
    color = (176, 18, 18)
