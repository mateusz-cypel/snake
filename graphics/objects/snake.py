from graphics.objects.object import Object
from settings import settings


class SnakeBody(Object):
    color = settings.snake.body_color


class SnakeHead(Object):
    color = settings.snake.head_color
