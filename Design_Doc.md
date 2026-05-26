# The Book of Answers — Design Doc

## Concept
A short 2D interactive dialogue game inspired by *The Book of Answers*.

The player silently thinks of a question in their head, then opens a mysterious book. The book flips to a random page and shows a vague, poetic, or philosophical answer.

The game has a calm, mysterious atmosphere, but sometimes the book behaves strangely. Rarely, a jump scare appears, such as a pair of eyes suddenly staring at the player.

## Core mechanic
Player interacts with a mysterious answer book.

Main interaction loop:
1. Player silently thinks of a question in their head.
2. Player presses ENTER or clicks the book.
3. The book flips pages with a short animation.
4. The game randomly chooses one outcome:
   - normal answer
   - spooky answer
   - jump scare
5. Player can restart and ask again.

The game creates the illusion that the book somehow “knows” the player’s thoughts.

## Gameplay
The player does not type anything.

Instead:
- The game asks the player to silently think of a question
- The player opens the book when ready
- The book reveals a random answer or strange event
- The player can restart and repeat the ritual

The game is not skill-based. It is a short atmospheric experience focused on curiosity, suspense, and surprise.

## Random answers
The book will choose one answer from a list of pre-written responses.

Example normal answers:
- “You already know the answer.”
- “Wait a little longer.”
- “Not yet.”
- “Yes, but not in the way you expect.”
- “Let time decide.”
- “The answer is closer than you think.”
- “Do nothing for now.”

Example spooky answers:
- “Do not ask again tonight.”
- “Someone has already noticed.”
- “You did not ask the right question.”
- “That memory still bothers you.”
- “The book heard you.”
- “Something is behind you.”
- “The eyes are open now.”

## Jump scare / Easter egg mechanic
There is a random chance that opening the book triggers a spooky event.

Suggested probability:
- Normal answer: 83%
- Spooky answer: 12%
- Full jump scare: 5%

Possible jump scares:
- A pair of eyes appears in the darkness
- The screen flickers
- The answer text changes to “I heard you.”
- The book closes by itself
- A loud or sudden sound plays
- The screen briefly turns black, then shows eyes

The jump scare should be uncommon enough to feel unexpected, but common enough that players feel uneasy after repeated plays.

## Demo done when
- Player can open the game window
- Start screen works
- Player is instructed to silently think of a question
- Player can press ENTER or click the book
- Book opening / page flipping interaction works
- Random outcome is selected
- Normal answer screen works
- Spooky answer screen works
- At least one jump scare event is implemented
- Restart / ask again works
- Game can run from Python without crashing

## 10-hour MVP scope
Must-have:
- Static dark background
- Simple book visual
- Start screen
- Silent question instruction
- Book opening interaction
- Random answer system
- Normal answer outcome
- Spooky answer outcome
- One jump scare visual
- Restart loop

Nice-to-have:
- Background music
- Page turning sound
- Multiple spooky events
- Fade in / fade out transitions
- Better book art
- Animated eyes
- Save previous answers
- Screen shake effect

## Tech stack
Python 3  
Pygame 2

## Art style
Dark, mysterious, simple 2D style.

Visual direction:
- Dark background
- Old book in the center
- Warm yellow page color
- White or pale text
- Red / black jump scare effect
- Minimal UI
- Eyes hidden in the darkness

## Controls
- ENTER: open the book / continue
- Mouse click: open the book / restart
- R: restart after answer
- ESC: quit game

## Game states
The game flow is divided into distinct states.

1. Start screen
   - Intro text
   - “Think of a question in your head.”
   - Press ENTER to begin

2. Idle / waiting state
   - Book is closed
   - Player is silently thinking
   - ENTER or mouse click opens the book

3. Book opening animation
   - Page flip animation
   - Sound effects
   - Random outcome is selected

4. Normal answer state
   - A standard answer appears
   - Calm atmosphere
   - Player can press R or click to ask again

5. Spooky answer state
   - A disturbing or unusual answer appears
   - May include flickering text, red tint, distorted sound, or unsettling message
   - Player can restart afterward

6. Jump scare state
   - Sudden visual/audio scare event
   - Example: eyes appear, loud sound, screen flash
   - Brief duration before transitioning to restart screen

7. Restart / replay state
   - “Ask another question?”
   - Player can restart the loop or quit the game

After the book opening animation, only one outcome state should happen:
- normal answer state
- spooky answer state
- jump scare state

## Outcome logic
The outcome is selected after the book opening animation.

Example logic:

```python
random_value = random.random()

if random_value < 0.05:
    state = JUMPSCARE
elif random_value < 0.17:
    state = SPOOKY_ANSWER
else:
    state = NORMAL_ANSWER