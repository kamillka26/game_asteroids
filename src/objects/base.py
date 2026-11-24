"""Базовый игровой объект."""

from src import config
from src.utils import wrap_position


class GameObject:
    """Объект с позицией и скоростью. Тороидальное перемещение."""

    def __init__(self, x, y, image):
        """Инициализирует объект в точке (x, y)."""
        self.x = x
        self.y = y
        self.vx = 0.0
        self.vy = 0.0
        self.image = image
        self.angle = 0.0

    def update(self, dt_ms):
        """Обновляет позицию с тороидальной геометрией."""
        self.x += self.vx
        self.y += self.vy
        self.x, self.y = wrap_position(
            self.x, self.y, config.SCREEN_WIDTH, config.SCREEN_HEIGHT
        )

    def radius(self):
        """Радиус описанной окружности для столкновений."""
        return max(self.image.get_width(), self.image.get_height()) / 2

    def get_rotated(self):
        """Возвращает повёрнутое изображение и его прямоугольник."""
        import pygame
        rotated = pygame.transform.rotate(self.image, self.angle - 90)
        rect = rotated.get_rect(center=(self.x, self.y))
        return rotated, rect

    def draw(self, surface):
        """Рисует объект на поверхности."""
        rotated, rect = self.get_rotated()
        surface.blit(rotated, rect)
