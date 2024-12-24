# the future second lab
from taskTracker import TaskTracker

tt = TaskTracker()

choice = -1

while(choice != 10):
	print("""
	Pick your choice:
	1. Add a task
	2. Print tasks
	3. Add a category
	4. Print categories
	5. Complete the task
	6. Assign the category
	10. Quit
			""")
	choice = int(input('Enter the number of command: '))
	print()
	match choice:
		case 1:
			tt.add_task()
		case 2:
			tt.print_tasks()
		case 3:
			tt.add_category()
		case 4:
			tt.print_categories()
		case 5:
			tt.complete_task()
		case 6:
			tt.assign_category()