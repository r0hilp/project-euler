# Max x s.t. 2^x | n
def max_2_factor(n):
	x = 0
	while n % 2**x == 0:
		x += 1
	return x

def smallest_prime_factor(n):
	i = 2
	while(n % i != 0):
		i += 1
	return i

def num_divisors(n):
	primes = {}
	while(n != 1):
		fac = smallest_prime_factor(n)
		if fac in primes:
			primes[fac] += 1
		else:
			primes[fac] = 1
		n = n/fac
	tot = 1
	for prime in primes:
		tot *= primes[prime]+1
	return tot

# num divisors of T_n = n*(n+1)/2
def num_tri_divisors(n):
	if(n%2 == 0):
		power = max_2_factor(n)
	else:
		power = max_2_factor(n+1)
	return num_divisors(n)*num_divisors(n+1)*(power-1)/power

i = 3
while (num_tri_divisors(i) < 500):
	i += 1
print i*(i+1)/2

# ANS: 76576500