def fib(maxNum):
	a = 1
	b = 2
	nums = []
	fibNums = [a, b]
	while b < maxNum:
		a, b  = b, a + b
		if b <= maxNum:
			fibNums.append(b)
	for i in fibNums:
		if i % 2 is 0:
			nums.append(i)
	return sum(nums)
print(fib(4000000))