#!/usr/bin/python

import random
guessTaken = 0

print('Hello, What is your name?')
myName = raw_input()

number = random.randint(1,20)
print('OK, ' + myName + ', I am thinking of number between 1 and 20')

while guessTaken < 6:
    print ('Take a guess')
    guess = input()
    guess = int(guess)

    guessTaken = guessTaken + 1

    if guess < number:
        print('too low')

    if guess > number:
        print('too big')

    if guess == number:
        print('thats the kill')
        break

if guess == number:
    guessTaken = str(guessTaken)
    print('good job, you guessed in '  + guessTaken + ' attempts')

if guess != number:
    number = str(number)
    print('nope,the number was '+number)
            
