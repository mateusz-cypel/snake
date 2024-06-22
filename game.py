import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Hungry Python")

    def run(self):
        is_running = True
        while is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False

            pygame.display.flip()
        pygame.quit()


def initialize() -> Game:
    pygame.init()
    return Game()
