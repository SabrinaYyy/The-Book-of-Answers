# The Book of Answers

> *Clear your mind. Think of a question. Open the book.*

A minimalist 2D psychological horror game inspired by *The Book of Answers*. The player silently thinks of a question, opens a mysterious old book, and receives one of three outcomes: a normal answer, a disturbing answer, or a rare jump scare.

Built with Python 3 and Pygame 2. No external game engine. No heavy frameworks.

---

## Features

- Atmospheric dark visuals with flickering backgrounds and fade transitions
- Three outcome types: normal answers, spooky answers, and rare jump scares
- TV-static noise overlay on spooky answers
- Background piano music with horror ambient audio on jump scares
- Disclaimer screen on launch with content warnings
- First answer always normal — the game eases you in
- Full pytest test suite covering all major systems

---

## Requirements

- Python 3.9 or later
- Pygame 2

Install Pygame if you do not have it:

```bash
pip install pygame
```

---

## Running the Game

### macOS / Linux

```bash
cd ~/"The Book of Answers"
python main.py
```

### Windows (Command Prompt)

```cmd
cd "%USERPROFILE%\The Book of Answers"
python main.py
```

### Windows (PowerShell)

```powershell
cd "$HOME\The Book of Answers"
python main.py
```

> **Note:** On some systems `python` may be aliased as `python3`. If `python main.py` does not work, try `python3 main.py`.

---

### Running Tests

#### macOS / Linux

```bash
python -m pytest tests/
```

#### Windows

```cmd
python -m pytest tests/
```

---

## How to Play

| Action | Control |
|---|---|
| Advance / acknowledge | `ENTER` or mouse click |
| Open the book | `ENTER` or click the book |
| Turn the page / restart | `ENTER`, `R`, or mouse click |
| Quit | `ESC` |

1. A **disclaimer** screen appears on launch — press `ENTER` to continue.
2. You reach the **Start** screen. Clear your mind and think of a question.
3. Press `ENTER` to enter the **IDLE** state and see the closed book.
4. Click the book or press `ENTER` to open it. Watch the animation.
5. Receive your answer — normal, spooky, or something worse.
6. Press `ENTER` to reach the **Restart** screen. Ask again if you dare.

---

## Optional: Gothic Font

The game ships with a serif fallback font. For the intended atmosphere, drop any gothic-style `.ttf` file (e.g. *IM Fell English* or *Cinzel* from Google Fonts) into:

```
assets/fonts/book.ttf
```

No code changes needed — the game loads it automatically.

---

## Project Structure

```
The Book of Answers/
├── main.py              # Entry point and game loop
├── states.py            # State machine constants and transition validation
├── book.py              # Book rendering and opening animation
├── answers.py           # Answer loading and weighted random outcome selection
├── effects.py           # Jump scare, fader, static noise overlay, flicker
├── audio.py             # Music and sound manager
├── constants.py         # All shared constants (colors, sizes, durations)
├── assets/
│   ├── fonts/           # Drop book.ttf here for gothic font
│   └── sounds/          # BGM and jump scare audio files
├── data/
│   ├── normal.txt       # Normal answer pool (one per line)
│   └── spooky.txt       # Spooky answer pool (one per line)
└── tests/               # pytest test suite
```

---

## Content Warnings

This game contains flashing visuals, sudden loud sounds, psychological horror themes, and unsettling imagery. Players with epilepsy, heart conditions, or sensitivity to flashing lights are advised to play with caution.

---

## Built with Claude Code — Step by Step

