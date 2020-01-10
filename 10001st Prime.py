import numpy as np
primes = [2]  # instantiate first prime
possiblePrimes = np.arange(2,10)
def growPossiblePrimes():
	addValues = np.arange(max(possiblePrimes)+1, (max(possiblePrimes)+1)*2)
	# filter values already filtered before adding to array
	for i in primes:
		addValues = addValues[addValues%i!=0]
	return np.append(possiblePrimes, addValues)
# filter
i=0
cont = True
while cont is True:
	possiblePrimes = possiblePrimes[possiblePrimes%primes[i]!=0]
	primes.append(possiblePrimes[0])
	if len(primes) > 10000:
		cont = False
	i += 1
	if i >= len(possiblePrimes):
		possiblePrimes = growPossiblePrimes()
print("possiblePrimes")
print(possiblePrimes)
print("")
print("primes")
print(primes)
print("")
if len(primes) >= 10001:
	print("10001st prime")
	print(primes[10000]) # is 10001st prime
else:
	print("np 10001st prime found")