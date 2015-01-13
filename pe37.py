from functions import is_prime, sieve

LIMIT = 1000000
primes = [i for i in sieve(LIMIT)]

def right_trunc(prime):
	while(prime != 0):
		prime = prime/10
		if (is_prime(prime)):
			continue
		else:
			return False
	return True

def left_trunc(prime):
	prime = str(prime)
	while(len(prime) > 0):
		if (not is_prime(int(prime))):
			return False
		prime = prime[1:]
	return True

def trunc(prime):
	return left_trunc(prime) and right_trunc(prime)

print sum(filter(lambda prime: trunc(prime), primes)) - 2 - 3 - 5 - 7
# ANS: 748317