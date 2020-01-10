import numpy as np
result = [0, 0, 0]
for b in range(1000):
	for a in range(1, b):
		if a + b + np.sqrt(a**2 + b**2) == 1000:
			result = [a, b, int(np.sqrt(a**2 + b**2))]
print(np.prod(result))