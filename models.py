from dataclasses import dataclass


@dataclass(frozen=True)
class Size:
    width: int
    height: int


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
