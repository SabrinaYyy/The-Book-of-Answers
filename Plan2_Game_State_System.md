
# Plan 2: Game State System

## Goal
Implement a simple state-driven game flow using one explicit `current_state` variable.

## Steps
1. Create `states.py`.
2. Define game states:
   - START
   - IDLE
   - OPENING_BOOK
   - NORMAL_ANSWER
   - SPOOKY_ANSWER
   - JUMPSCARE
   - RESTART
3. Add a helper function for valid state transitions.
4. In `main.py`, store one `current_state`.
5. Render placeholder text showing the current state name.
6. Print the current state name to the terminal whenever it changes.
7. Add temporary ENTER transitions:
   - START → IDLE
   - IDLE → OPENING_BOOK
   - OPENING_BOOK → NORMAL_ANSWER
   - NORMAL_ANSWER → RESTART
   - RESTART → IDLE
8. Avoid duplicated boolean flags like `is_opening`, `is_spooky`, or `is_jumpscare`.

## Tests
Create:

```text
tests/test_states.py