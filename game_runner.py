import pygame

from game_handler import GameHandler


class GameRunner:
    def __init__(self, game: GameHandler):
        self._game = game

    def run(self):
        clock = pygame.time.Clock()
        is_running = True
        while is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False

            pygame.display.flip()
            clock.tick(60)
        pygame.quit()


def initialize() -> GameRunner:
    pygame.init()
    game = GameHandler()
    return GameRunner(
        game=game
    )