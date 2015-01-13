from itertools import permutations
from functions import is_prime, sieve, smallest_prime_factor

LIMIT = 1000000
primes = [i for i in sieve(LIMIT)]

# has 4 prime factors
def works(n):
	factors = {}
	while (n > 1):
		factor = smallest_prime_factor(n)
		if factor in factors:
			factors[factor] += 1
		else:
			factors[factor] = 1
		n = n/factor
	return (len(factors.keys()) == 4)

# creates an array with arr[i] = (num prime factors in i+1)
def nfactors_sieve(limit):
	lst = [0 for x in range(limit)]
	for prime in primes:
		for i in range(prime, limit+1, prime):
			lst[i-1] += 1
	return lst

factor_lst = nfactors_sieve(1000000)
for i in range(0, len(factor_lst)-3):
	if factor_lst[i:i+4] == [4,4,4,4]:
		print i

# ANS: 134043