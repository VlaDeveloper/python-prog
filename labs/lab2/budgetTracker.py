class BudgetTracker:
	def __init__(self, operationList:list[str]=['scholarship', 'bus 41'],
							operationListSums:list[int]=[2500, 37],
							isIncome:list[bool]=[True, False],
							operationListCategories:list[str]=['academic', 'transport'],
							operationCategories:list[str]=['academic', 'transport']) -> None:
		self.operationList = operationList
		self.operationListSums = operationListSums
		self.operationCategories = operationCategories
		self.operationListCategories = operationListCategories
		self.isIncome = isIncome
	def add_operation(self) -> None:
		user_operation = input('Enter the operation description: ')
		self.operationList.append(user_operation)
		user_sum = input('Enter the operation sum: ')
		self.operationListSums.append(user_sum)
		user_income = input('Is the operation income?: (y, n) ')
		user_income_text = ''
		if user_income == 'y':
			self.isIncome.append(True)
			user_income_text = 'income'
		elif user_income == 'n':
			self.isIncome.append(False)
			user_income_text = 'spending'
		self.operationListCategories.append('')
		print(f'The {user_income_text} with the name {user_operation} and the sum {user_sum} is successfuly added!')
	def print_operations(self) -> None:
		a = range(len(self.operationList))
		print(f'You have {len(self.operationList)} operations:')
		# print(self.operationList)
		for i in a:
			res_income = "income" if self.isIncome[i] else "spending"
			res_category = f'#{self.operationListCategories[i]}' if self.operationListCategories[i] != '' else ""
			print(f'[ {res_income} ] {self.operationList[i]} with the sum {self.operationListSums[i]} {res_category}')
	def add_category(self) -> None:
		user_category = input('Enter the category: ')
		self.operationCategories.append(user_category)
		print(f'The category with the name {user_category} is successfuly added!')
	def print_categories(self) -> None:
		a = range(len(self.operationCategories))
		print(f'You have {len(self.operationCategories)} categories:')
		for i in a:
			print(self.operationCategories[i])
	def change_operation(self) -> None:
		user_num = int(input('Enter the number of the operation: '))
		user_change = input('Is it income?: (y, n) ')
		if user_change == 'y':
			self.isIncome[user_num-1] = True
			print(f'The operation with the name {self.operationList[user_num-1]} is income now!')
		elif user_change == 'n':
			self.isIncome[user_num-1] = False
			print(f'The operation with the name {self.operationList[user_num-1]} is spending now!')
	def assign_category(self) -> None:
		user_num = int(input('Enter the number of the operation: '))
		user_cat = int(input('Enter the number of the category: '))
		user_complete = input('Assign the category?: (y, n) ')
		if user_complete == 'y':
			self.operationListCategories[user_num-1] = self.operationCategories[user_cat-1]
			print(f'The operation with the name {self.operationList[user_num-1]} has got the category {self.operationCategories[user_cat-1]}!')
		elif user_complete == 'n':
			self.operationListCategories[user_num-1] = ''
			print(f'The operation with the name {self.operationList[user_num-1]} has no categories!')