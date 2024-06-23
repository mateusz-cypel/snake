from typing import Any, Tuple

import pygame

from graphics.widgets import Label

DEFAULT_SPACING = 10
DEFAULT_PADDING = (0, 0)
DEFAULT_BORDER_COLOR = (0, 0, 0)


# todo border validation, all params > 0
class Section(pygame.Surface):
    def __init__(
        self,
        header: str,
        value: int,
        color: Any,
        font_size: int,
        background_color: Any,
        border_radius: int,
        border_thickness: int,
        border_color: Any = DEFAULT_BORDER_COLOR,
        spacing: int = DEFAULT_SPACING,
        padding: Tuple[int, int] = DEFAULT_PADDING,
    ):
        self.header_label = Label(header, color, font_size)
        self.value_label = Label(str(value), color, font_size)

        padding_x, padding_y = padding
        width = max(self.header_label.rect.w, self.value_label.rect.w) + padding_x * 2
        height = (
            self.header_label.rect.h + spacing + self.value_label.rect.h + padding_y * 2
        )

        super().__init__(size=(width, height))
        self.fill(background_color)

        header_rect = pygame.Rect(
            width / 2 - self.header_label.rect.w / 2,
            padding_y + self.header_label.rect.y,
            self.header_label.rect.w,
            self.header_label.rect.h,
        )

        value_rect = pygame.Rect(
            width / 2 - self.value_label.rect.w / 2,
            padding_y + self.header_label.rect.h + spacing,
            self.value_label.rect.w,
            self.value_label.rect.h,
        )

        self.blit(self.header_label.image, header_rect)
        self.blit(self.value_label.image, value_rect)
        pygame.draw.rect(
            self, border_color, self.get_rect(), border_thickness, border_radius
        )
