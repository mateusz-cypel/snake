from models import Snake, Fruit


class SnakeEnergyHandler:
    def __init__(self, snake: Snake):
        self.snake = snake
        self._energy = self._max_energy = 100 * 10
        self.snake.energy = self._energy // 10

    def move(self) -> None:
        self._energy -= 1
        self._energy = min(self._energy, self._max_energy)
        self.snake.energy = self._energy // 10

    def hit_border(self) -> None:
        self._energy -= 20 * 10
        self._energy = min(self._energy, self._max_energy)
        self.snake.energy = self._energy // 10

    def eat_fruit(self, fruit: Fruit) -> None:
        self._energy += fruit.energy * 10
        self._energy = min(self._energy, self._max_energy)
        self.snake.energy = self._energy // 10

    def is_alive(self) -> bool:
        return self.snake.energy > 0

    def reset(self) -> None:
        self._energy = self._max_energy
        self.snake.energy = self._energy // 10
