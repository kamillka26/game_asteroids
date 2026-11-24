"""Статичный и динамический фон."""

import pygame

from src import config


class Background:
    """Фон: статика + прокручиваемый полупрозрачный слой."""

    def __init__(self, static_img, dynamic_img):
        """Сохраняет изображения и обнуляет смещение."""
        self.static = static_img
        self.dynamic = dynamic_img
        self.dynamic.set_alpha(config.BG_ALPHA)
        self.offset_x = 0.0

    def update(self, dt_ms):
        """Прокручивает динамический слой влево."""
        self.offset_x = (self.offset_x 
                         - config.BG_SCROLL_SPEED) % config.SCREEN_WIDTH

    def draw(self, surface):
        """Рисует статичный и динамический слои."""
        surface.blit(self.static, (0, 0))
        surface.blit(self.dynamic, (self.offset_x - config.SCREEN_WIDTH, 0))
        surface.blit(self.dynamic, (self.offset_x, 0))
