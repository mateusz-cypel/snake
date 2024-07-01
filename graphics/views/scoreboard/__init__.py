from typing import Tuple

import pygame

from graphics.views.scoreboard.section import Section
from settings import settings


class Scoreboard(pygame.Surface):
    # todo update current score and hi-score in the same time
    #  when current score is a new hi-score

    def __init__(self):
        super().__init__(
            size=(settings.scoreboard.width, settings.scoreboard.height)
        )
        self.fill(settings.scoreboard.background_color.rgb)
        for i, title in enumerate(settings.scoreboard.titles):
            _section = Section(
                header=title,
                value=settings.scoreboard.section.value,
                font_color=settings.scoreboard.section.font_color,
                background_color=settings.scoreboard.background_color,
                border_radius=settings.scoreboard.section.border.radius,
                border_thickness=settings.scoreboard.section.border.thickness,
                border_color=settings.scoreboard.section.border.color,
                font_size=settings.scoreboard.section.font_size,
                padding=settings.scoreboard.section.padding,
                spacing=settings.scoreboard.section.spacing
            )

            x = settings.scoreboard.section.starting_point.x
            y = settings.scoreboard.section.starting_point.y
            centered_rect = pygame.Rect(
                x + self.get_width() / 2 - _section.get_width() / 2,
                y + i * (_section.get_height() + settings.scoreboard.section.spacing),
                _section.get_width(),
                _section.get_height(),
            )
            self.blit(_section, centered_rect)
