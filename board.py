from typing import Optional, Any

from models import BoardIndex


class Board:
    def __init__(self, rows: int, cols: int, value: Optional[Any] = None, border_value: Optional[Any] = None):
        self.rows = rows
        self.cols = cols
        self._matrix = [
            [value for _ in range(self.cols)]
            for _ in range(self.rows)
        ]
        if border_value is not None:
            self._apply_border(border_value)

    def __getitem__(self, index: BoardIndex) -> Any:
        if not isinstance(index, BoardIndex):
            raise Exception("Unknown index")
        return self._matrix[index.y][index.x]

    def insert(self, index: BoardIndex, value: Optional[Any]) -> None:
        self._matrix[index.y][index.x] = value

    def _apply_border(self, border_value: Optional[Any]) -> None:
        # -1 -1 -1 -1
        #  0  0  0  0
        #  0  0  0  0
        # -1 -1 -1 -1
        for y in range(self.rows):
            if y == 0 or y == self.rows - 1:
                for x in range(self.cols):
                    self._matrix[y][x] = border_value

        # -1  0  0 -1
        # -1  0  0 -1
        # -1  0  0 -1
        # -1  0  0 -1
        for y in range(self.rows):
            for x in range(self.cols):
                if x == 0 or x == self.cols - 1:
                    self._matrix[y][x] = border_value
