import string

def game_instruction() -> None:
		print("""Wordle is a single player game 
A player has to guess a five letter hidden word 
You have six attempts 
Your Progress Guide "[a]bc[d](e)"  
"[a]" Indicates that the letter at that position was guessed correctly 
"(e)" indicates that the letter at that position is in the hidden word, but in a different position 
"b" indicates that the letter at that position is wrong, and isn't in the hidden word   """)


game_instruction()

def check_word() -> None:
	hidden_word = "snail"
	attempt = 6
	while attempt > 0:
		guess:string = str(input("Guess the word: "))
		if guess == hidden_word:
			print("You guessed the words correctly! Victory!")
			break
		else:
			attempt = attempt - 1
			print(f"you have {attempt} attempt(s) ,, \n ")
			for char, word in zip(hidden_word, guess):
						if word in hidden_word and word in char:
								# print(word + " [] ")
								print(f" [{word}] ")

						elif word in hidden_word:
								print(f" ({word}) ")
						else:
								print(f" {word} ")
			if attempt == 0:
				print(" Game over !!!! ")

check_word()
