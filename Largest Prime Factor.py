import math

primeFactors = []
num = 13195

for i in range(2, math.ceil(num/2) + 1):
	while num % i is 0:
		primeFactors.append(i)
		num = int(num/i)
print(max(primeFactors))