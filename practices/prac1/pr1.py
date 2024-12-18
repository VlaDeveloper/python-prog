import random

def get_random_int(amount: int) -> list:
		res_list = []
		x = range(amount)
		a = 1
		b = 10

		for n in x:
			rint = random.randint(a, b)
			rint = round(rint)
			res_list.append(rint)
		
		return res_list

def print_list(mylist: list) -> None:
	a = range(len(mylist))
	for n in a:
		print(mylist[n])

if __name__ == '__main__':
		run_amount:int = int(input('Enter the amount of numbers: '))
		run_list = get_random_int(run_amount)
		print_list(run_list)
		print()
		run_list.reverse()
		print_list(run_list)