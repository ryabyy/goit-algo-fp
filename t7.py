import random
from collections import Counter

def two_dice_simulation(n=1000):
	frequencies = Counter()
	for i in range(n):
		a, b = random.randint(1,6), random.randint(1,6)
		frequencies[a+b] += 1
	frequencies
	tab = [(a,b) for a,b in frequencies.items()]
	tab = sorted(tab, key=lambda p: p[0])
	return tab

simulations = 100000
res = two_dice_simulation(simulations)
max_len = 0
for pair in res:
	percentage = f"{pair[1]/simulations*100:.2f} %"
	row = f"{pair[0]:^10}|{percentage:^14}|{pair[1]:>8}"
	print(row)
	max_len = max(max_len, len(row))
print('-' * max_len)
print(f"{'Total':^10}|{'100.0 %':^14}|{simulations:>8}")