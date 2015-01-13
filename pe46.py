from functions import is_prime, sieve

LIMIT = 10000
primes = [prime for prime in sieve(LIMIT)]

# n is odd, composite, and cannot be written as
# the sum of a prime and twice a square
def works(n):
	if(is_prime(n)):
		return True
	for prime in primes:
		# print prime
		if prime > n:
			return False
		test = ((n - prime)/2)**0.5
		if int(test) - test == 0:
			return True

print filter(lambda x: not works(x), range(1, 10000, 2))
# ANS: 5777