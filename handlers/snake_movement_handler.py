from typing import Tuple

from models import Snake, Move


class SnakeMovementHandler:
    def next_move(self, snake: Snake) -> Move:
        if snake.direction == "UP":
            return Move(x=0, y=1)
        if snake.direction == "DOWN":
            return Move(x=0, y=-1)
        if snake.direction == "RIGHT":
            return Move(x=1, y=0)
        if snake.direction == "LEFT":
            return Move(x=-1, y=0)
        raise Exception("Unknown direction")
