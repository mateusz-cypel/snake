import random

from handlers.board_handler import BoardHandler
from models import BoardIndex


class FreeSpotProvider:
    def __init__(self, board: BoardHandler):
        self._board = board

    def get(self) -> BoardIndex:
        spots = self._board.free_spots
        return random.choice(spots)
