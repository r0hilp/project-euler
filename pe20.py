def fact(n):
	if n == 1:
		return 1
	return fact(n-1)*n

def digit_sum(n):
	total = 0
	while(n != 0):
		total += n%10
		n = (n-n%10)/10
	return total

print digit_sum(fact(100))

# ANS: 648