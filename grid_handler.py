from typing import Iterable, Tuple

from models import Size, Fruit, Apple, Orange, Strawberry

BORDER_SIGN = -1
EMPTY_SIGN = 0
SNAKE_HEAD = 1
SNAKE_BODY = 2
SNAKE_TAIL = 3
APPLE_FRUIT_SIGN = 4
ORANGE_FRUIT_SIGN = 5
STRAWBERRY_FRUIT_SIGN = 6


class GridFruitMapper:
    @staticmethod
    def get_sign(fruit: Fruit) -> int:
        if isinstance(fruit, Apple):
            return APPLE_FRUIT_SIGN
        if isinstance(fruit, Orange):
            return ORANGE_FRUIT_SIGN
        if isinstance(fruit, Strawberry):
            return STRAWBERRY_FRUIT_SIGN
        raise Exception("Fruit type not handled")


class GridHandler:
    def __init__(self, panel_size: Size, grid_size: Size):
        self.snake_head_coordinates = (None, None)
        self.snake_tail_coordinates = (None, None)

        self._grid_size = grid_size
        self._panel_size = panel_size

        self._map = [
            [0 for _ in range(panel_size.width // grid_size.width)]
            for _ in range(panel_size.height // grid_size.height)
        ]

    @property
    def map(self) -> Iterable[Iterable[int]]:
        return self._map

    def _add_object(self, sign: int, x: int, y: int) -> None:
        # todo validation
        self._map[x][y] = sign

    def add_fruit(self, fruit: Fruit, x: int, y: int) -> None:
        sign = GridFruitMapper.get_sign(fruit)
        self._add_object(sign, x, y)

    def add_snake_head(self, x:int, y: int):
        self.snake_head_coordinates = (x, y)
        self._add_object(SNAKE_HEAD, x, y)

    def move_snake(self, x:int, y:int):
        self.clear_cell(*self.snake_head_coordinates)
        self.add_snake_head(x, y)

    def clear_cell(self, x:int, y:int):
        self._add_object(EMPTY_SIGN, x, y)

    def check_snake_collision(self, x: int, y: int):
        if self._map[x][y] == EMPTY_SIGN:
            return "SnakeNoCollision"
        if self._map[x][y] in (SNAKE_HEAD, SNAKE_BODY, SNAKE_TAIL):
            return "SnakeToSnakeCollision"
        if self._map[x][y] in (
            APPLE_FRUIT_SIGN, ORANGE_FRUIT_SIGN, STRAWBERRY_FRUIT_SIGN
        ):
            return "SnakeToFruitCollision"
        if self._map[x][y] == BORDER_SIGN:
            return "SnakeToBorderCollision"
        raise Exception("Unexpected collision behaviour")

    @property
    def free_spots(self) -> Iterable[Tuple[int, int]]:
        return [
            (i, j)
            for i, signs in enumerate(self._map)
            for j, sign in enumerate(signs) if sign == EMPTY_SIGN
        ]

