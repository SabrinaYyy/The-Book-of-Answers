
```md
# Plan 5: Answer Display

## Goal
Display the selected answer clearly on the open book page.

## Steps
1. Render open book pages in NORMAL_ANSWER and SPOOKY_ANSWER states.
2. Display normal answers in a calm style.
3. Display spooky answers with subtle visual differences.
4. Use serif font fallback, not pygame default pixel font.
5. Add text wrapping so long answers fit inside the book page.
6. Pressing R or clicking after an answer transitions to RESTART.

## Tests
Create:

```text
tests/test_text_rendering.py