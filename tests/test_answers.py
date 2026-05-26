import random
import states
from answers import load_answers, pick_outcome


# --- load_answers ---

def test_missing_file_uses_fallback():
    result = load_answers("data/does_not_exist_xyz.txt", ["fallback"])
    assert result == ["fallback"]


def test_fallback_is_a_copy():
    fallback = ["a", "b"]
    result = load_answers("data/does_not_exist_xyz.txt", fallback)
    assert result is not fallback


def test_loads_lines_from_file(tmp_path):
    f = tmp_path / "answers.txt"
    f.write_text("First answer\nSecond answer\n")
    result = load_answers(str(f), ["fallback"])
    assert result == ["First answer", "Second answer"]


def test_skips_blank_lines(tmp_path):
    f = tmp_path / "answers.txt"
    f.write_text("First\n\nSecond\n   \nThird\n")
    result = load_answers(str(f), ["fallback"])
    assert result == ["First", "Second", "Third"]


def test_empty_file_uses_fallback(tmp_path):
    f = tmp_path / "empty.txt"
    f.write_text("")
    result = load_answers(str(f), ["fallback"])
    assert result == ["fallback"]


def test_whitespace_only_file_uses_fallback(tmp_path):
    f = tmp_path / "ws.txt"
    f.write_text("   \n\n  \n")
    result = load_answers(str(f), ["fallback"])
    assert result == ["fallback"]


# --- pick_outcome probabilities ---

def test_jumpscare_on_low_roll(monkeypatch):
    monkeypatch.setattr(random, "random", lambda: 0.01)
    state, text = pick_outcome()
    assert state == states.JUMPSCARE
    assert text is None


def test_spooky_on_mid_roll(monkeypatch):
    monkeypatch.setattr(random, "random", lambda: 0.10)
    state, text = pick_outcome()
    assert state == states.SPOOKY_ANSWER
    assert isinstance(text, str) and text


def test_normal_on_high_roll(monkeypatch):
    monkeypatch.setattr(random, "random", lambda: 0.50)
    state, text = pick_outcome()
    assert state == states.NORMAL_ANSWER
    assert isinstance(text, str) and text


def test_boundary_0_05_is_not_jumpscare(monkeypatch):
    monkeypatch.setattr(random, "random", lambda: 0.05)
    state, _ = pick_outcome()
    assert state != states.JUMPSCARE


def test_boundary_0_17_is_normal(monkeypatch):
    monkeypatch.setattr(random, "random", lambda: 0.17)
    state, _ = pick_outcome()
    assert state == states.NORMAL_ANSWER


def test_all_outcomes_are_valid_states():
    for _ in range(60):
        state, _ = pick_outcome()
        assert state in (states.NORMAL_ANSWER, states.SPOOKY_ANSWER, states.JUMPSCARE)


def test_non_jumpscare_text_is_nonempty():
    for _ in range(60):
        state, text = pick_outcome()
        if state != states.JUMPSCARE:
            assert isinstance(text, str) and len(text) > 0
