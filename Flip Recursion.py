def reverseString(s):
	a = 0
	b = len(s) - 1
	while a < int(len(s)/2):
		temp = s[a]
		s[a] = s[b]
		s[b] = temp
		a += 1
		b -= 1

word = ['h', 'e', 'l', 'l', 'o']
reverseString(word)
print(word)


# def add_position_recur(lst, number_from=1):
#     if not lst:
#         return lst
#     return [lst[0]+number_from] + add_position_recur(lst[1:], number_from+1)
# lst = add_position_recur([1,2,3])