

def undescore_letters(word):
	letters = []
	for letter in word:
		letters.append('__')
	return letters


def show_letters(letters):
	for l in letters:
		print(l,end=' ')
	print('\n')



word = input('What\'s the word?')


letters = undescore_letters(word)
show_letters(letters)


while True:
	attempt = input('Choose a letter: ')
	for i,l in enumerate(word):
		if(attempt == l):
			#print(i)
			letters[i] = attempt

	show_letters(letters)
	