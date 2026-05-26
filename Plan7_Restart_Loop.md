
```md
# Plan 7: Restart Loop

## Goal
Allow the player to ask again without restarting the program.

## Steps
1. Add RESTART state rendering.
2. Show text such as “Ask another question?”
3. Press ENTER or click to return to IDLE.
4. Press ESC to quit.
5. Clear previous answer before replay.
6. Reset temporary animation and effect timers before replay.

## Tests
Create:

```text
tests/test_restart.py