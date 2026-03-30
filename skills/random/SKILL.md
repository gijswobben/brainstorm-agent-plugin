---
name: random
description: "Use this skill to generate random values, such as integers or words, for various purposes."
user-invocable: true
---

# Randomness

The Randomness skill provides tools for generating random values, which can be useful in a variety of contexts, such as brainstorming sessions, simulations, or any situation where you need to introduce an element of chance.

## Available scripts

- [scripts/random_integer.py](scripts/random_integer.py) — Generates random integers
- [scripts/random_word.py](scripts/random_word.py) — Generates random words like nouns, verbs, adjectives, or characters

## Usage

To use the Randomness skill, simply call the desired script with the appropriate parameters. For example, to generate a random integer between 1 and 100, you can run:

```bash
uv run scripts/random_integer.py --min 1 --max 100
```

To generate a random word, you can run:

```bash
uv run scripts/random_word.py --type noun --n-words 5
```

These commands are examples, the scripts can be found in the `scripts` directory of this skill.
