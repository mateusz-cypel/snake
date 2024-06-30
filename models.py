from dataclasses import dataclass


@dataclass(frozen=True)
class Size:
    width: int
    height: int


@dataclass(frozen=True)
class XYField:
    """
    x: horizonal

    y: vertical
    """
    x: int
    y: int


@dataclass(frozen=True)
class Move(XYField):
    pass


@dataclass(frozen=True)
class BoardIndex(XYField):
    def __add__(self, other):
        if not isinstance(other, Move):
            raise Exception
        return BoardIndex(self.x + other.x, self.y + other.y)


@dataclass(frozen=True)
class Cell:
    top: int
    left: int
    width: int
    height: int


@dataclass(frozen=True)
class MapIndex(XYField):
    pass


@dataclass(frozen=True)
class Fruit:
    score: int
    energy: int


@dataclass(frozen=True)
class Apple(Fruit):
    pass


@dataclass(frozen=True)
class Orange(Fruit):
    pass


@dataclass(frozen=True)
class Strawberry(Fruit):
    pass


@dataclass
class Snake:
    direction: str
    energy: int
