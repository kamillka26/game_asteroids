"""Точка входа в игру «Астероиды»."""

import os

import pygame

from src import config
from src.game import Game


def load_image(name):
    """Загружает картинку из assets/images с прозрачностью."""
    path = os.path.join("assets", "images", name)
    return pygame.image.load(path).convert_alpha()


def make_star_background():
    """Генерирует звёздный фон, если нет готовой картинки."""
    import random
    surf = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    surf.fill(config.COLOR_BG)
    for _ in range(200):
        x = random.randint(0, config.SCREEN_WIDTH)
        y = random.randint(0, config.SCREEN_HEIGHT)
        r = random.choice([1, 1, 1, 2])
        color = random.choice([(255, 255, 255), (200, 200, 255),
                               (255, 240, 200)])
        pygame.draw.circle(surf, color, (x, y), r)
    return surf


def make_explosion_frames():
    """5 кадров взрыва-заглушки."""
    frames = []
    for i in range(5):
        surf = pygame.Surface((60, 60), pygame.SRCALPHA)
        pygame.draw.circle(surf, (255, 180, 60), (30, 30), 10 + i * 8, 3)
        frames.append(surf)
    return frames


def load_assets():
    """Загружает картинки из assets/images и масштабирует."""
    ship = load_image("playerShip3_green.png")
    ship = pygame.transform.scale(ship, config.SHIP_SPRITE_SIZE)

    flame = load_image("fire03.png")
    flame = pygame.transform.scale(flame, (14, 20))

    asteroid = load_image("meteorBrown_med1.png")
    asteroid = pygame.transform.scale(asteroid, config.ASTEROID_SPRITE_SIZE)

    bg = make_star_background()

    return {
        "ship": ship,
        "flame": flame,
        "asteroid": asteroid,
        "bg_static": bg,
        "bg_dynamic": bg,
        "explosion": make_explosion_frames(),
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
