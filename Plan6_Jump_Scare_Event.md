
```md
# Plan 6: Jump Scare Event

## Goal
Implement one rare jump scare event that is brief, simple, and atmospheric.

## Steps
1. Create `effects.py`.
2. Add a jump scare timer or duration constant.
3. Draw a black screen.
4. Draw two white ellipses using `pygame.draw.ellipse`, positioned symmetrically on the black screen to look like eyes.
5. Add a brief screen flash or flicker.
6. Keep the jump scare visible for around 2 seconds.
7. After the timer ends, transition to RESTART.
8. Ensure no missing sound file can crash the game.

## Tests
Create:

```text
tests/test_effects.py