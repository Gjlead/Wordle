from random import randrange

def load_allowed_guesses():
	allowed_guesses = list()
	with open("resources\english-allowed-guesses.txt", "r") as guess_list:
		for line in guess_list:
			allowed_guesses.append(line.rstrip("\n"))
	with open("resources\english-words.txt", "r") as word_list:
		for line in word_list:
			allowed_guesses.append(line.rstrip("\n"))
	return allowed_guesses
	

def create_word():
	with open("resources\english-words.txt", "r") as word_list:
		number_of_lines = sum(1 for _ in word_list)
		random_number = randrange(number_of_lines)
		
	# Open file anew to restart at the top
	with open("resources\english-words.txt", "r") as word_list:
		for line_counter, line in enumerate(word_list, 0):
			if line_counter == random_number:
				return line.rstrip("\n")
	

def handle_guess(word, allowed_guesses):
	print("Guess a word with five letters.")
	guess = input()

	if guess == word:
		return "Found word."
	if guess not in allowed_guesses:
		return "Guess not allowed."
	
	character_colors = list() # Green: Right character in right place. Yellow: Character exists in word, but somewhere else. Red: Character does not exist in word.
	for char_number, character in enumerate(guess, 0):
		if character == word[char_number]:
			character_colors.append("green")
		elif character in word:
			character_colors.append("yellow")
		else:
			character_colors.append("red")
			
	for number, color in enumerate(character_colors, 0):
		if color == "green":
			print(guess[number] + " is at the right place!")
		elif color == "yellow":
			print(guess[number] + " exists in the word, but somewhere else.")
		else:
			print(guess[number] + " does not exist in the word.")
	return ""

	
def main():
	allowed_guesses = load_allowed_guesses()
	word = create_word()
	
	guess_counter = 1
	
	while True:
		print("Remaining guesses: " + str(7-guess_counter))
		message = handle_guess(word, allowed_guesses)
		if message == "Found word.":
			print("Victory! You guessed " + word + " in " + str(guess_counter) + " moves!")
			break
		if message == "Guess not allowed.":
			print("Guess not allowed. Try again.")
			continue
			
		guess_counter = guess_counter + 1
		
		if guess_counter == 7:
			print("Game Over! The word was " + word + ".")
			break
	
	
main()


# to do:
# - GUI with colors
# - Different victory messages for different guess counters (like "Close one!" at six guesses)
# - Highscores
# - German version