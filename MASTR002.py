# https://www.askpython.com/python/examples/create-mastermind-game-in-python
try:
  from ti_system import *
except Exception as e:
    print ("no module ti_system")

import random
try:
  from os import system
except Exception as e:
    print ("no module os")

def clear():
    system("cls")


# Function to print the mastermind board
def print_mastermind_board(passcode, guess_codes, guess_flags):
    print("-----------------------------------------")
    print("\t      MASTERMIND")
    print("-----------------------------------------")

    print("    |", end="")
    for x in passcode:
        print("\t" + x[:3], end="")
    print()

    for i in reversed(range(len(guess_codes))):
        print("-----------------------------------------")
        print(guess_flags[i][0], guess_flags[i][1], "|")

        print(guess_flags[i][2], guess_flags[i][3], end=" |")
        for x in guess_codes[i]:
            print("\t" + x[:3], end="")

        print()
    print("-----------------------------------------")

# The Main function
#if __name__ == '__main__':

# List of colors
colors = ["RED", "GREEN", "YELLOW", "BLUE", "BLACK", "ORANGE"]

# Mapping of colors to numbers
colors_map = {1: "RED", 2: "GREEN", 3: "YELLOW", 4: "BLUE", 5: "BLACK", 6: "ORANGE"}

# Randomly selecting a passcode
random.shuffle(colors)
passcode = colors[:4]


# Number of chances for the player
chances = 8

# The passcode to be shown to the user
show_passcode = ['UNK', 'UNK', 'UNK', 'UNK']

# The codes guessed by the player each turn
guess_codes = [['-', '-', '-', '-'] for x in range(chances)]

# The clues provided to the player each turn
guess_flags = [['-', '-', '-', '-'] for x in range(chances)]

clear()

# The current turn
turn = 0

# The GAME LOOP
while turn < chances:

    print("-----------------------------------------")
    print("\t\tMenu")
    print("-----------------------------------------")
    print("Enter code using numbers.")
    print("1 - RED, 2 - GREEN, 3 - YELLOW, 4 - BLUE, 5 - BLACK, 6 - ORANGE")
    print("Example: RED YELLOW ORANGE BLACK ---> 1 3 6 5")
    print("-----------------------------------------")
    print_mastermind_board(show_passcode, guess_codes, guess_flags)

    # Accepting the player input
    try:
        code = list(map(int, input("Enter your choice = ").split()))
    except ValueError:
        clear()
        print("\tWrong choice!! Try again!!")
        continue

        # Check if the number of colors nunbers are 4
    if len(code) != 4:
        clear()
        print("\tWrong choice!! Try again!!")
        continue

    # Check if each number entered corresponds to a number
    flag = 0
    for x in code:
        if x > 6 or x < 1:
            flag = 1

    if flag == 1:
        clear()
        print("\tWrong choice!! Try again!!")
        continue

        # Storing the player input
    for i in range(4):
        guess_codes[turn][i] = colors_map[code[i]]

        # Process to apply clues according to the player input
    dummy_passcode = [x for x in passcode]

    pos = 0

    # Loop to set up clues for the player move
    for x in code:
        if colors_map[x] in dummy_passcode:
            if code.index(x) == passcode.index(colors_map[x]):
                guess_flags[turn][pos] = 'R'
            else:
                guess_flags[turn][pos] = 'W'
            pos += 1
            dummy_passcode.remove(colors_map[x])

    random.shuffle(guess_flags[turn])

    # Check for win condition
    if guess_codes[turn] == passcode:
        clear()
        print_mastermind_board(passcode, guess_codes, guess_flags)
        print("Congratulations!! YOU WIN!!!!")
        break

    # Update turn
    turn += 1
    clear()

# Check for loss condiiton
if turn == chances:
    clear()
    print_mastermind_board(passcode, guess_codes, guess_flags)
    print("YOU LOSE!!! Better luck next time!!!")