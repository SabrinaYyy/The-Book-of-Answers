import sys
import os
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import answers

@pytest.fixture(autouse=True)
def reset_answers_state():
    answers._first_pick = False
    yield
