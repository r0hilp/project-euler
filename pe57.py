from fractions import gcd

def num_digits(n):
	return len(str(n))

MAX = 1000

# do for convergents up to MAX

num = 3
denom = 2
total = 0

# S_n = 1 + 1/(1 + S_(n-1))

for i in range(MAX):
	num = num + denom
	num, denom = denom, num
	num = num + denom
	fac = gcd(num, denom)
	num, denom = num/fac, denom/fac
	if(num_digits(num) > num_digits(denom)):
		total += 1
	#print num,denom

print total