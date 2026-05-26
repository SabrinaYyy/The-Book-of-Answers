import states
import answers
from book import Book
from effects import JumpScare
from constants import BOOK_ANIM_DURATION, JUMPSCARE_DURATION

import pygame
pygame.init()


# --- state transitions ---

def test_all_outcomes_can_reach_restart():
    for outcome in (states.NORMAL_ANSWER, states.SPOOKY_ANSWER, states.JUMPSCARE):
        assert states.is_valid(outcome, states.RESTART), f"{outcome} cannot reach RESTART"


def test_restart_can_return_to_idle():
    assert states.is_valid(states.RESTART, states.IDLE)


def test_full_cycle_state_path():
    path = [
        (states.IDLE,          states.OPENING_BOOK),
        (states.OPENING_BOOK,  states.NORMAL_ANSWER),
        (states.NORMAL_ANSWER, states.RESTART),
        (states.RESTART,       states.IDLE),
    ]
    for src, dst in path:
        assert states.is_valid(src, dst), f"{src} -> {dst} invalid"


def test_five_consecutive_cycles_all_valid():
    cycle = [
        (states.IDLE,          states.OPENING_BOOK),
        (states.OPENING_BOOK,  states.NORMAL_ANSWER),
        (states.NORMAL_ANSWER, states.RESTART),
        (states.RESTART,       states.IDLE),
    ]
    for _ in range(5):
        for src, dst in cycle:
            assert states.is_valid(src, dst)


# --- book reset ---

def test_book_is_done_after_full_animation():
    book = Book()
    book.update(BOOK_ANIM_DURATION)
    assert book._done


def test_book_reset_clears_done_and_progress():
    book = Book()
    book.update(BOOK_ANIM_DURATION)
    book.reset()
    assert not book._done
    assert book.progress == 0.0


def test_book_animates_correctly_on_second_cycle():
    book = Book()
    book.update(BOOK_ANIM_DURATION)   # first cycle
    book.reset()
    assert not book.update(BOOK_ANIM_DURATION - 0.01)
    assert book.update(0.02)           # second cycle completes


# --- jumpscare timer reset ---

def test_jumpscare_timer_reusable_after_reset():
    js = JumpScare()
    assert js.update(JUMPSCARE_DURATION)   # first trigger
    js.reset()
    assert not js.update(JUMPSCARE_DURATION - 0.01)
    assert js.update(0.02)                 # second trigger


# --- answer selection across cycles ---

def test_pick_outcome_valid_across_ten_calls():
    valid = {states.NORMAL_ANSWER, states.SPOOKY_ANSWER, states.JUMPSCARE}
    for _ in range(10):
        outcome, text = answers.pick_outcome()
        assert outcome in valid


def test_jumpscare_outcome_has_no_text():
    import random
    original = random.random
    random.random = lambda: 0.01
    try:
        outcome, text = answers.pick_outcome()
        assert outcome == states.JUMPSCARE
        assert text is None
    finally:
        random.random = original


def test_answer_text_is_nonempty_for_non_jumpscare():
    import random
    original = random.random
    random.random = lambda: 0.5
    try:
        outcome, text = answers.pick_outcome()
        assert outcome == states.NORMAL_ANSWER
        assert text and len(text) > 0
    finally:
        random.random = original
