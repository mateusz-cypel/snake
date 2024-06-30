from typing import Tuple

import pygame

from board import Board
from models import Cell, BoardIndex


class Map(pygame.Surface):
    def __init__(self, config: dict):
        self.config = config
        super().__init__(self.config["size"])

        map_width, map_height = self.config["size"]
        cell_width, cell_height = self.config["grid"]["cell"]["size"]

        self._board = Board(
            rows=map_height // cell_height,
            cols=map_width // cell_width,
            value=None,
        )

        for y, top in enumerate(range(0, map_height, cell_height)):
            for x, left in enumerate(range(0, map_width, cell_width)):
                self._board.insert(
                    index=BoardIndex(x=x, y=y),
                    value=Cell(left=left, top=top, width=cell_width, height=cell_height)
                )

        self.clear()
        self.draw_grid()

    @property
    def left_top(self) -> Tuple[int, int]:
        return self.config["left_top"]

    def clear(self):
        self.fill(self.config["background_color"])
        if self.config["grid"]["border"]["enabled"]:
            self.draw_border()

    def get_cell(self, index: BoardIndex) -> Cell:
        return self._board[index]

    def draw_border(self):
        color = self.config["border_color"]

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
        border_color = self.config["grid"]["border"]["color"]
        border_thickness = self.config["grid"]["border"]["thickness"]

        for y in range(self._board.rows):
            for x in range(self._board.cols):
                cell = self._board[BoardIndex(x=x, y=y)]
                rect = pygame.Rect(cell.left, cell.top, cell.width, cell.height)
                pygame.draw.rect(self, border_color, rect, border_thickness)
