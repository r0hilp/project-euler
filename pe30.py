MAX = 5*59049

def digit_power_sum(n, p):
	total = 0
	while n != 0:
		total += (n%10)**p
		n = (n-n%10)/10
	return total

total = 0
for i in range(2, MAX):
	if digit_power_sum(i, 5) == i:
		print i
		total += i

print total