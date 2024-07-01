import pygame

from graphics.widgets import Label
from settings import Color, Padding


# todo border validation, all params > 0
class Section(pygame.Surface):
    def __init__(
        self,
        header: str,
        value: int,
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
        self.value_label = Label(str(value), font_color.rgb, font_size)

        width = max(self.header_label.rect.w, self.value_label.rect.w) + padding.x * 2
        height = (
            self.header_label.rect.h + spacing + self.value_label.rect.h + padding.y * 2
        )

        super().__init__(size=(width, height))
        self.fill(background_color.rgb)

        header_rect = pygame.Rect(
            width / 2 - self.header_label.rect.w / 2,
            padding.y + self.header_label.rect.y,
            self.header_label.rect.w,
            self.header_label.rect.h,
        )

        value_rect = pygame.Rect(
            width / 2 - self.value_label.rect.w / 2,
            padding.y + self.header_label.rect.h + spacing,
            self.value_label.rect.w,
            self.value_label.rect.h,
        )

        self.blit(self.header_label.image, header_rect)
        self.blit(self.value_label.image, value_rect)
        pygame.draw.rect(
            self, border_color.rgb, self.get_rect(), border_thickness, border_radius
        )
