import states


ALL_STATES = [
    states.START, states.IDLE, states.OPENING_BOOK,
    states.NORMAL_ANSWER, states.SPOOKY_ANSWER, states.JUMPSCARE, states.RESTART,
]


def test_all_states_are_strings():
    for s in ALL_STATES:
        assert isinstance(s, str) and s


def test_no_duplicate_state_values():
    assert len(set(ALL_STATES)) == len(ALL_STATES)


# --- valid transitions ---

def test_start_to_idle():
    assert states.is_valid(states.START, states.IDLE)

def test_idle_to_opening_book():
    assert states.is_valid(states.IDLE, states.OPENING_BOOK)

def test_opening_book_to_normal_answer():
    assert states.is_valid(states.OPENING_BOOK, states.NORMAL_ANSWER)

def test_opening_book_to_spooky_answer():
    assert states.is_valid(states.OPENING_BOOK, states.SPOOKY_ANSWER)

def test_opening_book_to_jumpscare():
    assert states.is_valid(states.OPENING_BOOK, states.JUMPSCARE)

def test_normal_answer_to_restart():
    assert states.is_valid(states.NORMAL_ANSWER, states.RESTART)

def test_spooky_answer_to_restart():
    assert states.is_valid(states.SPOOKY_ANSWER, states.RESTART)

def test_jumpscare_to_restart():
    assert states.is_valid(states.JUMPSCARE, states.RESTART)

def test_restart_to_idle():
    assert states.is_valid(states.RESTART, states.IDLE)


# --- invalid transitions ---

def test_start_cannot_skip_to_opening_book():
    assert not states.is_valid(states.START, states.OPENING_BOOK)

def test_idle_cannot_jump_to_normal_answer():
    assert not states.is_valid(states.IDLE, states.NORMAL_ANSWER)

def test_normal_answer_cannot_go_back_to_idle():
    assert not states.is_valid(states.NORMAL_ANSWER, states.IDLE)

def test_restart_cannot_go_to_jumpscare():
    assert not states.is_valid(states.RESTART, states.JUMPSCARE)

def test_unknown_state_returns_false():
    assert not states.is_valid("MADE_UP", states.IDLE)
    assert not states.is_valid(states.IDLE, "MADE_UP")
