stringList = ['H','E','L','L','O']

i = 0
j = len(stringList)-1 

def flipString(stringList, i, j):
	if i < j:
		temp = stringList[j]
		stringList[j] = stringList[i]
		stringList[i] = temp
		i += 1
		j -= 1
		flipString(stringList, i, j)

flipString(stringList, i, j)
print(stringList)