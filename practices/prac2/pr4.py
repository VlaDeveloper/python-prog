import math

def divisorGenerator(n: int) -> list:
	large_divisors = []
	for i in range(1, int(math.sqrt(n) + 1)):
			if n % i == 0:
					yield i
					if i*i != n:
							large_divisors.append(n / i)
	for divisor in reversed(large_divisors):
			yield divisor

number:int = int(input('Enter the number: '))
res_list = list(divisorGenerator(number))

print(res_list)

if len(res_list) <= 2:
	print('Number is prime')
else:
	print('Number is not prime')