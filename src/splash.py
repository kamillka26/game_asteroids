"""Заставка игры."""

import pygame

from src import config


class SplashScreen:
    """Прямоугольник в центре. Клик только внутри запускает игру."""

    def __init__(self, font_big, font_small):
        """Создаёт прямоугольник заставки."""
        self.font_big = font_big
        self.font_small = font_small
        w, h = 360, 160
        self.rect = pygame.Rect(
            (config.SCREEN_WIDTH - w) // 2,
            (config.SCREEN_HEIGHT - h) // 2, w, h
        )

    def is_click_inside(self, pos):
        """Клик попал в заставку."""
        return self.rect.collidepoint(pos)

    def draw(self, surface):
        """Рисует заставку."""
        s = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        s.fill((0, 0, 0, 160))
        surface.blit(s, self.rect.topleft)
        pygame.draw.rect(surface, config.COLOR_TEXT, self.rect, 2)
        t1 = self.font_big.render("АСТЕРОИДЫ", True, config.COLOR_TEXT)
        t2 = self.font_small.render("Кликните для старта", True,
                                    config.COLOR_TEXT)
        surface.blit(t1, t1.get_rect(center=(self.rect.centerx,
                                             self.rect.centery - 20)))
        surface.blit(t2, t2.get_rect(center=(self.rect.centerx,
                                             self.rect.centery + 30)))
