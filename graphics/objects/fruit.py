from graphics.objects.object import Object
from settings import settings


class Fruit(Object):
    color = None


class Apple(Fruit):
    color = settings.fruit.apple.color


class Orange(Fruit):
    color = settings.fruit.orange.color


class Strawberry(Fruit):
    color = settings.fruit.strawberry.color
