"""Вспомогательные математические функции."""

import math


def wrap_position(x, y, w, h):
    """Тороидальное сворачивание координат."""
    return x % w, y % h


def angle_to_vector(angle_deg):
    """Угол в градусах → единичный вектор (0 — вправо, 90 — вверх)."""
    rad = math.radians(angle_deg)
    return math.cos(rad), -math.sin(rad)


def wrap_delta(dx, dy, w, h):
    """Кратчайшая дистанция между объектами с учётом тора."""
    if dx > w / 2:
        dx -= w
    elif dx < -w / 2:
        dx += w
    if dy > h / 2:
        dy -= h
    elif dy < -h / 2:
        dy += h
    return dx, dy
