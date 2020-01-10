import random
a = 0
total = 0
while True:
	v = random.choice([-1, 1])
	if v == -1:
		a += 1
	total += 1
	print(f'Fraction: {a/total}')