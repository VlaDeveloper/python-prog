class TaskTracker:
	def __init__(self, taskList:list[str]=['task 1', 'task 2'], taskComplete:tuple[str]=('done', 'not_done'),
							completedTasks:list[bool]=[True, False],
							taskListCategories:list[str]=['category 1', ''],
							taskCategories:list[str]=['category 1', 'category 2']) -> None:
		self.taskList = taskList
		self.taskComplete = taskComplete
		self.taskCategories = taskCategories
		self.taskListCategories = taskListCategories
		self.completedTasks = completedTasks
	def add_task(self) -> None:
		user_task = input('Enter the task: ')
		self.taskList.append(user_task)
		self.completedTasks.append(False)
		print(f'The task with the name {user_task} is successfuly added!')
	def print_tasks(self) -> None:
		a = range(len(self.taskList))
		print(f'You have {len(self.taskList)} tasks:')
		for i in a:
			res_complete = "x" if self.completedTasks[i] else " "
			res_category = f'#{self.taskListCategories[i]}' if self.taskListCategories[i] != '' else ""
			print(f'[ {res_complete} ] {self.taskList[i]} {res_category}')
	def add_category(self) -> None:
		user_category = input('Enter the category: ')
		self.taskCategories.append(user_category)
		print(f'The category with the name {user_category} is successfuly added!')
	def print_categories(self) -> None:
		a = range(len(self.taskCategories))
		print(f'You have {len(self.taskCategories)} categories:')
		for i in a:
			print(self.taskCategories[i])
	def complete_task(self) -> None:
		user_num = int(input('Enter the number of the task: '))
		user_complete = input('Complete it?: (y, n) ')
		if user_complete == 'y':
			self.completedTasks[user_num-1] = True
			print(f'The task with the name {self.taskList[user_num-1]} is successfuly completed!')
		elif user_complete == 'n':
			self.completedTasks[user_num-1] = False
			print(f'The task with the name {self.taskList[user_num-1]} is not done yet!')
	def assign_category(self) -> None:
		user_num = int(input('Enter the number of the task: '))
		user_cat = int(input('Enter the number of the category: '))
		user_complete = input('Assign the category?: (y, n) ')
		if user_complete == 'y':
			self.taskListCategories[user_num-1] = self.taskCategories[user_cat-1]
			print(f'The task with the name {self.taskList[user_num-1]} has got the category {self.taskCategories[user_cat-1]}!')
		elif user_complete == 'n':
			self.taskListCategories[user_num-1] = ''
			print(f'The task with the name {self.taskList[user_num-1]} has no categories!')