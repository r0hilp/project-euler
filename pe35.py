def is_prime(n):
	if(n == 1):
		return False
	for i in range(2, int(n**0.5) + 1):
		if n%i == 0:
			return False
	return True

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

LIMIT = 1000000
primes = [prime for prime in sieve(LIMIT)]

def binary_search(lst, n):
	if len(lst) == 1:
		return lst[0] == n
	mid = len(lst)/2
	if(n == lst[mid]):
		return True
	elif(n < lst[mid]):
		return binary_search(lst[:mid], n)
	else:
		return binary_search(lst[mid:], n)

def is_circular(prime):
	rot_prime = int(str(prime%10) + str(prime/10))
	if (prime < 10):
		return True
	while(rot_prime != prime):
		check = binary_search(primes, rot_prime)
		if (not check):
			return False
		rot_prime = int(str(rot_prime%10) + str(rot_prime/10))
	return True

print len(filter(lambda prime: is_circular(prime), primes))
# ANS: 55