def sum_divisors(n):
	total = 0
	for i in range(1, n+1):
		if n%i == 0:
			total += i
	return total

def product(l1, l2):
	prod = []
	for i in l1:
		for j in l2:
			prod.append((i,j))
	return prod

MAX = 28123
abundants = filter(lambda x: sum_divisors(x) > 2*x, range(MAX))
total = 0
for x in range(1, MAX):
	i = 0
	while(abundants[i] < x):
		if x - abundants[i] in abundants:
			total += x
			break
		else:
			i += 1
			continue

print sum(range(MAX)) - total