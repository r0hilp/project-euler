def num_digits(n):
	return len(str(n))

fib1 = 1
fib2 = 1
counter = 2
while(num_digits(max(fib1, fib2)) < 1000):
	counter += 1
	if fib1 == max(fib1, fib2):
		fib2 = fib1+fib2
	else:
		fib1 = fib1+fib2

print max(fib1, fib2), counter