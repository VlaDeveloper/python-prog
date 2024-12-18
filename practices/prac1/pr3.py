from pr1 import get_random_int, print_list

if __name__ == '__main__':
		run_amount:int = int(input('Enter the amount of numbers: '))
		run_list = get_random_int(run_amount)
		print_list(run_list)
		print()
		cleaned_list = list(set(run_list))
		print_list(cleaned_list)