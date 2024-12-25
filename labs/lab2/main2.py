import json
from budgetTracker import BudgetTracker

f = open("bt.json", "r")
r = f.read()
y = json.loads(r)

bt = BudgetTracker(y["operations"], y["operationListSums"], y["isIncome"], y["operationListCategories"], y["operationCategories"])

choice = -1

while(choice != 7):
	print("""
	Pick your choice:
	1. Add a operation
	2. Print operations
	3. Add a category
	4. Print categories
	5. Change operation income/spending
	6. Assign the category
	7. Quit
			""")
	choice = int(input('Enter the number of command: '))
	print()
	match choice:
		case 1:
			bt.add_operation()
		case 2:
			bt.print_operations()
		case 3:
			bt.add_category()
		case 4:
			bt.print_categories()
		case 5:
			bt.change_operation()
		case 6:
			bt.assign_category()

x = {
	"operations": bt.operationList,
	"operationListSums": bt.operationListSums,
	"isIncome": bt.isIncome,
	"operationListCategories": bt.operationListCategories,
	"operationCategories": bt.operationCategories
}

y = json.dumps(x)
# print(y)

f = open("bt.json", "w")
f.write(y)
f.close()