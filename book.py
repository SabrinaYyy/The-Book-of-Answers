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

    def draw_answer(self, surface, text, font, text_color):
        _draw_open(surface, self.rect, text, font, text_color)


# ---------------------------------------------------------------------------

def wrap_text(text, font, max_width):
    """Split text into lines that each fit within max_width pixels."""
    if not text:
        return []
    words = text.split()
    lines = []
    current = []
    for word in words:
        candidate = " ".join(current + [word])
        if font.size(candidate)[0] <= max_width:
            current.append(word)
        else:
            if current:
                lines.append(" ".join(current))
            current = [word]
    if current:
        lines.append(" ".join(current))
    return lines


def _render_page_text(surface, text, font, color, page_rect):
    padding = 8
    usable_w = page_rect.width - padding * 2
    lines = wrap_text(text, font, usable_w)
    line_h = font.get_linesize()
    total_h = line_h * len(lines)
    y = page_rect.centery - total_h // 2
    for line in lines:
        surf = font.render(line, True, color)
        x = page_rect.centerx - surf.get_width() // 2
        surface.blit(surf, (x, y))
        y += line_h


def _draw_open(surface, rect, text, font, text_color):
    """Draw both pages of the open book; render text on the right page."""
    left_page = pygame.Rect(rect.left, rect.top + 6, rect.width // 2 - 2, rect.height - 12)
    right_page = pygame.Rect(rect.centerx + 2, rect.top + 6, rect.width // 2 - 4, rect.height - 12)
    pygame.draw.rect(surface, _PAGE_SHADOW, left_page, border_radius=1)
    pygame.draw.rect(surface, COLOR_BOOK_PAGE, right_page, border_radius=1)
    spine = pygame.Rect(rect.centerx - _SPINE_W // 2, rect.top, _SPINE_W, rect.height)
    pygame.draw.rect(surface, COLOR_BOOK_SPINE, spine)
    if text:
        _render_page_text(surface, text, font, text_color, right_page)


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
