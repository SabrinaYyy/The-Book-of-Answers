import pygame
from effects import JumpScare, eye_rects, EYE_W, EYE_H, EYE_CX_OFFSET, Fader, flicker_bg
from constants import JUMPSCARE_DURATION, SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()


# --- timing ---

def test_not_done_before_duration():
    js = JumpScare()
    assert not js.update(JUMPSCARE_DURATION - 0.01)


def test_done_at_duration():
    js = JumpScare()
    assert js.update(JUMPSCARE_DURATION)


def test_done_after_overshoot():
    js = JumpScare()
    js.update(JUMPSCARE_DURATION * 3)
    assert js.update(0)


def test_reset_restarts_timer():
    js = JumpScare()
    js.update(JUMPSCARE_DURATION + 1)
    js.reset()
    assert not js.update(0)


def test_duration_is_approximately_two_seconds():
    assert 1.9 <= JUMPSCARE_DURATION <= 2.1


# --- eye geometry ---

def test_eyes_symmetric_horizontally():
    left, right = eye_rects(SCREEN_WIDTH, SCREEN_HEIGHT)
    cx = SCREEN_WIDTH // 2
    assert cx - left.centerx == right.centerx - cx


def test_left_eye_is_left_of_centre():
    left, _ = eye_rects(SCREEN_WIDTH, SCREEN_HEIGHT)
    assert left.centerx < SCREEN_WIDTH // 2


def test_right_eye_is_right_of_centre():
    _, right = eye_rects(SCREEN_WIDTH, SCREEN_HEIGHT)
    assert right.centerx > SCREEN_WIDTH // 2


def test_eyes_same_vertical_position():
    left, right = eye_rects(SCREEN_WIDTH, SCREEN_HEIGHT)
    assert left.y == right.y


def test_eyes_vertically_centred():
    left, right = eye_rects(SCREEN_WIDTH, SCREEN_HEIGHT)
    assert left.centery == right.centery == SCREEN_HEIGHT // 2


def test_eyes_correct_size():
    left, right = eye_rects(SCREEN_WIDTH, SCREEN_HEIGHT)
    for rect in (left, right):
        assert rect.width == EYE_W
        assert rect.height == EYE_H


def test_eye_offset_matches_constant():
    left, right = eye_rects(SCREEN_WIDTH, SCREEN_HEIGHT)
    cx = SCREEN_WIDTH // 2
    assert cx - left.centerx == EYE_CX_OFFSET
    assert right.centerx - cx == EYE_CX_OFFSET


# --- Fader ---

def test_fader_starts_inactive():
    assert Fader()._alpha == 0.0


def test_fader_start_sets_alpha():
    fader = Fader(alpha=200)
    fader.start()
    assert fader._alpha == 200.0


def test_fader_update_reduces_alpha():
    fader = Fader(alpha=200, duration=0.4)
    fader.start()
    fader.update(0.1)
    assert fader._alpha < 200.0


def test_fader_reaches_zero_at_duration():
    fader = Fader(alpha=200, duration=0.4)
    fader.start()
    fader.update(0.4)
    assert fader._alpha == 0.0


def test_fader_does_not_go_negative():
    fader = Fader(alpha=200, duration=0.4)
    fader.start()
    fader.update(999)
    assert fader._alpha == 0.0


# --- flicker_bg ---

def test_flicker_bg_red_channel_within_range():
    base = (14, 6, 8)
    for _ in range(30):
        r, g, b = flicker_bg(base, intensity=8)
        assert base[0] <= r <= base[0] + 8


def test_flicker_bg_green_unchanged():
    base = (14, 6, 8)
    for _ in range(10):
        assert flicker_bg(base)[1] == base[1]


def test_flicker_bg_no_channel_overflow():
    for _ in range(20):
        result = flicker_bg((252, 250, 253), intensity=10)
        assert all(0 <= c <= 255 for c in result)
