# Python dice roller — CLI coding exercise

A small command-line program for rolling tabletop-style dice using familiar notation such as `d6`, `2d20`, or `3d8+5`.

## Run it

Requires Python 3; no external Python packages are used.

```bash
git clone https://github.com/Imabyrd/dice_roller.git
cd dice_roller
python main.py
```

Enter a roll expression at the prompt, or `q` to quit.

## Examples

```text
d6
2d20
3d8+5
1d20-2
```

The program parses the number of dice, number of sides, and optional modifier, generates rolls using Python's `random` module, and prints the individual results and total.

## Code layout

- `main.py` — interactive input loop and friendly error message for malformed notation.
- `dice_roller.py` — regular-expression parser and dice-rolling logic.

## Learning goals

Working with functions, loops, modular Python, regular expressions, string formatting, input validation, and random-number generation.

## Known issues / improvements

- The parser accepts zero dice and zero-sided dice; these should be rejected before rolling.
- The display formatting for a roll of one and the modifier summary need correction.
- Bracketed maximum rolls are a visual convention here, not a complete rules engine for critical hits.
- Add deterministic automated tests by injecting or mocking randomness.
- Remove generated `__pycache__` files from version control and ignore them going forward.

## Status

Learning project: usable for basic notation, with the validation and formatting limitations above.
