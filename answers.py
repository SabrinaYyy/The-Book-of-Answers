import random
import states

_NORMAL_PATH = "data/normal.txt"
_SPOOKY_PATH = "data/spooky.txt"

_FALLBACK_NORMAL = [
    "You already know the answer.",
    "Wait a little longer.",
    "Not yet.",
    "Yes, but not in the way you expect.",
    "Let time decide.",
    "The answer is closer than you think.",
    "Do nothing for now.",
]

_FALLBACK_SPOOKY = [
    "Do not ask again tonight.",
    "Someone has already noticed.",
    "You did not ask the right question.",
    "That memory still bothers you.",
    "The book heard you.",
    "Something is behind you.",
    "The eyes are open now.",
]

# Lazily loaded on first pick_outcome() call
_normal = None
_spooky = None


def load_answers(filepath, fallback):
    """Load one answer per line from filepath; warn and return fallback on any failure."""
    try:
        with open(filepath, encoding="utf-8") as f:
            lines = [ln.strip() for ln in f if ln.strip()]
        if lines:
            return lines
    except (FileNotFoundError, OSError):
        pass
    print(f"Warning: could not load {filepath!r}, using built-in fallback.")
    return list(fallback)


def pick_outcome():
    """Return (state, text). text is None for JUMPSCARE."""
    global _normal, _spooky
    if _normal is None:
        _normal = load_answers(_NORMAL_PATH, _FALLBACK_NORMAL)
    if _spooky is None:
        _spooky = load_answers(_SPOOKY_PATH, _FALLBACK_SPOOKY)

    roll = random.random()
    if roll < 0.05:
        return states.JUMPSCARE, None
    if roll < 0.17:
        return states.SPOOKY_ANSWER, random.choice(_spooky)
    return states.NORMAL_ANSWER, random.choice(_normal)
