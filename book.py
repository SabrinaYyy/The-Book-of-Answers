import pygame
import states
from constants import (
    BOOK_X, BOOK_Y, BOOK_WIDTH, BOOK_HEIGHT,
    BOOK_ANIM_DURATION,
    COLOR_BOOK_COVER, COLOR_BOOK_SPINE, COLOR_BOOK_PAGE,
)

_SPINE_W = 4
_PAGE_SHADOW = (170, 155, 120)   # slightly darker page for depth


class Book:
    def __init__(self):
        self.rect = pygame.Rect(BOOK_X, BOOK_Y, BOOK_WIDTH, BOOK_HEIGHT)
        self._elapsed = 0.0
        self._done = False

    def reset(self):
        self._elapsed = 0.0
        self._done = False

    def update(self, dt):
        """Advance opening animation. Returns True when complete."""
        if self._done:
            return True
        self._elapsed += dt
        if self._elapsed >= BOOK_ANIM_DURATION:
            self._done = True
        return self._done

    @property
    def progress(self):
        return min(1.0, self._elapsed / BOOK_ANIM_DURATION)

    def contains(self, pos):
        return self.rect.collidepoint(pos)

    def draw(self, surface, current_state):
        if current_state == states.IDLE:
            _draw_cover(surface, self.rect)
        elif current_state == states.OPENING_BOOK:
            _draw_opening(surface, self.rect, self.progress)


# ---------------------------------------------------------------------------

def _draw_cover(surface, rect):
    pygame.draw.rect(surface, COLOR_BOOK_COVER, rect, border_radius=3)
    spine = pygame.Rect(rect.centerx - _SPINE_W // 2, rect.top, _SPINE_W, rect.height)
    pygame.draw.rect(surface, COLOR_BOOK_SPINE, spine)
    pygame.draw.rect(surface, (50, 35, 20), rect, width=1, border_radius=3)


def _draw_opening(surface, rect, progress):
    """Pages fan out from the right half of the spine as progress goes 0→1."""
    page_max_w = rect.width // 2 - 6
    for i in range(3):
        frac = max(0.0, min(1.0, (progress - i * 0.18) * 1.6))
        w = int(page_max_w * frac)
        if w > 0:
            margin = 6 + i * 3
            page = pygame.Rect(
                rect.centerx + 2,
                rect.top + margin,
                w,
                rect.height - margin * 2,
            )
            color = COLOR_BOOK_PAGE if i == 0 else _PAGE_SHADOW
            pygame.draw.rect(surface, color, page, border_radius=1)
    _draw_cover(surface, rect)
