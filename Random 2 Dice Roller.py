# Project: Random Dice Roller for Board games
# Purpose: Practice nested loops and dictionary mapping
# Author: Mohammed Raushan Hussain


import random


die_face = {1: ("┌─────────┐", "│         │", "│    ●    │", "│         │", "└─────────┘"),
            2: ("┌─────────┐", "│  ●      │", "│         │", "│      ●  │", "└─────────┘"),
            3: ("┌─────────┐", "│      ●  │", "│    ●    │", "│  ●      │", "└─────────┘"),
            4: ("┌─────────┐", "│  ●   ●  │", "│         │", "│  ●   ●  │", "└─────────┘"),
            5: ("┌─────────┐", "│  ●   ●  │", "│    ●    │", "│  ●   ●  │", "└─────────┘"),
            6: ("┌─────────┐", "│  ●   ●  │", "│  ●   ●  │", "│  ●   ●  │", "└─────────┘")}


is_running = True

while is_running:
    dice_per_roll = 2
    dice = []
    total = 0

    for die in range(dice_per_roll):
        dice.append(random.randint(1, 6))
    for line in range(5):
        for die in dice:
            print(die_face.get(die)[line], end="")
        print()
    for die in dice:
        total += die
    print(f"Total : {total}")

    user = input("Would you like to roll again(Y/N): ").upper()
    if not user == "Y":
        break
