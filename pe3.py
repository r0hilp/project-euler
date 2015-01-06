def smallest_prime_factor(n):
	i = 2
	while(n%i != 0):
		i = i+1
	return i

NUM = 600851475143

# prints the prime factors of NUM
while(NUM > 1):
	fact = smallest_prime_factor(NUM)
	print fact
	NUM = NUM/fact