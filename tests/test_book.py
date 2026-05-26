import pygame
from book import Book
from constants import BOOK_X, BOOK_Y, BOOK_WIDTH, BOOK_HEIGHT, BOOK_ANIM_DURATION

pygame.init()   # needed for pygame.Rect


def test_rect_position_and_size():
    book = Book()
    assert book.rect.x == BOOK_X
    assert book.rect.y == BOOK_Y
    assert book.rect.width == BOOK_WIDTH
    assert book.rect.height == BOOK_HEIGHT


def test_animation_not_done_before_duration():
    book = Book()
    assert not book.update(BOOK_ANIM_DURATION - 0.01)


def test_animation_done_at_duration():
    book = Book()
    assert book.update(BOOK_ANIM_DURATION)


def test_animation_done_after_overshoot():
    book = Book()
    book.update(BOOK_ANIM_DURATION * 3)
    assert book.update(0)   # stays done


def test_reset_clears_done_flag():
    book = Book()
    book.update(BOOK_ANIM_DURATION + 1)
    book.reset()
    assert not book.update(0)


def test_progress_zero_at_start():
    book = Book()
    assert book.progress == 0.0


def test_progress_one_when_complete():
    book = Book()
    book.update(BOOK_ANIM_DURATION)
    assert book.progress == 1.0


def test_progress_clamped_above_one():
    book = Book()
    book.update(BOOK_ANIM_DURATION * 10)
    assert book.progress == 1.0


def test_progress_partial():
    book = Book()
    half = BOOK_ANIM_DURATION / 2
    book.update(half)
    assert 0.4 < book.progress < 0.6


def test_progress_resets_to_zero():
    book = Book()
    book.update(BOOK_ANIM_DURATION)
    book.reset()
    assert book.progress == 0.0


def test_contains_center():
    book = Book()
    cx = BOOK_X + BOOK_WIDTH // 2
    cy = BOOK_Y + BOOK_HEIGHT // 2
    assert book.contains((cx, cy))


def test_contains_corner():
    book = Book()
    assert book.contains((BOOK_X + 1, BOOK_Y + 1))


def test_not_contains_origin():
    book = Book()
    assert not book.contains((0, 0))


def test_not_contains_outside_right():
    book = Book()
    assert not book.contains((BOOK_X + BOOK_WIDTH + 1, BOOK_Y))
