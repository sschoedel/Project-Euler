def reverseString(s):
	if len(s) == 0:
		return
	temp = s[0]
	s[0] = s[-1]
	s[-1] = temp
	reverseString(s[1:-1])
	

word = ['h', 'e', 'l', 'l', 'o']
reverseString(word)
print(word)