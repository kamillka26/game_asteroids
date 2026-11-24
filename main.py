"""Точка входа в игру «Астероиды»."""

import pygame

from src import config


def main():
    """Инициализирует pygame и открывает окно."""
    pygame.init()
    screen = pygame.display.set_mode(
        (config.SCREEN_WIDTH, config.SCREEN_HEIGHT)
    )
    pygame.display.set_caption("Asteroids")

    running = True
    clock = pygame.time.Clock()
    while running:
        clock.tick(config.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(config.COLOR_BG)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
