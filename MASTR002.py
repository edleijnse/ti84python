# https://www.askpython.com/python/examples/create-mastermind-game-in-python
try:
    from ti_system import *
except Exception as e:
    print("no module ti_system")

import random

dottedline = "--------------------------"


def clear():
    try:
        system("cls")
    except NameError:
        print("======")


# Function to print the mastermind board
def print_mastermind_board(passcode, guess_codes, guess_flags):
    print(dottedline)
    print(" MASTERMIND")
    print(passcode)
    print(dottedline)

    # print("    |", end="")
    # for x in passcode:
    #    print("\t" + x[:3], end="")
    # print()

    # for i in reversed(range(len(guess_codes))):
    maxi = len(guess_codes)
    i = maxi
    while i > 0:
        i = i - 1
        # print(dottedline)
        print(guess_flags[i][0], guess_flags[i][1], guess_flags[i][2], guess_flags[i][3], end=" |")

        # print(guess_flags[i][2], guess_flags[i][3], end=" |")
        for x in guess_codes[i]:
            print("\t" + x[:3], end="")

        print()
    print(dottedline)

# Function to set the guess_flags
def setGuessflags(guess_flags, turn, code, passcode):
    ii = 0
    passcodeItemChecked=[]
    for x in code:
        if (ii==turn):
           cc=0
           for codeitem in x:
               pp=0
               for passcodeitem in passcode:
                   # check if passworditem is already processed
                   toprocess = True
                   for pitem in passcodeItemChecked:
                       if pitem == pp:
                           toprocess = False
                   if toprocess == True:
                      if (str(codeitem)==str(passcodeitem)):
                         if cc==pp:
                            guess_flags[turn][cc] = 'R'
                         else:
                            guess_flags[turn][cc] = 'W'
                         passcodeItemChecked.append(pp)
                         break
                   pp +=1
               cc +=1
        ii +=1
    return guess_flags

# The Main function
# if __name__ == '__main__':

# List of colors
colors = ["1RED", "2GREEN", "3YELLOW", "4BLUE", "5BLACK", "6ORANGE"]

# Mapping of colors to numbers
colors_map = {1: "1RED", 2: "2GREEN", 3: "3YELLOW", 4: "4BLUE", 5: "5BLACK", 6: "6ORANGE"}

# Randomly selecting a passcode
# to be rewritten for TI-84
# https://www.w3schools.com/python/ref_random_randrange.asp
# random.shuffle(colors)
col1 = random.randrange(1, 6)
col2 = random.randrange(1, 6)
col3 = random.randrange(1, 6)
col4 = random.randrange(1, 6)
# passcode = colors[:4]
passcode = []
passcode.clear()
passcode.append(colors[col1])
passcode.append(colors[col2])
passcode.append(colors[col3])
passcode.append(colors[col4])

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

    print(dottedline)
    print("\t\tMenu")
    print(dottedline)
    print("Enter code using numbers.")
    print("1 - RED, 2 - GREEN, 3 - YELLOW, 4 - BLUE, 5 - BLACK, 6 - ORANGE")
    print("Example: RED YELLOW ORANGE BLACK ---> 1 3 6 5")
    print(dottedline)
    print_mastermind_board(show_passcode, guess_codes, guess_flags)

    # Accepting the player input
    try:
        code = list(map(int, input("Enter choice (.) = ").split(".")))
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

    guess_flags = setGuessflags(guess_flags, turn, guess_codes, passcode)


    # Check for win condition
    if guess_codes[turn] == passcode:
        clear()
        print_mastermind_board(passcode, guess_codes, guess_flags)
        print("YOU WIN!!!!")
        break

    # Update turn
    turn += 1
    clear()

# Check for loss condiiton
if turn == chances:
    clear()
    print_mastermind_board(passcode, guess_codes, guess_flags)
    print("YOU LOSE!!!")
