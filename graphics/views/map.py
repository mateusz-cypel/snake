from typing import Tuple

import pygame

from board import Board
from models import Cell, BoardIndex
from settings import settings


class Map(pygame.Surface):
    def __init__(self):
        super().__init__(
            size=(settings.map.width, settings.map.height)
        )

        self._board = Board(
            rows=settings.map.height // settings.map.grid.cell.height,
            cols=settings.map.width // settings.map.grid.cell.width,
            value=None,
        )

        for y, top in enumerate(range(0, settings.map.height, settings.map.grid.cell.height)):
            for x, left in enumerate(range(0, settings.map.width, settings.map.grid.cell.height)):
                self._board.insert(
                    index=BoardIndex(x=x, y=y),
                    value=Cell(
                        left=left,
                        top=top,
                        width=settings.map.grid.cell.width,
                        height=settings.map.grid.cell.height
                    )
                )

        self.clear()
        self.draw_grid()

    def clear(self):
        self.fill(settings.map.background_color.rgb)
        if settings.map.grid.border.enabled:
            self.draw_border()

    def get_cell(self, index: BoardIndex) -> Cell:
        return self._board[index]

    def draw_border(self):
        color = settings.map.border_color.rgb

        for y in range(self._board.rows):
            if y == 0 or y == self._board.rows - 1:
                for x in range(self._board.cols):
                    cell = self._board[BoardIndex(x=x, y=y)]
                    rect = pygame.Rect(cell.left, cell.top, cell.width, cell.height)
                    self.fill(color, rect)

        for y in range(self._board.rows):
            for x in range(self._board.cols):
                if x == 0 or x == self._board.cols - 1:
                    cell = self._board[BoardIndex(x=x, y=y)]
                    rect = pygame.Rect(cell.left, cell.top, cell.width, cell.height)
                    self.fill(color, rect)

    def draw_grid(self) -> None:
        border_color = settings.map.grid.border.color.rgb
        border_thickness = settings.map.grid.border.thickness

        for y in range(self._board.rows):
            for x in range(self._board.cols):
                cell = self._board[BoardIndex(x=x, y=y)]
                rect = pygame.Rect(cell.left, cell.top, cell.width, cell.height)
                pygame.draw.rect(self, border_color, rect, border_thickness)
