ns = []
candidates = []
for p in range(1,99999):
	ns.append(p*(3*p-1)/2)
for n,i in enumerate(ns):
	for j in ns[n+1:]:
		D = j-i
		S = j+i
		if S in ns:
			candidates.append(D)
print(candidates)