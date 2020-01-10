import numpy as np
a = 1
b = 1
recursionNums = [a,b]
iterationNums = [a,b]
def usingRecursion(digits,a,b):
	def fib(a, b):
		if len(str(b)) != digits:
			temp = a
			a = b
			b = b + temp
			recursionNums.append(b)
			fib(a, b)
	fib(a,b)
	print(fibnums)
def usingIteration(digits,a,b):
	cont = True
	while cont:
		if len(str(b)) != digits:
			temp = a
			a = b
			b = b + temp
			iterationNums.append(b)
		else:
			cont = False
	print(len(iterationNums))

usingIteration(1000,a,b)