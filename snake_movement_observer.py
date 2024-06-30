from handlers.joystick_input_handler import JoystickAction
from handlers.snake_movement_handler import SnakeMoveDirection
from models import Snake
from pattern.observer import Observer, Subject


class SnakeMoveObserver(Observer):
    JOYSTICK_ACTION_TO_SNAKE_DIRECTION: dict = {
        JoystickAction.UP: SnakeMoveDirection.UP,
        JoystickAction.DOWN: SnakeMoveDirection.DOWN,
        JoystickAction.LEFT: SnakeMoveDirection.LEFT,
        JoystickAction.RIGHT: SnakeMoveDirection.RIGHT,
    }

    SNAKE_DIRECTION_OPPOSITES: dict = {
        SnakeMoveDirection.UP: SnakeMoveDirection.DOWN,
        SnakeMoveDirection.DOWN: SnakeMoveDirection.UP,
        SnakeMoveDirection.LEFT: SnakeMoveDirection.RIGHT,
        SnakeMoveDirection.RIGHT: SnakeMoveDirection.LEFT,
    }

    def __init__(self, snake: Snake):
        super(SnakeMoveObserver, self).__init__()
        if not snake:
            raise ValueError(f"Snake object is required")
        self.snake = snake

    def update(self, subject: Subject) -> None:
        action: JoystickAction = subject.current_joystick_action
        if action not in self.JOYSTICK_ACTION_TO_SNAKE_DIRECTION:
            return

        direction: SnakeMoveDirection = self.JOYSTICK_ACTION_TO_SNAKE_DIRECTION[action]
        if direction != self.SNAKE_DIRECTION_OPPOSITES[self.snake.direction]:
            self.snake.direction = direction
