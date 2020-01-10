n = 19
cont = True
while cont:
	n += 1
	cont = False
	for i in range(11, 21):
		if n % i is not 0:
			cont = True
print(n)