This project was developed incrementally using [Claude Code](https://claude.ai/code), Anthropic's AI coding assistant. Each feature was planned in a separate markdown document and then implemented by Claude Code following the spec. Below is the full build history.

### Plan 1 — Core Game Loop and Window
`Design_Doc.md`,`Plan1_Core_Game_Loop_and_Window.md`

Set up a Pygame window running at a stable 60 FPS with a clean game loop and quit behavior. Established the project scaffold: `main.py`, `constants.py`, and the overall file structure defined in `CLAUDE.md`.

### Plan 2 — Game State System
`Plan2_Game_State_System.md`

Implemented a state machine with seven distinct states (`DISCLAIMER`, `START`, `IDLE`, `OPENING_BOOK`, `NORMAL_ANSWER`, `SPOOKY_ANSWER`, `JUMPSCARE`, `RESTART`) and a validation table that only allows legal transitions. All state logic lives in `states.py` as a single source of truth — no scattered boolean flags.

### Plan 3 — Book Interaction
`Plan3_Book_Interaction.md`

Created the book visual in the `IDLE` state with a click and keyboard handler to start the opening animation. The book renders as a closed cover, animates pages fanning out as it opens, then lands on the open two-page spread. All drawing logic is contained in `book.py`.

### Plan 4 — Random Answer Selection
`Plan4_Random_Answer_Selection.md`

Loaded normal and spooky answer pools from `data/normal.txt` and `data/spooky.txt`, with built-in fallback lists if files are missing. `pick_outcome()` uses weighted probability (normal / spooky / jump scare) and always returns a normal answer on the very first open to ease the player in.

### Plan 5 — Answer Display
`Plan5_Answer_Display.md`

Rendered the selected answer on the right page of the open book using a serif font with graceful fallback. Added `wrap_text()` to break long answers into lines that fit within the page boundary. Normal and spooky answers use different text colors to signal their tone.

### Plan 6 — Jump Scare Event
`Plan6_Jump_Scare_Event.md`

Implemented the rare jump scare: a white flash followed by a black screen with two staring eyes (white ellipses with dark red pupils). The scare lasts two seconds then automatically transitions to `RESTART`. Eye geometry is defined at module level so it can be verified in tests without a display surface.

### Plan 7 — Restart Loop
`Plan7_Restart_Loop.md`

Added the `RESTART` state so the player can ask another question without restarting the program. Pressing `ENTER` or clicking clears the previous answer and book state and returns to `IDLE`. The full cycle (`IDLE → OPENING_BOOK → outcome → RESTART → IDLE`) was verified across multiple consecutive iterations.

### Polish Pass
*Implemented in conversation with Claude Code after Plan 7.*

- **Screen fade** between every state transition (`Fader` class in `effects.py`, black overlay that decays over 0.4 s)
- **Spooky background flicker** — `flicker_bg()` slightly randomises the red-tinted background every frame during `SPOOKY_ANSWER`
- **TV-static overlay** — `StaticOverlay` draws 4 500 random noise pixels per frame on top of the spooky answer screen, visible on both the dark background and the light book pages
- **Better book colors** — cover, spine, page, shadow, and edge each have a named constant in `constants.py`
- **Atmospheric instruction text** — copy tuned for psychological tension at each state

### Audio
*Implemented in conversation with Claude Code.*

`audio.py` manages all sound with full silent-fail protection — a missing file or unavailable mixer never crashes the game. Background piano music (`pianotheme04_mp3_loop.mp3`) loops throughout. On a jump scare, the BGM stops and the horror ambient (`ambient_horror.ogg`) plays via an independent `pygame.mixer.Sound` channel so the BGM can resume cleanly on `RESTART`.

### Disclaimer Screen
*Implemented in conversation with Claude Code.*

A `DISCLAIMER` state was added before `START`. It renders the full content-warning text using `wrap_text()` for automatic line breaking and a near-white color (`COLOR_DISCLAIMER_TEXT`) for readability against the dark background. The screen appears once per session; the restart loop bypasses it.

---

## CLAUDE.md

The project includes a `CLAUDE.md` file that defines coding rules, architecture constraints, and the MVP priority order for Claude Code. It enforces:

- No magic numbers — every value is a named constant
- Files kept under 150 lines where possible
- No ECS, dependency injection, or deep inheritance
- Only Python, Pygame, and pytest as dependencies
- Silent fallback for every missing asset
- State driven by a single `current_state` variable

---

---

## Credits

### Music
**Simple Horror Piano Music Pack** by [Wfded](https://opengameart.org/content/simple-horror-piano-music-pack)
Licensed under [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
Source: OpenGameArt.org

### Sound Effects
**Ambient Horror** by [techiew](https://opengameart.org/content/ambient-horror)
Licensed under [CC0 1.0 Public Domain](https://creativecommons.org/publicdomain/zero/1.0/).
Source: OpenGameArt.org

### Font
**MedievalSharp** by [JoanaDias](https://fonts.google.com/specimen/MedievalSharp)
Licensed under the [SIL Open Font License 1.1](https://openfontlicense.org/).
Source: Google Fonts

---

*Player discretion is advised.*
