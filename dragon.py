#!/usr/bin/python

import random
import time

def displayIntro():
    print("You approach dragon area")

def chooseCave():
    cave = ''
    #input validation, assure that in return will be 1 or 2
    #until 1 or 2 it will go back to beginning and keep asking
    while cave != '1' and cave != '2':
        print("Which cave you choose? 1 or 2")         
        cave = raw_input()
    
    return cave

def checkCave(chosenCave):
    print("You approach cave...")
    time.sleep(2)
    print ("It is dark and spooky")
    time.sleep(2)

    friendlyCave = random.randint(1,2)

    if chosenCave == str(friendlyCave):
               print ("winner")
    else:
              print ("eaten")


playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print ("want play again? (y/yes)")
    playAgain = raw_input()
               
