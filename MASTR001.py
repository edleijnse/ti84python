# https://www.geeksforgeeks.org/mastermind-game-using-python/
try:
  from ti_system import *
except Exception as e:
    print ("no module ti_system")
import random

# check if number is valid
def checkinput(iNumber):
    strNumber = str(iNumber)
    if (len(strNumber) == 4):
        return True
    else:
        return False


# the .randrange() function generates a
# random number within the specified range.
nok = True
while (nok):
    # to be rewritten for TI-84
    # https://www.w3schools.com/python/ref_random_randrange.asp
    num = random.randrange(1000, 10000)
    if checkinput(num) == True:
        nok = False
nok = True
while (nok):
    n = int(input("Guess the 4 digit number:"))
    if checkinput(n) == True:
        nok = False

# ctr variable initialized. It will keep count of
# the number of tries the Player takes to guess the number.
ctr = 0

# while loop repeats as long as the
# Player fails to guess the number correctly.
while (n != num):
    # variable increments every time the loop
    # is executed, giving an idea of how many
    # guesses were made.
    ctr += 1

    count = 0

    # explicit type conversion of an integer to
    # a string in order to ease extraction of digits
    n = str(n)

    # explicit type conversion of a string to an integer
    num = str(num)

    # correct[] list stores digits which are correct
    correct = ['X'] * 4

    # for loop runs 4 times since the number has 4 digits.

    for i in range(0, 4):

        # checking for equality of digits
        if (n[i] == num[i]):
            # number of digits guessed correctly increments
            count += 1
            # hence, the digit is stored in correct[].
            correct[i] = n[i]
        else:
            continue

    # when not all the digits are guessed correctly.
    if (count < 4) and (count != 0):
        print("Not quite the number. But you did get ", count, " digit(s) correct!")
        print("Also these numbers in your input were correct.")
        for k in correct:
            print(k, end=' ')
        print('\n')
        print('\n')
        n = int(input("Enter your next choice of numbers: "))

    # when none of the digits are guessed correctly.
    elif (count == 0):
        print("None of the numbers in your input match.")
        n = int(input("Enter your next choice of numbers: "))

print("You've become a Mastermind!")
print("It took you only", ctr, "tries.")
