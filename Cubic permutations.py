cubes = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
permutations = []
n = 1
cont = True
while cont:
	c = n**3
	l = len(str(c))
	cubes[l-1].append(c)
	n += 1
	if n == 10000:
		cont = False
for i in range(len(cubes)):
	j = 0
	for c in cubes[i]:
		nums = [n for n in str(c)]
		remove = 0
		atLeastOne = False
		thesePerms = []
		for p in range(j+1,len(cubes[i])):
			compare = [s for s in str(cubes[i][p-remove])]
			isPerm = True
			for h in range(len(nums)):
				if nums[h] in compare:
					compare.remove(nums[h])
				else:
					isPerm = False
					break
			if isPerm:
				atLeastOne = True
				thesePerms.append(cubes[i][p-remove])
				cubes[i].remove(cubes[i][p-remove])
				remove += 1
		j += 1
		if atLeastOne:
			number = ''
			for numb in nums:
				number += numb
			thesePerms.append(int(number))
			permutations.append(thesePerms)
for p in permutations:
	if len(p) == 5:
		print(p)