import pygame

from graphics.widgets import Label
from settings import Color, Padding


# todo border validation, all params > 0
class Section(pygame.Surface):
    def __init__(
        self,
        header: str,
        value: int,
        max_value: int,
        font_color: Color,
        font_size: int,
        background_color: Color,
        border_radius: int,
        border_thickness: int,
        border_color: Color,
        spacing: int,
        padding: Padding,
    ):
        self.header_label = Label(header, font_color.rgb, font_size)
        self.value_label = Label(f'{max_value:,} (MAX)', font_color.rgb, font_size)
        width = max(self.header_label.rect.w, self.value_label.rect.w) + padding.x * 2
        height = (
            self.header_label.rect.h + spacing + self.value_label.rect.h + padding.y * 2
        )
        super().__init__(size=(width, height))
        self.padding = padding
        self.spacing = spacing
        self.font_color = font_color
        self.font_size = font_size
        self.max_value = max_value
        self.background_color = background_color

        self.fill(self.background_color.rgb)
        self._draw_border(border_color, border_thickness, border_radius)
        self._draw_header_label()
        self.update_value(value)

    def update_value(self, value: int):
        text = f'{self.max_value:,} (MAX)' if value >= self.max_value else f'{value:,}'
        self.value_label = self.value_label = Label(text, self.font_color.rgb, self.font_size)
        self._draw_value_label()

    def _draw_border(self, color: Color, thickness: int, radius: int):
        pygame.draw.rect(self, color.rgb, self.get_rect(), thickness, radius)

    def _draw_header_label(self):
        header_rect = pygame.Rect(
            self.get_width() / 2 - self.header_label.rect.w / 2,
            self.padding.y + self.header_label.rect.y,
            self.header_label.rect.w,
            self.header_label.rect.h,
        )
        self.blit(self.header_label.image, header_rect)

    def _draw_value_label(self) -> None:
        value_rect = pygame.Rect(
            self.get_width() / 2 - self.value_label.rect.w / 2,
            self.padding.y + self.header_label.rect.h + self.spacing,
            self.value_label.rect.w,
            self.value_label.rect.h,
        )

        rect_to_clear = pygame.Rect(
            self.get_rect().left + self.padding.x,
            value_rect.top,
            self.get_width() - self.padding.x * 2,
            value_rect.height
        )
        self.fill(self.background_color.rgb, rect_to_clear)
        self.blit(self.value_label.image, value_rect)
