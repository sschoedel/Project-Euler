palindromes = []
n = 12345

for i in range(100, 1000):
	for b in range(i):
		n = i * b
		palindrome = True
		for l in range(int(len(str(n))/2)):
			if str(n)[l] is not str(n)[-(l+1)]:
				palindrome = False
		if palindrome:
			palindromes.append(n)
print(max(palindromes))
					