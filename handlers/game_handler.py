import pygame

from handlers.snake_movement_handler import SnakeMovementHandler
from providers.free_spot_provider import FreeSpotProvider
from providers.fruit_provider import FruitProvider
from graphics.objects.fruit import Orange as OrangeObject, Apple as AppleObject, Strawberry as StrawberryObject
from graphics.objects.snake import SnakeHead
from graphics.views.map import Map
from graphics.views.scoreboard import Scoreboard
from handlers.board_handler import BoardHandler, CollisionStatus
from models import Size, Orange as OrangeModel, Apple as AppleModel, Strawberry as StrawberryModel, Snake, BoardIndex

WINDOW_SIZE = (800, 600)
WINDOW_TITLE = "Hungry Python"

# map width: scoreboard width is in 3:1 ratio
MAP_GRID_BORDER_COLOR = (0, 0, 0)
MAP_GRID_BORDER_THICKNESS = 1
MAP_GRID_CELL_SIZE = (60, 60)
MAP_SIZE = (600, 600)
MAP_LEFT_TOP = (0, 0)
MAP_BACKGROUND_COLOR = (76, 18, 18)

SCOREBOARD_LEFT_TOP = (600, 0)  #

config = {
    "window": {
        "title": WINDOW_TITLE,
        "size": WINDOW_SIZE,
        "map": {
            "background_color": MAP_BACKGROUND_COLOR,
            "left_top": MAP_LEFT_TOP,
            "size": MAP_SIZE,
            "grid": {
                "cell": {
                    "size": MAP_GRID_CELL_SIZE
                },
                "border": {
                    "enabled": True,
                    "thickness": MAP_GRID_BORDER_THICKNESS,
                    "color": MAP_GRID_BORDER_COLOR
                }
            }
        },
        "scoreboard": {
            "left_top": SCOREBOARD_LEFT_TOP
        }
    }
}
fruit_map = {
    AppleModel: AppleObject,
    OrangeModel: OrangeObject,
    StrawberryModel: StrawberryObject,
}


class GameHandler:
    def __init__(self):
        # init window
        self.display_surface = pygame.display.set_mode(config["window"]["size"])
        pygame.display.set_caption(config["window"]["title"])

        # init map and scoreboard
        self.map = Map(config=config["window"]["map"])
        self.scoreboard = Scoreboard(config=config["window"]["scoreboard"])
        self.refresh()

        self.board_handler = BoardHandler(
            board_size=Size(*config["window"]["map"]["size"]),
            cell_size=Size(*config["window"]["map"]["grid"]["cell"]["size"]),
        )
        self.fruit_provider = FruitProvider()
        self.spot_provider = FreeSpotProvider(
            board=self.board_handler
        )

        snake_starting_point = self.spot_provider.get()
        snake_starting_point = BoardIndex(x=1, y=1)
        self.board_handler.add_snake_head(snake_starting_point)
        fruit_starting_point = BoardIndex(y=1, x=7)
        self.board_handler.add_fruit(index=fruit_starting_point, fruit=self.fruit_provider.get())

    def handle(self):
        # todo in progress
        move = (
            SnakeMovementHandler()
            .next_move(
                Snake(energy=20, direction="RIGHT"),
            )
        )
        next_index = self.board_handler.snake_head_index + move
        collision = self.board_handler.check_collision(next_index)

        print(f'{self.board_handler.snake_head_index=}')
        print(f'--')
        print(f'{self.board_handler.current_fruit_index=}')
        print(f'--')
        self.map.clear()

        fruit_obj_class = fruit_map[type(self.board_handler.current_fruit)]
        fruit_cell = self.map.get_cell(self.board_handler.current_fruit_index)
        fruit_obj_class(
            fruit_cell.left,
            fruit_cell.top,
            fruit_cell.width,
            fruit_cell.height
        ).draw_on(self.map)

        snake_head_cell = self.map.get_cell(next_index)
        SnakeHead(
            snake_head_cell.left,
            snake_head_cell.top,
            snake_head_cell.width,
            snake_head_cell.height
        ).draw_on(self.map)

        if collision in (
            CollisionStatus.BORDER_COLLISION,
            CollisionStatus.SNAKE_COLLISION
        ):
            print("You lose")
            next_index = BoardIndex(1,1)
        elif collision == CollisionStatus.FRUIT_COLLISION:
            spot = self.spot_provider.get()
            self.board_handler.add_fruit(index=spot, fruit=self.fruit_provider.get())
            print("Collision")

        print(f'{collision=}')

        self.board_handler.move_snake_to(next_index)

        self.map.draw_grid()
        self.refresh()


        # try:
        #
        #     fruit = self.fruit_provider.get()
        #     spot = self.spot_provider.get()
        #     self.board_handler.add_fruit(fruit, *spot)
        #
        #     fruit_obj_class = fruit_map[type(fruit)]
        #
        #     i_x, i_y = spot
        #     left, top = self.map.left_top_points[i_x][i_y]
        #
        #     fruit_obj = fruit_obj_class(left, top, *MAP_GRID_CELL_SIZE)
        #
        #     for i in self.board_handler.board:
        #         print(i)
        #     print('-----------------------')
        #     fruit_obj.draw(self.map)
        #     self.map.draw_grid()
        #     self.display_surface.blit(self.map, (0, 0))
        # except IndexError:
        #     pass
        #
        # SnakeHead(*self.map.left_top_points[0][0], 60, 60).draw(self.map)
        # SnakeBody(*self.map.left_top_points[0][1], 60, 60).draw(self.map)
        # self.display_surface.blit(self.map, (0, 0))
        #
        # x, y = SnakeMovementHandler().next_move(Snake(energy=20, direction="RIGHT"), 0, 0)
        # print(x,y)
        # SnakeHead(*self.map.left_top_points[x][y], 60, 60).draw(self.map)
        # self.display_surface.blit(self.map, (0, 0))

    def refresh(self):
        self.display_surface.blit(self.map, self.map.left_top)
        self.display_surface.blit(self.scoreboard, self.scoreboard.left_top)