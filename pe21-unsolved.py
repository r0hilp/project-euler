def smallest_prime_factor(n):
	i = 2
	while(n % i != 0):
		i += 1
	return i

def sum_divisors(n):
	primes = {}
	while (n != 1):
		fac = smallest_prime_factor(n)
		if fac in primes:
			primes[fac] += 1
		else:
			primes[fac] = 1
		n = n/fac
	tot = 1
	for prime in primes:
		tot *= (prime**(primes[prime]+1)-1)/(prime-1)
	return tot

def sum_proper_divisors(n):
	return sum_divisors(n)-n

MAX = 10000
print filter(lambda n: sum_proper_divisors(sum_proper_divisors(n)) == n, range(1, MAX+1))

# ANS: 40284