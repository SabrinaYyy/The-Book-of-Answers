
```md
# Plan 3: Book Interaction

## Goal
Display a simple mysterious book and allow the player to open it with ENTER or mouse click.

## Steps
1. Create `book.py`.
2. Define book constants such as position, width, height, and page colors.
3. Add a `Book` class or simple book rendering functions.
4. Draw a closed book in the IDLE state using rectangles.
5. Add a function to detect whether a mouse click is inside the book rectangle.
6. Pressing ENTER in IDLE transitions to OPENING_BOOK.
7. Clicking the book rectangle in IDLE transitions to OPENING_BOOK.
8. Add a brief page-opening animation using elapsed time or frame count.
9. After animation completes, allow transition to outcome selection later.

## Tests
Create:

```text
tests/test_book.py