# fibnumbers = []
# fibs = []
# N = 90
# def fib(n,a,b):
# 	if n <= N:
# 		temp = b
# 		b = a + b
# 		a = temp
# 		n += 1
# 		fibs.append(b)
# 		fib(n,a,b)
# fib(2,0,1)
# print(fibs)
# numbers = []
# prevc = 0
# for c in fibs:
# 	print(f'c: {c}')
# 	digits = []
# 	p = c
# 	while p != 0:
# 		if p >= 9:
# 			digits.append(9)
# 			p -= 9
# 		else:
# 			digits.append(p)
# 			p -= p
# 	f = ""
# 	for v in digits:
# 		f += str(v)
# 	currentVal = int(f)
# 	numbers.append(currentVal)
# 	p = c
# 	p -= 1
# 	while p != prevc:
# 		digits[0] -= 1
# 		if digits[0] == 0:
# 			digits = digits[1:]
# 		f = ""
# 		for v in digits:
# 			f += str(v)
# 		if f != "":
# 			currentVal = int(f)
# 			numbers.append(currentVal)
# 		p -= 1
# 	prevc = c
# 	# print(f'sum all: {sum(numbers)}')
# 	# print("")
# 	fibnumbers.append(sum(numbers))
# print(f'sum all of sum all: {sum(fibnumbers)}')
# print("")
# print(f'mod 1000000007: {sum(fibnumbers)%1000000007}')
fibnumbers = []
fibs = []
N = 90
def fib(n,a,b):
	if n <= N:
		temp = b
		b = a + b
		a = temp
		n += 1
		fibs.append(b)
		fib(n,a,b)
fib(2,0,1)
print(fibs)
numbers = []
prevc = 0
fibs = [2880067194370816120]
for c in fibs:
	r = c%9
	t = int(c/9)
	digits = [r]
	digits += [9]*t
	print(digits)

print(f'sum all of sum all: {sum(fibnumbers)}')
print("")
print(f'mod 1000000007: {sum(fibnumbers)%1000000007}')