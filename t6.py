def greedy_algorithm(items, constraint):
	selection = []

	priority = list(items.keys())
	priority.sort(key=lambda item: items[item]['calories'] / items[item]['cost'])

	foods = set(items)

	current = 0
	while current < constraint:
		last = current
		for food in priority:
			if food in foods:
				if current + items[food]['cost'] <= constraint:
					selection.append(food)
					foods.remove(food)
					current += items[food]['cost']
					break
		if current == last: return selection
	return selection

def dynamic_programming(items, constraint):
	selection = []

	foods = list(items)

	K = [[0 for c in range(constraint + 1)] for i in range(len(items) + 1)]

	for i in range(len(items) + 1):
		for c in range(constraint + 1):
			if i == 0 or c == 0:
				K[i][c] = 0
			elif items[foods[i - 1]]['cost'] <= c:
				K[i][c] = max(items[foods[i - 1]]['calories'] + K[i - 1][c - items[foods[i - 1]]['cost']], K[i - 1][c])
			else:
				K[i][c] = K[i - 1][c]
	j = constraint
	for i in range(len(items), 0, -1):
		if K[i][j] != K[i - 1][j]:
			food = foods[i - 1]
			selection.append(food)
			j -= items[food]["cost"]
	selection.reverse()
	return selection

items = {
	"pizza": {"cost": 50, "calories": 300},
	"hamburger": {"cost": 40, "calories": 250},
	"hot-dog": {"cost": 30, "calories": 200},
	"pepsi": {"cost": 10, "calories": 100},
	"cola": {"cost": 15, "calories": 220},
	"potato": {"cost": 25, "calories": 350}
}

constraint = 100
res = greedy_algorithm(items, constraint)
print("Greedy algorithm:", res)
res = dynamic_programming(items, constraint)
print("Dynamic programming:", res)