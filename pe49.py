from functions import is_prime, sieve, product
from itertools import permutations

LIMIT = 10000
primes = [i for i in sieve(LIMIT)]

# y is a permutation of x
def is_permutation(x, y):
	digits = [0 for i in range(10)]
	for digit in str(x):
		digits[int(digit)] += 1
	for digit in str(y):
		digits[int(digit)] -= 1
	return digits == [0 for i in range(10)]

# prime is in an arithmetic sequence of permutation primes
def works(prime):
	if('0' in str(prime)):
		return False
	prime_perms = set(filter(lambda x: is_prime(int(x)), [''.join(i) for i in permutations(str(prime))]))
	prime_sums = [(int(tup[0])+int(tup[1]))/2 for tup in product(prime_perms, prime_perms)]
	if prime_sums.count(prime) > 1:
		return True
	else:
		return False

for prime in primes:
	if prime < 1000:
		continue
	if works(prime):
		print prime

print 2969, 6299, 6299*2-2969

# ANS: 296962999629