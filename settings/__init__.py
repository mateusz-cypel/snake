from settings.constants import *
from settings.models import *


settings = Settings(
    window=WindowSettings(
        width=WINDOW_WIDTH,
        height=WINDOW_HEIGHT,
        title=WINDOW_TITLE,
    ),
    map=MapSettings(
        background_color=Color(
            red=MAP_BACKGROUND_COLOR[0],
            green=MAP_BACKGROUND_COLOR[1],
            blue=MAP_BACKGROUND_COLOR[2]
        ),
        border_color=Color(
            red=MAP_BORDER_COLOR[0],
            green=MAP_BORDER_COLOR[1],
            blue=MAP_BORDER_COLOR[2]
        ),
        left=MAP_LEFT,
        top=MAP_TOP,
        width=MAP_WIDTH,
        height=MAP_HEIGHT,
        grid=Grid(
            border=Border(
                color=Color(
                    red=MAP_GRID_BORDER_COLOR[0],
                    green=MAP_GRID_BORDER_COLOR[1],
                    blue=MAP_GRID_BORDER_COLOR[2],
                ),
                thickness=MAP_GRID_BORDER_THICKNESS,
                enabled=MAP_GRID_BORDER_ENABLED,
            ),
            cell=Cell(
                width=MAP_GRID_CELL_WIDTH,
                height=MAP_GRID_CELL_HEIGHT,
            )
        )
    ),
    scoreboard=ScoreboardSettings(
        left=SCOREBOARD_LEFT,
        top=SCOREBOARD_TOP,
    ),
    snake=SnakeSettings(
        starting_energy=SNAKE_STARTING_ENERGY,
    ),
    fruit=FruitSettings(

    )
)