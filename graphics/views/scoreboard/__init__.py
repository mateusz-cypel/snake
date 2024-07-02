from typing import Tuple, Dict

import pygame

from graphics.views.scoreboard.section import Section
from settings import settings


TITLES = [
    settings.scoreboard.score_title,
    settings.scoreboard.hi_score_title,
    settings.scoreboard.energy_title,
]


class Scoreboard(pygame.Surface):
    # todo update current score and hi-score in the same time
    #  when current score is a new hi-score

    def __init__(self):
        super().__init__(
            size=(settings.scoreboard.width, settings.scoreboard.height)
        )
        self.fill(settings.scoreboard.background_color.rgb)
        self._section_details: Dict[str, Tuple[Section, pygame.Rect]] = {}
        for i, title in enumerate(TITLES):
            _section = Section(
                header=title,
                value=settings.scoreboard.section.value,
                max_value=settings.scoreboard.section.max_value,
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
            self._section_details[title] = (_section, centered_rect)

    def update_score(self, value: int):
        self._section_details[settings.scoreboard.score_title][0].update_value(value)
        self.blit(*self._section_details[settings.scoreboard.score_title])

    def update_hi_score(self, value: int):
        self._section_details[settings.scoreboard.hi_score_title][0].update_value(value)
        self.blit(*self._section_details[settings.scoreboard.hi_score_title])

    def update_energy(self, value: int):
        self._section_details[settings.scoreboard.energy_title][0].update_value(value)
        self.blit(*self._section_details[settings.scoreboard.energy_title])
