from models import Move


# todo change to some class
class SnakeMoveDirection:
    UP = "UP"
    DOWN = "DOWN"
    RIGHT = "RIGHT"
    LEFT = "LEFT"


class SnakeMovementHandler:
    def next_move(self, direction: str) -> Move:
        if direction == SnakeMoveDirection.UP:
            return Move(x=0, y=-1)
        if direction == SnakeMoveDirection.DOWN:
            return Move(x=0, y=1)
        if direction == SnakeMoveDirection.RIGHT:
            return Move(x=1, y=0)
        if direction == SnakeMoveDirection.LEFT:
            return Move(x=-1, y=0)
        raise Exception("Unknown direction")
