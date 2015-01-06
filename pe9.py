# Primitive pythag triplets are m^2+n^2, 2mn, m^2-n^2
# Sum is 2m^2 + 4mn

MAX = 1000

def product(l1, l2):
	prod = []
	for i in l1:
		for j in l2:
			prod.append((i,j))
	return prod

tests = product(range(1,MAX), range(1,MAX))
for tup in tests:
	a = tup[0]**2 + tup[1]**2
	b = tup[0]*tup[1]*2
	c = abs(tup[0]**2 - tup[1]**2)
	if(1000%(a+b+c) == 0):
		print a*b*c