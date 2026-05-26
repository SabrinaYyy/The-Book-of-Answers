import pygame
from book import wrap_text

pygame.init()
_font = pygame.font.SysFont("serif", 20)


def test_empty_text_returns_empty_list():
    assert wrap_text("", _font, 200) == []


def test_single_word_returns_one_line():
    lines = wrap_text("Hello", _font, 300)
    assert lines == ["Hello"]


def test_short_sentence_fits_one_line():
    lines = wrap_text("Yes.", _font, 400)
    assert len(lines) == 1


def test_long_text_splits_into_multiple_lines():
    text = "You did not ask the right question and the book has noticed."
    lines = wrap_text(text, _font, 80)
    assert len(lines) > 1


def test_each_line_fits_within_max_width():
    text = "The answer is closer than you think and always has been."
    max_w = 100
    lines = wrap_text(text, _font, max_w)
    for line in lines:
        assert _font.size(line)[0] <= max_w


def test_all_words_preserved_wide_wrap():
    text = "one two three four five six seven"
    lines = wrap_text(text, _font, 400)
    assert " ".join(lines) == text


def test_all_words_preserved_narrow_wrap():
    text = "one two three four five"
    lines = wrap_text(text, _font, 50)
    assert " ".join(lines) == text


def test_no_empty_lines_produced():
    text = "Something is behind you."
    lines = wrap_text(text, _font, 120)
    assert all(line != "" for line in lines)
