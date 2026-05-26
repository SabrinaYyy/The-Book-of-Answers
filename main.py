import sys
import pygame
import states
import answers
from book import Book
from constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT, FPS,
    COLOR_BG, COLOR_TEXT, COLOR_HINT, COLOR_SPOOKY_TEXT, COLOR_PAGE_TEXT,
    FONT_PATH, FONT_SIZE_BODY, FONT_SIZE_HINT,
    BOOK_Y, BOOK_HEIGHT,
)

# ENTER key transitions for states without dedicated interaction logic
_ENTER_TRANSITIONS = {
    states.START:          states.IDLE,
    states.NORMAL_ANSWER:  states.RESTART,
    states.SPOOKY_ANSWER:  states.RESTART,
    states.JUMPSCARE:      states.RESTART,
    states.RESTART:        states.IDLE,
}


def _load_font(size):
    try:
        return pygame.font.Font(FONT_PATH, size)
    except (FileNotFoundError, OSError):
        print(f"Warning: font not found at {FONT_PATH!r}, using serif fallback.")
        return pygame.font.SysFont("serif", size)  # TODO: replace with gothic font


def _center_text(surface, text, font, color, y):
    surf = font.render(text, True, color)
    surface.blit(surf, ((SCREEN_WIDTH - surf.get_width()) // 2, y))


def _transition(current, next_state):
    if states.is_valid(current, next_state):
        print(f"State: {current} → {next_state}")
        return next_state
    return current


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("The Book of Answers")
    clock = pygame.time.Clock()
    font = _load_font(FONT_SIZE_BODY)
    font_hint = _load_font(FONT_SIZE_HINT)

    book = Book()
    current_state = states.START
    answer_text = None
    print(f"State: {current_state}")

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_RETURN:
                    if current_state == states.IDLE:
                        book.reset()
                        answer_text = None
                        current_state = _transition(current_state, states.OPENING_BOOK)
                    else:
                        next_s = _ENTER_TRANSITIONS.get(current_state)
                        if next_s:
                            current_state = _transition(current_state, next_s)
                elif event.key == pygame.K_r:
                    if current_state in (states.NORMAL_ANSWER, states.SPOOKY_ANSWER):
                        current_state = _transition(current_state, states.RESTART)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if current_state == states.IDLE and book.contains(event.pos):
                    book.reset()
                    answer_text = None
                    current_state = _transition(current_state, states.OPENING_BOOK)
                elif current_state in (states.NORMAL_ANSWER, states.SPOOKY_ANSWER):
                    current_state = _transition(current_state, states.RESTART)
                elif current_state == states.RESTART:
                    current_state = _transition(current_state, states.IDLE)

        # Time-driven transition: animation complete → pick real outcome
        if current_state == states.OPENING_BOOK and book.update(dt):
            outcome, answer_text = answers.pick_outcome()
            current_state = _transition(current_state, outcome)

        # Draw
        screen.fill(COLOR_BG)

        if current_state == states.START:
            _center_text(screen, "Think of a question in your head.",
                         font, COLOR_TEXT, SCREEN_HEIGHT // 2 - 30)
            _center_text(screen, "Press ENTER when you are ready.",
                         font_hint, COLOR_HINT, SCREEN_HEIGHT // 2 + 10)
        elif current_state in (states.IDLE, states.OPENING_BOOK):
            book.draw(screen, current_state)
            if current_state == states.IDLE:
                _center_text(screen, "Press ENTER or click the book.",
                             font_hint, COLOR_HINT, BOOK_Y + BOOK_HEIGHT + 24)
        elif current_state == states.NORMAL_ANSWER:
            book.draw_answer(screen, answer_text, font, COLOR_PAGE_TEXT)
            _center_text(screen, "Press ENTER or R to ask again.",
                         font_hint, COLOR_HINT, BOOK_Y + BOOK_HEIGHT + 24)
        elif current_state == states.SPOOKY_ANSWER:
            book.draw_answer(screen, answer_text, font, COLOR_SPOOKY_TEXT)
            _center_text(screen, "Press ENTER or R to ask again.",
                         font_hint, COLOR_HINT, BOOK_Y + BOOK_HEIGHT + 24)
        elif current_state == states.RESTART:
            _center_text(screen, "Ask another question?",
                         font, COLOR_TEXT, SCREEN_HEIGHT // 2 - 20)
            _center_text(screen, "Press ENTER to continue  \xb7  ESC to quit",
                         font_hint, COLOR_HINT, SCREEN_HEIGHT // 2 + 20)
        elif current_state == states.JUMPSCARE:
            # Plan 6 will replace this with the real jump scare effect
            _center_text(screen, "…", font, COLOR_SPOOKY_TEXT,
                         (SCREEN_HEIGHT - font.get_linesize()) // 2)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
