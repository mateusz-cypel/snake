import random
from typing import Tuple

from grid_handler import GridHandler


class FreeSpotProvider:
    def __init__(self, grid: GridHandler):
        self._grid = grid

    def get(self) -> Tuple[int, int]:
        spots = self._grid.free_spots
        return random.choice(spots)
