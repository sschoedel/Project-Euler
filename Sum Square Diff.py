n = 100

sumn = 0

squares = []
for i in range(n+1):
	squares.append(i**2)
sumSquares = sum(squares)

for i in range(n+1):
	sumn = sumn + i
squareSum = sumn**2

print(sumSquares)
print(squareSum)
print(squareSum - sumSquares)