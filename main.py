"""Точка входа в игру «Астероиды»."""

import pygame

from src import config
from src.objects.ship import Ship


def make_placeholder_image(size, color):
    """Создаёт однотонную заглушку вместо картинки."""
    surf = pygame.Surface(size, pygame.SRCALPHA)
    surf.fill(color)
    return surf


def main():
    """Инициализирует pygame и рисует корабль в центре."""
    pygame.init()
    screen = pygame.display.set_mode((config.SCREEN_WIDTH,
                                      config.SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    ship_img = make_placeholder_image((40, 50), config.COLOR_SHIP)
    ship_thrust_img = make_placeholder_image((40, 50), (255, 160, 60))
    ship = Ship(ship_img, ship_thrust_img)

    running = True
    clock = pygame.time.Clock()
    while running:
        clock.tick(config.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(config.COLOR_BG)
        ship.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
