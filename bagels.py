
import random

def getSecretNum(numDigits):
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(numDigits):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'

    clue = []

    for i in range(len(secretNum)):
        if guess[i] == secretNum[i]:
            clue.append('Fermi')
        elif guess[i] in secretNum:
            clue.append('Pico')
        if len(clue) == 0:
            return 'Bagels'

        clue.sort()
        return ' '.join(clue)

def isOnlyDigits(num):
    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True

def playAgain():
    print('Do you want to play again? Y/N')
    return input().lower().startswith('y')

NUMDIGITS = 3
MAXGUESS = 10

print('I am thinking about %s-digit number. Try to gues' %(NUMDIGITS))
print('Pico - one digit correct but in wrong position')
print('Fermi - one digit correct and in correct position')
print('Bagels - no digit is correct')

while True:
    secretNum = getSecretNum(NUMDIGITS)
    print('I have secret number, you have %s guesses' %(MAXGUESS) )

    numGuesses = 1
    while numGuesses <= MAXGUESS:
        guess = ''
        while len(guess) != NUMDIGITS or not isOnlyDigits(guess):
            print('Guess #%s' %(numGuesses))
            guess = input()

        clue = getClues(guess, secretNum)
        print(clue)
        numGuesses += 1

        if guess == secretNum:
            break
        if numGuesses > MAXGUESS:
            print('You run out of guesses, answer was %s' %(secretNum))

    if not playAgain():
        break

