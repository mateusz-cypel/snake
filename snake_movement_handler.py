from typing import Tuple

from models import Snake


class SnakeMovementHandler:
    def next_move(self, snake: Snake, x: int, y: int) -> Tuple[int, int]:
        if snake.direction == "UP":
            return x, y + 1
        if snake.direction == "DOWN":
            return x, y - 1
        if snake.direction == "RIGHT":
            return x + 1, y
        if snake.direction == "LEFT":
            return x - 1, y
        raise Exception("Unknown direction")
