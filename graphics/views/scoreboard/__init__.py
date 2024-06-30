from typing import Tuple

import pygame

from graphics.views.scoreboard.section import Section

SCOREBOARD_SIZE = (200, 600)
SCOREBOARD_BACKGROUND_COLOR = (18, 18, 176)
SCOREBOARD_TITLES = (
    "SCORE",
    "HI-SCORE",
    "ENERGY",
)
SCOREBOARD_SECTION_BORDER_RADIUS = 25
SCOREBOARD_SECTION_BORDER_THICKNESS = 3
SCOREBOARD_SECTION_DEFAULT_VALUE = 0
SCOREBOARD_SECTION_FONT_SIZE = 20
SCOREBOARD_SECTION_PADDING = (45, 15)
SCOREBOARD_SECTION_SPACING = 10
SCOREBOARD_SECTION_START_POINT = (0, 20)

LABEL_FONT_COLOR = (123, 123, 123)


class Scoreboard(pygame.Surface):
    # todo update current score and hi-score in the same time
    #  when current score is a new hi-score

    def __init__(self):
        super().__init__(SCOREBOARD_SIZE)
        self.fill(SCOREBOARD_BACKGROUND_COLOR)
        for i, title in enumerate(SCOREBOARD_TITLES):
            _section = Section(
                header=title,
                value=SCOREBOARD_SECTION_DEFAULT_VALUE,
                color=LABEL_FONT_COLOR,
                background_color=SCOREBOARD_BACKGROUND_COLOR,
                border_radius=SCOREBOARD_SECTION_BORDER_RADIUS,
                border_thickness=SCOREBOARD_SECTION_BORDER_THICKNESS,
                font_size=SCOREBOARD_SECTION_FONT_SIZE,
                padding=SCOREBOARD_SECTION_PADDING,
            )

            x, y = SCOREBOARD_SECTION_START_POINT
            centered_rect = pygame.Rect(
                x + self.get_width() / 2 - _section.get_width() / 2,
                y + i * (_section.get_height() + SCOREBOARD_SECTION_SPACING),
                _section.get_width(),
                _section.get_height(),
            )
            self.blit(_section, centered_rect)

    @property
    def left_top(self) -> Tuple[int, int]:
        return self.config["left_top"]