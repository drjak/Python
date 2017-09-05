import random
HANGMANPICS = ['''

 +---+
 |   |
     |
     |
     |
     |
 ======''','''

 +---+
 |   |
 o   |
     |
     |
     |
 ======''','''

 +---+
 |   |
 o   |
 |   |
     |
     |
 ======''','''

 +---+
 |   |
 o   |
/|   |
     |
     |
 ======''','''

 +---+
 |   |
 o   |
/|\  |
     |
     |
 ======''','''

 +---+
 |   |
 o   |
/|\  |
/    |
     |
 ======''','''

 +---+
 |   |
 o   |
/|\  |
/ \  |
     |
 ======''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule nwet otter owl panda parrot pigeon python raboot ram rat raven rhino salmon seal sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWord(wordList):
 	wordIndex = random.randint(0, len(wordList) - 1)
 	return wordList[wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
 	print(HANGMANPICS[len(missedLetters)])
 	print()

 	print('Missed letters:', end=' ')
 	for letter in missedLetters:
 		print(letter, end=' ')
 	print()

 	blanks = '_' * len(secretWord)

 	for i in range(len(secretWord)):
 		if secretWord[i] in correctLetters:
 			blanks = blanks[:i] + secretWord[i]+blanks[i+1:]

 	for letter in blanks:
 		print(letter, end=' ')
 	print()

def getGuess(alreadyGuessed):
    #this function makes sure this is letter
 	while True:
 		print('Guess a letter.')
 		guess = input()
 		guess = guess.lower()
 		if len(guess) != 1:
 			print('Please enter a single letter.')
 		elif guess in alreadyGuessed:
 			print('You have already guessed this letter')
 		elif guess not in 'abcdefghijklmnopqrstuvwxyz':
 			print('Please enter LETTER')
 		else:
 			return guess

def playAgain():
 	#returns true if player want play again
 	print('Do you want to play again? (yes or no)')
 	return input().lower().startswith('y')


print('H A N G M A N')
missedLetters=''
correctLetters=''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
	displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

	#let player type
	guess = getGuess(missedLetters+correctLetters)

	if guess in secretWord:
		correctLetters = correctLetters + guess

		#check if  player won
		foundAllLetters = True
		for i in range(len(secretWord)):
			if secretWord[i] not in correctLetters:
				foundAllLetters = False
				break
		if foundAllLetters:
			print('Yes! Secret word is "' + secretWord +'"! You have won!')
			gameIsDone = True
	else:
		missedLetters = missedLetters + guess

	#check if player had guessed too many times
	if len(missedLetters)==len(HANGMANPICS) - 1:
		displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
		print('You have run out of guess!\nAfter '+str(len(missedLetters))+' missed guesses and '+str(len(correctLetters))+' correct guesses\nThe word was "'+secretWord+'"')
		gameIsDone=True

	if gameIsDone:
		if playAgain():
			missedLetters=''
			correctLetters=''
			gameIsDone=False
			secretWord=getRandomWord(words)
		else:
			break



