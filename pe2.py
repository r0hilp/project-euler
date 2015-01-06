fib = [1,1]
while(fib[len(fib)-1] < 4000000):
	fib.append(fib[len(fib)-1]+fib[len(fib)-2])

print sum([x if x%2 == 0 else 0 for x in fib])