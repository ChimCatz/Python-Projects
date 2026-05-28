# AGENTS.md

## Purpose

This repository is a personal Python learning workspace.

The owner writes code primarily for learning and practice, then uses
AI/Codex to help clean up code, explain bugs, improve structure, and get
unstuck without taking over the whole learning process.

## Collaboration Rules

- Prioritize learning value over clever abstractions.
- Preserve the user's original intent and beginner-friendly style unless a
  cleanup is explicitly requested.
- When fixing bugs, explain the cause in simple terms.
- Prefer small, clear refactors over large architectural rewrites.
- Keep naming consistent and descriptive.
- Do not delete learning artifacts unless explicitly asked.

## Udemy Projects Conventions

The `Udemy_Projects/` folder tracks progress through
`100 Days of Code: The Complete Python Pro Bootcamp`.

Expected direction:

- the main executable for each day stays in the root of
  `Udemy_Projects/`
- helper files can be moved into day-specific support folders such as
  `day_7_scripts/`
- filenames should remain easy to scan, for example
  `day_2_tipcalculator.py`

## File Header Convention

For Day project files, prefer a short header comment at the top:

```python
# DAY X - TITLE
# Run: python .\Udemy_Projects\filename.py
# Related: helper files or folders, or "None"
```

## Documentation Goals

When updating docs in this repo:

- reflect the current learning stage honestly
- keep instructions practical and short
- document how to run files from the repo root
- mention related helper files when they matter
