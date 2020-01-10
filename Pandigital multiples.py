import numpy as np
pandigitalNums = []
for num in range(1,100000):
	for maxN in range(1,10):
		multiples = np.arange(1,maxN+1)
		s = ''
		for i in multiples:
			s += str(i*num)
		if len(s) == 9 and '1' in s and '2' in s and '3' in s and '4' in s and '5' in s and '6' in s and '7' in s and '8' in s:
			pandigitalNums.append(s)
print(pandigitalNums)
print(max(pandigitalNums))