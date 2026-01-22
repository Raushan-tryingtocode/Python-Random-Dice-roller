# Python-Random-Dice-roller


A lightweight, terminal-based Python tool that simulates rolling multiple dice and displays them horizontally using high-quality ASCII art. This project focuses on clean logic, user input validation, and nested loop structures.

## Features

- **Side-by-Side Display:** Unlike standard scripts that print dice one under another, this tool uses nested loops to render dice faces horizontally.
- **Persistent Sessions:** Roll as many times as you like without restarting the program.
- **Input Validation:** Built-in checks to ensure the user enters a valid number of dice (integers > 0).
- **Dynamic Scoring:** Automatically calculates and displays the sum of all dice rolled in the current round.

## Technical Topics Covered

This project was built to practice core Python concepts required for open-source contributions (like Zulip):
- **Dictionary Mapping:** Using a dictionary to store and retrieve complex ASCII tuple data.
- **Nested Iteration:** Managing `for` loops to synchronize line-by-line printing across multiple list items.
- **Control Flow:** Implementing `while` loops with `continue` and `break` for a smooth user experience.
- **Variable Scoping:** Ensuring list and integer resets occur correctly within the loop cycle.

##  How to Run

1. Make sure you have **Python 3** installed.
2. Clone this repository:
   ```bash
   git clone [https://github.com/Raushan-tryingtocode/Python-Random-Dice-roller/tree/main](https://github.com/Raushan-tryingtocode/Python-Random-Dice-roller/tree/main)
3.**bash to run**:
    python dice_roller.py
