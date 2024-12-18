import random
from pr1 import print_list

def get_random_dict(amount: int) -> dict:
		res_dict = dict()
		x = range(amount)
		a = 1
		b = 10

		for n in x:
			rint = random.randint(a, b)
			rint = round(rint)
			res_dict[f'num{n}'] = rint
		
		return res_dict

def print_dict(mydict: dict) -> None:
	a = range(len(mydict))
	for n in a:
		print(mydict[f'num{n}'])

def existsOnce3(aDict: dict) -> list:
	vals = dict()
	# create dict to sum all value counts
	for i in aDict.values():
			vals.setdefault(i,0)
			vals[i] += 1
	# use each v/val from aDict as the key to vals
	# keeping each k/key from aDict if the count is 1
	return sorted(k for k, v in aDict.items() if vals[v] == 1)

def make_tuple_list(mylist: list, mydict: dict) -> list:
	lst = list()
	a = range(len(mydict))
	b = range(len(mylist))
	for n in b:
		my_tpl = (mydict[mylist[n]], [mylist[n]])
		lst.append(my_tpl)
	return lst

if __name__ == '__main__':
		run_amount:int = int(input('Enter the amount of numbers: '))
		run_dict = get_random_dict(run_amount)
		print_dict(run_dict)
		print()
		test = existsOnce3(run_dict)
		print_list(test)
		print()
		lst_tpl = make_tuple_list(test, run_dict)
		print_list(lst_tpl)
