# CLAUDE.md

# Project
2D psychological horror / dialogue game inspired by *The Book of Answers*.
The player silently thinks of a question, opens a mysterious book, and receives:
- a normal answer,
- a disturbing/spooky answer,
- or a rare jump scare event.

The game should feel mysterious, minimalist, unsettling, and psychologically immersive.
See `design_doc.md` for full specification.

---

# Stack
- Python 3
- Pygame 2
- No external game engines
- No online APIs
- No heavy frameworks

---

# Core design philosophy
The game should:
- feel minimal and atmospheric,
- avoid excessive UI,
- create psychological tension through uncertainty,
- rely on timing, sound, darkness, and ambiguity,
- remain simple enough to finish a playable MVP in ~10 hours.

Prioritize:
1. atmosphere,
2. polish,
3. clean game loop,
4. simple implementation.

Do NOT over-engineer systems.

---

# File structure
```
answer_book_game/
├── main.py              # entry point + game loop
├── states.py            # game state management
├── book.py              # book rendering and animations
├── answers.py           # answer loading and random selection
├── effects.py           # jumpscares, flicker, screen effects
├── audio.py             # sound and music manager (stub at MVP — build last)
├── constants.py         # shared constants
├── assets/
│   ├── sounds/
│   ├── images/
│   └── fonts/
├── data/
│   ├── normal.txt
│   └── spooky.txt
└── tests/
```

---


---

# Rules

## Workspace boundary
- Only read, create, edit, or delete files inside this project directory.
- Do not use `cd ..`.
- Do not modify parent folders or other projects.
- If a task seems to require files outside this directory, stop and ask first.

## Code quality
- Never hardcode magic numbers — use constants.
- Keep files under 150 lines when possible.
- Keep functions small and readable.
- Prefer simple procedural logic over unnecessary abstraction.
- Avoid premature optimization.

## Architecture constraints
- Do not introduce ECS architecture.
- Do not introduce dependency injection frameworks.
- Avoid deep inheritance trees.
- Avoid generic engine-like systems.
- Build only what the MVP currently needs.

## Dependency rules
- Do not add new dependencies unless absolutely necessary.
- The game should run with only:
  - Python
  - pygame
  - pytest

## Asset handling
- If any asset file is missing (font, sound, image), fall back to a pygame
  default gracefully — never raise an exception on a missing asset.
- Log a warning to the console if a fallback is used, so it is easy to spot.
- Example safe font load:
  ```python
  try:
      font = pygame.font.Font("assets/fonts/book.ttf", 32)
  except FileNotFoundError:
      font = pygame.font.SysFont("serif", 32)  # fallback

## Font guidance
- Prefer a serif or gothic-style `.ttf` font if one is present in
  `assets/fonts/`. This is critical for atmosphere.
- If no font file exists yet, use `pygame.font.SysFont("serif", size)` as a
  placeholder and add a `# TODO: replace with gothic font` comment so it is
  easy to find later.
- Never use the pygame default pixel font (`pygame.font.Font(None, size)`) —
  it breaks the visual tone entirely.

## Visual style
- Use dark minimalist visuals.
- Use rectangles/placeholders instead of generated art.
- Avoid cluttered UI.
- Keep most scenes visually quiet.

## Audio rules
- `audio.py` is a stub at MVP — build it last, after the full gameplay loop works.
- While audio is unimplemented, all audio calls should fail silently (try/except).
- Audio is important for atmosphere once added.
- Silence is better than constant music.
- Sudden sounds should be used sparingly.

## Horror pacing
- Prioritize timing and pauses over complex animations.
- A simple delay with good atmosphere is better than flashy effects.
- Short moments of silence are valuable.

## Jump scare rules
- Jump scares must remain rare.
- The game should create unease BEFORE fear.
- Psychological tension is more important than loud scares.

## State management
The game flow should remain state-driven:
- START
- IDLE
- OPENING_BOOK
- NORMAL_ANSWER
- SPOOKY_ANSWER
- JUMPSCARE
- RESTART

Only one outcome state may occur after opening the book.

## State rules
- Game state must be controlled from a single source of truth.
- Avoid duplicated boolean flags like:
  - is_jumpscare
  - is_spooky
  - is_opening
- Prefer one explicit current_state variable.

## Testing
- Every major system should be testable independently.
- Add lightweight pytest tests when appropriate.
- Run tests before marking tasks complete.

---

# Gameplay constraints
- The player NEVER types their question.
- The game only asks the player to think silently.
- The illusion that the game "knows" the player's thoughts is important.

---

# Performance constraints
- Keep the game lightweight.
- Avoid large assets.
- Avoid unnecessary particle systems.
- Maintain stable FPS on low-end hardware.

---

# Art direction
Visual inspiration:
- dark room,
- old book,
- candlelight,
- liminal horror,
- analog horror,
- subtle supernatural elements.

Avoid:
- cartoon UI,
- bright colors,
- excessive animations,
- meme horror.

---

# How to run
```
python main.py
```

---

# MVP priority order
1. Window and game loop
2. State system
3. Book interaction
4. Random answer selection
5. Answer display
6. Spooky answer system
7. Jump scare system
8. Restart loop
9. Audio polish
10. Visual polish

---

# Definition of done
The MVP is complete when:
- the full gameplay loop works,
- spooky outcomes occur correctly,
- at least one jump scare exists,
- the atmosphere feels intentionally unsettling,
- the game runs reliably without crashes,
- no missing asset causes a crash — all fallbacks are in place.
