MAX = 100

def product(l1, l2):
	prod = []
	for i in l1:
		for j in l2:
			prod.append((i,j))
	return prod

print sum([tup[0]*tup[1] if tup[0] != tup[1] else 0 for tup in product(range(1, MAX+1), range(1, MAX+1))])