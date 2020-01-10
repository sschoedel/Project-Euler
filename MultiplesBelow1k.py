def sum_below(num):
	nums = []
	for i in range(num):
		if i % 3 is 0 or i % 5 is 0:
			nums.append(i)
	return sum(nums)
print(sum_below(1000))