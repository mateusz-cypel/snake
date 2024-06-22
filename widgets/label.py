import pygame

DEFAULT_FONT_COLOR = (0, 0, 0)
DEFAULT_FONT_NAME = "Arial"
DEFAULT_FONT_SIZE = 20


class Label:
    def __init__(
        self,
        text: str,
        color: str = DEFAULT_FONT_COLOR,
        font_size: int = DEFAULT_FONT_SIZE,
    ):
        self._text = text
        self.font = pygame.font.SysFont(DEFAULT_FONT_NAME, size=font_size)
        self.image = self.font.render(text, True, color)
        _, _, w, h = self.image.get_rect()
        self.rect = pygame.Rect(0, 0, w, h)
