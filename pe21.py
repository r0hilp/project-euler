def sum_proper_divisors(n):
	total = 0
	for i in range(1, n):
		if n%i == 0:
			total += i
	return total

MAX = 10000
print sum([n if sum_proper_divisors(sum_proper_divisors(n)) == n else 0 for n in range(1, MAX+1)])

# ANS: 40284