import random

def game_instruction() -> None:
	print("""You play Rock-papper-scissors against the computer
You choices:
1. Rock
2. Papper
3. Scissors

Good luck!""")

def rock_papper_scissors() -> None:
	choice_list = ['rock', 'papper', 'scissors']

	choice:int = int(input('Choose the action(1-3): '))
	rint = random.randint(1, 3)
	
	if choice == rint:
		print("tie")
	elif choice == 1 and rint == 2:
		print("You lose")
	elif choice == 1 and rint == 3:
		print("You win")
	elif choice == 2 and rint == 1:
		print("You win")
	elif choice == 3 and rint == 1:
		print("You lose")
	elif choice == 2 and rint == 3:
		print("You lose")
	elif choice == 3 and rint == 2:
		print("You win")

	print(f'You picked {choice_list[choice-1]} and the computer picked {choice_list[rint-1]}')


game_instruction()
rock_papper_scissors()