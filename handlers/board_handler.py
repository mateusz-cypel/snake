from enum import Enum, auto
from typing import Iterable, Tuple

from board import Board
from models import Size, Fruit, Apple, Orange, Strawberry, BoardIndex, Move

BORDER_SIGN = -1
EMPTY_SIGN = 0
SNAKE_HEAD = 1
SNAKE_BODY = 2
SNAKE_TAIL = 3
APPLE_FRUIT_SIGN = 4
ORANGE_FRUIT_SIGN = 5
STRAWBERRY_FRUIT_SIGN = 6


class CollisionStatus(Enum):
    BORDER_COLLISION = auto()
    FRUIT_COLLISION = auto()
    NO_COLLISION = auto()
    SNAKE_COLLISION = auto()


class BoardFruitMapper:
    @staticmethod
    def get_sign(fruit: Fruit) -> int:
        if isinstance(fruit, Apple):
            return APPLE_FRUIT_SIGN
        if isinstance(fruit, Orange):
            return ORANGE_FRUIT_SIGN
        if isinstance(fruit, Strawberry):
            return STRAWBERRY_FRUIT_SIGN
        raise Exception("Fruit type not handled")


class BoardHandler:
    def __init__(self, board_size: Size, cell_size: Size):
        self.snake_head_index: BoardIndex = None
        self.snake_tail_index: BoardIndex = None

        self.current_fruit: Fruit = None
        self.current_fruit_index: BoardIndex = None

        self._board = Board(
            rows=board_size.height // cell_size.height,
            cols=board_size.width // cell_size.width,
            value=EMPTY_SIGN,
            border_value=BORDER_SIGN
        )

    def _add_object(self, index: BoardIndex, sign: int) -> None:
        # todo validation
        self._board.insert(index=index, value=sign)

    def add_fruit(self, index: BoardIndex, fruit: Fruit) -> None:
        self.current_fruit = fruit
        self.current_fruit_index = index
        sign = BoardFruitMapper.get_sign(fruit)
        self._add_object(index=index, sign=sign)

    def add_snake_head(self, index: BoardIndex):
        self.snake_head_index = index
        self._add_object(index=self.snake_head_index, sign=SNAKE_HEAD)

    def move_snake_to(self, index: BoardIndex):
        self.clear_cell(self.snake_head_index)
        self.add_snake_head(index=index)

    def clear_cell(self, index: BoardIndex):
        self._add_object(index=index, sign=EMPTY_SIGN)

    def check_collision(self, index: BoardIndex):
        sign = self._board[index]
        if sign in (EMPTY_SIGN, SNAKE_HEAD):
            return CollisionStatus.NO_COLLISION
        if sign in (SNAKE_BODY, SNAKE_TAIL):
            return CollisionStatus.SNAKE_COLLISION
        if sign in (
            APPLE_FRUIT_SIGN, ORANGE_FRUIT_SIGN, STRAWBERRY_FRUIT_SIGN
        ):
            return CollisionStatus.FRUIT_COLLISION
        if sign == BORDER_SIGN:
            return CollisionStatus.BORDER_COLLISION
        raise Exception("Unexpected collision behaviour")

    @property
    def free_spots(self) -> Iterable[BoardIndex]:
        indices = []
        for y in range(self._board.rows):
            for x in range(self._board.cols):
                index = BoardIndex(x=x, y=y)
                if self._board[index] == EMPTY_SIGN:
                    indices.append(index)
        return indices

