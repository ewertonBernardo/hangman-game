

def undescore_letters(word):
	letters = []
	for letter in word:
		letters.append('__')
	return letters


def show_letters(letters):
	for l in letters:
		print(l,end=' ')
	print('\n')


def check_word(word, letters):
	letters = "".join(letters)
	if (word == letters):
		return True



word = input('What\'s the word?').upper()


letters = undescore_letters(word)
show_letters(letters)


while True:
	attempt = input('Choose a letter: ').upper()
	for i,l in enumerate(word):
		if(attempt == l):
			#print(i)
			letters[i] = attempt

	show_letters(letters)
	if(check_word(word, letters)):
		print("HIT!")
		break