import pygame


class Object(pygame.Rect):
    color = None

    def __init__(self, left: float, top: float, width: float, height: float):
        if not self.color:
            raise ValueError(f"Color must be defined")
        super().__init__(left, top, width, height)

    def draw_on(self, surface: pygame.Surface) -> None:
        surface.fill(self.color, self)
