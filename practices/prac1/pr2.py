from pr1 import get_random_int, print_list

def get_even_odd(l1:list, l2:list) -> list:
	res_list = []
	x = range(len(l1))
	for n in x:
		if n % 2 == 0:
			res_list.append(l1[n])

	y = range(len(l2))
	for n in y:
		if n % 2 == 1:
			res_list.append(l2[n])

	return res_list

if __name__ == '__main__':
		run_amount:int = int(input('Enter the amount of numbers: '))

		run_list = get_random_int(run_amount)
		run_list2 = get_random_int(run_amount)
		print_list(run_list)
		print()
		print_list(run_list2)
		print()
		mixed_list = get_even_odd(run_list, run_list2)
		print(mixed_list)