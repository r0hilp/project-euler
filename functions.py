def num_digits(n):
	return len(str(n))

def digit_sum(n):
	total = 0
	while(n != 0):
		total += n%10
		n = (n-n%10)/10
	return total

def reverse(str):
	return str[::-1]

def is_palindrome(n):
	str_n = str(n)
	return reverse(str_n) == str(n)

def is_prime(n):
	if(n == 1):
		return False
	for i in range(2, int(n**0.5) + 1):
		if n%i == 0:
			return False
	return True

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

def sum_divisors_bf(n):
	total = 0
	for i in range(1, n+1):
		if n%i == 0:
			total += i
	return total

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

def product(l1, l2):
	prod = []
	for i in l1:
		for j in l2:
			prod.append((i,j))
	return prod

# Generator for Erastosthenes sieve
def sieve(limit):
	numbers = [True for x in range(limit)] # numbers[i] = (i+1 is prime)
	numbers[0] = False
	for i in range(1, limit):
		if (is_prime(i)):
			for j in range(i*i, limit+1, i):
				numbers[j-1] = False
	for i in range(limit):
		if (numbers[i]):
			yield i+1