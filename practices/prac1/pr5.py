import random
import string

def get_random_dict(amount: int, keyword: string) -> dict:
		res_dict = dict()
		x = range(amount)
		a = 1
		b = 10

		for n in x:
			rint = random.randint(a, b)
			rint = round(rint)
			res_dict[f'{keyword}{n}'] = rint
		
		return res_dict

def print_dict(mydict: dict) -> None:
	for i in mydict.keys():
			print(i, ':', mydict[i])

def make_common_dict(dct1: dict, dct2: dict, k1: string, k2: string) -> dict:
	dct = dict()
	for i in dct1.keys():
			for j in dct2.keys():
				if dct1[i] == dct2[j]:
					# print(i, ':', dct1[i], j, ':', dct2[j])
					dct[i] = dct1[i]
					dct[j] = dct2[j]

	return dct

if __name__ == '__main__':
		run_amount:int = int(input('Enter the amount of numbers: '))
		run_dict = get_random_dict(run_amount, 'num')
		run_dict2 = get_random_dict(run_amount, 'foo')
		print_dict(run_dict)
		print()
		print()
		print_dict(run_dict2)
		print()
		print()
		com_dct = make_common_dict(run_dict, run_dict2, 'num', 'foo')
		print()
		print()
		print_dict(com_dct)
