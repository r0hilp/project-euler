from functions import is_prime, sieve

LIMIT = 100000
PRIMES = [i for i in sieve(LIMIT)]

# all primes that are a sum of n consecutive primes from PRIMES
def consec(n):
	return filter(lambda x: is_prime(x) and x < 1000000, [sum(PRIMES[i:i+n]) for i in range(len(PRIMES)-n)])

for diff in range(550, 1, -1):
	result = consec(diff)
	if len(result) > 0:
		print result[len(result)-1]

# ANS: 997651
