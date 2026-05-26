
```md
# Plan 4: Random Answer Selection

## Goal
Load normal and spooky answers from text files and randomly select an outcome.

## Steps
1. Create `answers.py`.
2. Create `data/normal.txt`.
3. Create `data/spooky.txt`.
4. Load answers from files safely.
5. If a file is missing or empty, use fallback answer lists.
6. Implement outcome probabilities:
   - 83% normal answer
   - 12% spooky answer
   - 5% jump scare
7. Return exactly one outcome after book opening.

## Tests
Create:

```text
tests/test_answers.py