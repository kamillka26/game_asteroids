"""Точка входа в игру «Астероиды»."""

import pygame

from src import config
from src.game import Game


def make_placeholder_image(size, color):
    """Однотонная заглушка вместо картинки."""
    surf = pygame.Surface(size, pygame.SRCALPHA)
    surf.fill(color)
    return surf


def load_assets():
    """Загружает картинки (пока заглушки)."""
    ship = make_placeholder_image((40, 50), config.COLOR_SHIP)
    ship_thrust = make_placeholder_image((40, 50), (255, 160, 60))
    asteroid = make_placeholder_image((80, 80), config.COLOR_ASTEROID)
    bg_static = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    bg_static.fill(config.COLOR_BG)
    bg_dynamic = make_placeholder_image(
        (config.SCREEN_WIDTH, config.SCREEN_HEIGHT), (60, 60, 120)
    )
    explosion = [make_placeholder_image((60, 60), (255, 200 - i * 40, 0))
                 for i in range(5)]
    return {
        "ship": ship, "ship_thrust": ship_thrust, "asteroid": asteroid,
        "bg_static": bg_static, "bg_dynamic": bg_dynamic,
        "explosion": explosion,
    }


def main():
    """Инициализирует pygame и запускает игру."""
    pygame.init()
    screen = pygame.display.set_mode((config.SCREEN_WIDTH,
                                      config.SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    Game(screen, load_assets()).run()
    pygame.quit()


if __name__ == "__main__":
    main()
