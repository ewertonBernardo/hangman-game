
import os

def undescore_letters(word):
	letters = []
	for letter in word:
		letters.append('__')
	return letters


def show_letters(letters):
	for l in letters:
		print(l,end=' ')
	print('\n')


def check_letter(word, letter):
	if (letter in word):
		return True

def check_word(word, letters):
	letters = "".join(letters)
	if (word == letters):
		return True

def screen_clear():
  os.system('cls' if os.name == 'nt' else 'clear')
  

remaining_attempts  = 5
word = input('What\'s the word?').upper()
screen_clear()

letters = undescore_letters(word)
show_letters(letters)


while True and remaining_attempts > 0:
	attempt = input('Choose a letter: ').upper()
	for i,l in enumerate(word):
		if (attempt == l):
			letters[i] = attempt

	show_letters(letters)

	if (check_letter(word, attempt) == None):
		remaining_attempts -= 1
		print(f'Remaining attempts: {remaining_attempts}')

	if (check_word(word, letters)):
		print("HIT!")
		break
	elif (remaining_attempts == 0):
		print("LOSE!")