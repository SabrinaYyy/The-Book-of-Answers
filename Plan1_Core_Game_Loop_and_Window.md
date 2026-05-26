# Plan 1: Core Game Loop and Window

## Goal
Create a runnable Pygame window with a stable game loop and clean quit behavior.

## Steps
1. Create `constants.py`.
2. Define `SCREEN_WIDTH = 800`, `SCREEN_HEIGHT = 600`, `FPS = 60`, and dark background color constants.
3. Create `main.py`.
4. Initialize Pygame and create an 800×600 window.
5. Add `pygame.time.Clock()` and cap the loop at 60 FPS.
6. Handle window close event.
7. Handle ESC key to quit.
8. Fill the screen with a dark background every frame.

## Verification
Run:

```bash
python main.py