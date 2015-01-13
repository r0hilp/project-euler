from fractions import gcd

def is_prime(n):
	if(n == 1):
		return False
	for i in range(2, int(n**0.5) + 1):
		if n%i == 0:
			return False
	return True

# checks how many consecutive primes n^2 + an + b makes
def num_consecutive_primes(a, b):
	if (is_prime(abs(b)) == False):
		return 0
	common_div = gcd(a,b)
	bound = 0
	if (common_div > 1):
		bound = common_div
	else:
		bound = b
	for i in range(bound):
		output = i*i + a*i + b
		if is_prime(abs(output)):
			continue
		else:
			return i

BOUNDS = 1000

max_primes = 0
max_prod = 0
for a in range(BOUNDS*-1, BOUNDS+1):
	for b in range(BOUNDS*-1, BOUNDS+1):
		result = num_consecutive_primes(a,b)
		if (result > max_primes):
			max_primes = result
			max_prod = a*b

print max_primes, max_prod
# ANS -59231
