import random
import pygame
from constants import JUMPSCARE_DURATION, SCREEN_WIDTH, SCREEN_HEIGHT

_FLASH_DURATION = 0.15   # white flash before the eyes appear

# Eye geometry — module-level so tests can import and verify without a surface
EYE_W          = 60
EYE_H          = 30
EYE_CX_OFFSET  = 80    # horizontal distance from screen centre to each eye centre
PUPIL_W        = 22
PUPIL_H        = 20
_PUPIL_COLOR   = (180, 30, 30)   # dark blood red


def flicker_bg(base_color, intensity=8):
    """Return a slightly randomised version of base_color for spooky flicker."""
    r, g, b = base_color
    n = random.randint(0, intensity)
    return (min(255, r + n), g, min(255, b + n // 2))


class Fader:
    """Fade-from-black overlay; call start() on state change, update()/draw() each frame."""
    def __init__(self, alpha=220, duration=0.4):
        self._start_alpha = float(alpha)
        self._speed = alpha / duration
        self._alpha = 0.0
        self._surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self._surf.fill((0, 0, 0))

    def start(self):
        self._alpha = self._start_alpha

    def update(self, dt):
        if self._alpha > 0:
            self._alpha = max(0.0, self._alpha - self._speed * dt)

    def draw(self, surface):
        if self._alpha <= 0:
            return
        self._surf.set_alpha(int(self._alpha))
        surface.blit(self._surf, (0, 0))


def eye_rects(w, h):
    """Return (left_rect, right_rect) for a surface of pixel size (w, h)."""
    cy = h // 2
    rects = []
    for sign in (-1, 1):
        cx = w // 2 + sign * EYE_CX_OFFSET
        rects.append(pygame.Rect(cx - EYE_W // 2, cy - EYE_H // 2, EYE_W, EYE_H))
    return tuple(rects)


class JumpScare:
    def __init__(self):
        self._elapsed = 0.0

    def reset(self):
        self._elapsed = 0.0

    def update(self, dt):
        """Advance timer. Returns True when the scare has finished."""
        self._elapsed += dt
        return self._elapsed >= JUMPSCARE_DURATION

    def draw(self, surface):
        w, h = surface.get_size()
        if self._elapsed < _FLASH_DURATION:
            surface.fill((255, 255, 255))
        else:
            surface.fill((0, 0, 0))
            for eye in eye_rects(w, h):
                pygame.draw.ellipse(surface, (255, 255, 255), eye)
                pupil = pygame.Rect(
                    eye.centerx - PUPIL_W // 2,
                    eye.centery - PUPIL_H // 2,
                    PUPIL_W, PUPIL_H,
                )
                pygame.draw.ellipse(surface, _PUPIL_COLOR, pupil)
