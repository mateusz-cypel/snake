from typing import Iterable, Tuple

from models import Size, Fruit, Apple, Orange, Strawberry

EMPTY_SIGN = 0
APPLE_FRUIT_SIGN = 1
ORANGE_FRUIT_SIGN = 2
STRAWBERRY_FRUIT = 3


class GridFruitMapper:
    @staticmethod
    def get_sign(fruit: Fruit) -> int:
        if isinstance(fruit, Apple):
            return APPLE_FRUIT_SIGN
        if isinstance(fruit, Orange):
            return ORANGE_FRUIT_SIGN
        if isinstance(fruit, Strawberry):
            return STRAWBERRY_FRUIT
        raise Exception("Fruit type not handled")


class GridHandler:
    def __init__(self, panel_size: Size, grid_size: Size):
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
        self._map[x][y] = sign

    def add_fruit(self, fruit: Fruit, x: int, y: int) -> None:
        sign = GridFruitMapper.get_sign(fruit)
        self._add_object(sign, x, y)

    @property
    def free_spots(self) -> Iterable[Tuple[int, int]]:
        return [
            (i, j)
            for i, signs in enumerate(self._map)
            for j, sign in enumerate(signs) if sign == EMPTY_SIGN
        ]

