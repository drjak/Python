#!/usr/bin/python
import random

print('Hello, What is your name?')
myName = raw_input()

def adding(myName):
	number1 = random.randint(1, 10)
	number2 = random.randint(1, 10)
	right = 0
	wrong = 0
	print (myName + ' what is ' +str(number1) + '+' +str(number2) +' ?')
	answer = input()
	if int(answer) == number1 + number2:
		print ('That is right !')
		right=right+1
		return right
	else:
		print ("That is wrong!")
		wrong = wrong + 1
		return wrong

attempt = 0
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
	attempt = attempt + 1
	adding(myName)
	print ("Want play again? (y/yes), you made "+str(attempt)+' attempts')
	playAgain = raw_input()           
                   
