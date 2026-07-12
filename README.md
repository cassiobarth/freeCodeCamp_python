# freeCodeCamp — Python Certification

Code from the workshops and labs of the [freeCodeCamp](https://www.freecodecamp.org/) **Scientific Computing with Python** certification.

A collection of small Python exercises exploring core language features — list comprehensions, `filter`, string manipulation — plus a Tkinter GUI that turns one of the labs into an interactive app.

## Contents

| File | Description |
| --- | --- |
| [`loops.py`](loops.py) | List comprehensions and `filter()` exercises — even numbers, mapping values, conditional expressions, and filtering lists. |
| [`pin_extractor.py`](pin_extractor.py) | "Secret code" lab: reads a set of poems and builds a PIN from the word lengths at each line. |
| [`pin_extractor_gui.py`](pin_extractor_gui.py) | A Tkinter desktop app wrapping the PIN extractor — type your own poem and extract its PIN interactively. |

## Requirements

- Python 3.10+
- No third-party dependencies — everything uses the standard library (`tkinter` ships with most Python installs).

## Getting started

```bash
# clone
git clone https://github.com/cassiobarth/freeCodeCamp_python.git
cd freeCodeCamp_python

# (optional) create and activate a virtual environment
python -m venv .venv
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate
```

## Running the scripts

```bash
python loops.py
python pin_extractor.py
python pin_extractor_gui.py   # opens the GUI window
```

## The PIN extractor

Given a list of poems, the extractor builds a numeric code, one digit per line:

- For line *i* (0-indexed), take the word at index *i* on that line and use its **length** as the digit.
- If that line doesn't have a word at index *i*, the digit is `0`.

```
Stars and the moon         -> "Stars" (index 0)     -> 5
shine in the sky           -> "in"    (index 1)     -> 2
white and                  -> (no word at index 2)  -> 0
until the end of the night -> "of"    (index 3)     -> 2
                                                 PIN = 5202
```

The GUI ([`pin_extractor_gui.py`](pin_extractor_gui.py)) shows this original example and lets you paste your own poem to generate a PIN on the fly.

## License

Educational project — free to use and adapt.
