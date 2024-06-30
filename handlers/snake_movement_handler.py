from models import Snake, Move


class SnakeMoveDirection:
    UP = "UP"
    DOWN = "DOWN"
    RIGHT = "RIGHT"
    LEFT = "LEFT"


class SnakeMovementHandler:
    def next_move(self, snake: Snake) -> Move:
        if snake.direction == SnakeMoveDirection.UP:
            return Move(x=0, y=-1)
        if snake.direction == SnakeMoveDirection.DOWN:
            return Move(x=0, y=1)
        if snake.direction == SnakeMoveDirection.RIGHT:
            return Move(x=1, y=0)
        if snake.direction == SnakeMoveDirection.LEFT:
            return Move(x=-1, y=0)
        raise Exception("Unknown direction")
