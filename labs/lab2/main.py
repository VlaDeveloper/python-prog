import json
from taskTracker import TaskTracker

f = open("tt.json", "r")
r = f.read()
y = json.loads(r)

tt = TaskTracker(y["tasks"], y["completedTasks"], y["taskListCategories"], y["taskCategories"])

choice = -1

while(choice != 7):
	print("""
	Pick your choice:
	1. Add a task
	2. Print tasks
	3. Add a category
	4. Print categories
	5. Complete the task
	6. Assign the category
	7. Quit
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

x = {
	"tasks": tt.taskList,
	"completedTasks": tt.completedTasks,
	"taskListCategories": tt.taskListCategories,
	"taskCategories": tt.taskCategories
}

y = json.dumps(x)

f = open("tt.json", "w")
f.write(y)
f.close()