import pygame

from graphics.views.window import Window


class Game:
    def __init__(self):
        self.window = Window()

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


def initialize() -> Game:
    pygame.init()
    return Game()
