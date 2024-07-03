import pygame

from handlers.joystick_input_handler import JoystickInputHandlerSubjectWrapper, JoystickInputHandler
from handlers.score_handler import ScoreHandler
from handlers.snake_energy_handler import SnakeEnergyHandler
from handlers.snake_movement_handler import SnakeMovementHandler
from providers.free_spot_provider import FreeSpotProvider
from providers.fruit_provider import FruitProvider
from graphics.objects.fruit import Orange as OrangeObject, Apple as AppleObject, Strawberry as StrawberryObject
from graphics.objects.snake import SnakeHead, SnakeBody
from graphics.views.map import Map
from graphics.views.scoreboard import Scoreboard
from handlers.board_handler import BoardHandler, CollisionStatus
from models import Size, Orange as OrangeModel, Apple as AppleModel, Strawberry as StrawberryModel, Snake, BoardIndex
from settings import settings
from snake_movement_observer import SnakeMoveObserver

fruit_map = {
    AppleModel: AppleObject,
    OrangeModel: OrangeObject,
    StrawberryModel: StrawberryObject,
}


class GameHandler:
    def __init__(self):
        # init window
        self.display_surface = pygame.display.set_mode(
            size=(settings.window.width, settings.window.height)
        )
        pygame.display.set_caption(settings.window.title)

        # init map and scoreboard
        self.map = Map()
        self.scoreboard = Scoreboard()
        self.refresh()

        # init snake model
        self.snake = Snake(
            energy=settings.snake.starting_energy,
            direction="RIGHT",  # todo starting direction depends on pressed button
        )

        # init handlers
        self.board_handler = BoardHandler(
            board_size=Size(
                width=settings.map.width,
                height=settings.map.height
            ),
            cell_size=Size(
                width=settings.map.grid.cell.width,
                height=settings.map.grid.cell.height
            ),
        )
        self.fruit_provider = FruitProvider()
        self.spot_provider = FreeSpotProvider(
            board=self.board_handler
        )
        self.snake_movement_handler = SnakeMovementHandler()
        self.snake_energy_handler = SnakeEnergyHandler(snake=self.snake)
        self.score_handler = ScoreHandler()

        # init snake and first fruit position on the board
        self.board_handler.add_snake_head(
            index=self.spot_provider.get()
        )
        self.board_handler.add_fruit(
            index=self.spot_provider.get(),
            fruit=self.fruit_provider.get()
        )

        # init keyboard controller
        snake_move_observer = SnakeMoveObserver(
            snake=self.snake
        )
        self.joystick_input_handler_subject_wrapper = JoystickInputHandlerSubjectWrapper(
            joystick_input_handler=JoystickInputHandler()
        )
        self.joystick_input_handler_subject_wrapper.attach(
            observer=snake_move_observer
        )

    # todo may require some refactor because of using next index for handling snake
    def handle(self):
        self.map.clear()
        self.joystick_input_handler_subject_wrapper.read()

        self.snake_energy_handler.move()
        self.scoreboard.update_energy(self.snake.energy)

        move = self.snake_movement_handler.next_move(
            direction=self.snake.direction
        )
        next_index = self.board_handler.snake_head_index + move
        collision = self.board_handler.check_collision(next_index)

        self.draw_fruit(self.board_handler.current_fruit_index)
        self.draw_snake(index=self.board_handler.snake_head_index)

        if collision in (
            CollisionStatus.BORDER_COLLISION,
            CollisionStatus.SNAKE_COLLISION
        ):
            self.snake_energy_handler.hit_border()
            self.scoreboard.update_energy(self.snake.energy)
            next_index = self.spot_provider.get()
            self.board_handler.move_snake_to(next_index)
        elif collision == CollisionStatus.FRUIT_COLLISION:
            # todo when no free spots then raises IndexError
            #  potential win condition
            self.board_handler.add_snake_body(self.board_handler.snake_head_index)
            self.board_handler.add_snake_head(next_index)
            self.snake_energy_handler.eat_fruit(self.board_handler.current_fruit)
            self.score_handler.handle(self.board_handler.current_fruit)
            self.scoreboard.update_energy(self.snake.energy)
            self.scoreboard.update_score(self.score_handler.score)
            self.scoreboard.update_hi_score(self.score_handler.hi_score)
            spot = self.spot_provider.get()
            self.board_handler.add_fruit(index=spot, fruit=self.fruit_provider.get())
        else:
            self.board_handler.move_snake_to(next_index)
        if not self.snake_energy_handler.is_alive():
            self.snake_energy_handler.reset()
            self.score_handler.reset()
            self.scoreboard.update_energy(self.snake.energy)
            self.scoreboard.update_score(self.score_handler.score)
            self.scoreboard.update_hi_score(self.score_handler.hi_score)

        self.map.draw_grid()
        self.refresh()

    def draw_fruit(self, index: BoardIndex):
        fruit_cell = self.map.get_cell(index)
        fruit_obj_class = fruit_map[type(self.board_handler.current_fruit)]
        fruit_obj_class(
            fruit_cell.left,
            fruit_cell.top,
            fruit_cell.width,
            fruit_cell.height
        ).draw_on(self.map)

    def draw_snake(self, index: BoardIndex):
        snake_head_cell = self.map.get_cell(index)
        SnakeHead(
            snake_head_cell.left,
            snake_head_cell.top,
            snake_head_cell.width,
            snake_head_cell.height
        ).draw_on(self.map)

        for snake_body_part_index in self.board_handler.body_parts:
            snake_body_part_cell = self.map.get_cell(snake_body_part_index)
            SnakeBody(
                snake_body_part_cell.left,
                snake_body_part_cell.top,
                snake_body_part_cell.width,
                snake_body_part_cell.height,
            ).draw_on(self.map)

    def refresh(self):
        self.display_surface.blit(
            source=self.map,
            dest=(settings.map.left, settings.map.top),
        )
        self.display_surface.blit(
            source=self.scoreboard,
            dest=(settings.scoreboard.left, settings.scoreboard.top),
        )
