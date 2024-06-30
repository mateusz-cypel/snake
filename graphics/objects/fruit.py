from graphics.objects.object import Object


class Fruit(Object):
    color = None


class Apple(Fruit):
    color = (9, 154, 38)


class Orange(Fruit):
    color = (223, 111, 25)


class Strawberry(Fruit):
    color = (176, 18, 18)
