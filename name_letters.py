#! /usr/bin/python

def check_name():
	print ("Please tell name to check")
	name = raw_input()
	return name

def letter_number(name):
	print ('Hello ' + name + ' your name consist of '+str(len(name))+ ' letters')


#check_name()
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
	letter_number(check_name())
	print ("Want play again? (y/yes)")
	playAgain = raw_input()
