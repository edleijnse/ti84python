import unittest

from MASTR002 import setGuessflags
# https://stackoverflow.com/questions/52013612/python-unittest-does-not-run-tests

class Mastr002TestCase(unittest.TestCase):
    def test_setGuessflagsRed(self):
        chances = 8
        passcode = []
        passcode.append(1)
        passcode.append(6)
        passcode.append(2)
        passcode.append(5)
        turn=1
        guess_flags = [['-', '-', '-', '-'] for x in range(chances)]
        guess_codes = [['1', '6', '2', '5'] for x in range(chances)]
        newguessflags = setGuessflags(guess_flags,turn,guess_codes,passcode)
        self.assertEqual(['R', 'R', 'R', 'R'], newguessflags[1])

    def test_setGuessflagsRedWhite(self):
        chances = 8
        passcode = []
        passcode.append(1)
        passcode.append(6)
        passcode.append(2)
        passcode.append(5)
        turn=1
        guess_flags = [['-', '-', '-', '-'] for x in range(chances)]
        guess_codes = [['1', '6', '5', '2'] for x in range(chances)]
        newguessflags = setGuessflags(guess_flags,turn,guess_codes,passcode)
        self.assertEqual(['R', 'R', 'W', 'W'], newguessflags[1])

    def test_setGuessflagsNone(self):
        chances = 8
        passcode = []
        passcode.append(1)
        passcode.append(6)
        passcode.append(2)
        passcode.append(5)
        turn=1
        guess_flags = [['-', '-', '-', '-'] for x in range(chances)]
        guess_codes = [['2', '2', '3', '3'] for x in range(chances)]
        newguessflags = setGuessflags(guess_flags,turn,guess_codes,passcode)
        self.assertEqual(['W', '-', '-', '-'], newguessflags[1])

    def test_setGuessflagsSimulation2262(self):
        chances = 8
        passcode = []
        passcode.append(2)
        passcode.append(2)
        passcode.append(6)
        passcode.append(2)
        turn=1
        guess_flags = [['-', '-', '-', '-'] for x in range(chances)]
        guess_codes = [['1', '1', '2', '2'] for x in range(chances)]
        newguessflags = setGuessflags(guess_flags,turn,guess_codes,passcode)
        self.assertEqual(['-', '-', 'W', 'W'], newguessflags[1])

    def test_setGuessflagsSimulation4464(self):
        chances = 8
        passcode = []
        passcode.append(4)
        passcode.append(4)
        passcode.append(6)
        passcode.append(4)
        turn = 1
        guess_flags = [['-', '-', '-', '-'] for x in range(chances)]
        guess_codes = [['4', '4', '4', '4'] for x in range(chances)]
        newguessflags = setGuessflags(guess_flags, turn, guess_codes, passcode)
        self.assertEqual(['R', 'R', '-', 'R'], newguessflags[1])


if __name__ == '__main__':
    unittest.main()
