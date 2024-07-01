from dataclasses import dataclass
from typing import Tuple, Iterable, Optional


@dataclass(frozen=True)
class Color:
    red: int
    green: int
    blue: int

    @property
    def rgb(self) -> Tuple[int, int, int]:
        return self.red, self.green, self.blue


@dataclass(frozen=True)
class Border:
    color: Color
    thickness: int
    enabled: Optional[bool]
    radius: Optional[int]


@dataclass(frozen=True)
class Cell:
    width: int
    height: int


@dataclass(frozen=True)
class Grid:
    border: Border
    cell: Cell


@dataclass(frozen=True)
class Padding:
    x: int
    y: int


@dataclass(frozen=True)
class Point:
    x: int
    y: int


@dataclass(frozen=True)
class Section:
    spacing: int
    padding: Padding
    border: Border
    value: int
    font_size: int
    font_color: Color
    starting_point: Point


@dataclass(frozen=True)
class WindowSettings:
    width: int
    height: int
    title: str


@dataclass(frozen=True)
class MapSettings:
    background_color: Color
    border_color: Color
    left: int
    top: int
    width: int
    height: int
    grid: Grid


@dataclass(frozen=True)
class ScoreboardSettings:
    left: int
    top: int
    width: int
    height: int
    titles: Iterable[str]
    background_color: Color
    section: Section


@dataclass(frozen=True)
class SnakeSettings:
    starting_energy: int


@dataclass(frozen=True)
class FruitSettings:
    pass


@dataclass(frozen=True)
class Settings:
    window: WindowSettings
    map: MapSettings
    scoreboard: ScoreboardSettings
    snake: SnakeSettings
    fruit: FruitSettings
