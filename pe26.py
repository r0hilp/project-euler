# divide out all the 2s and 5s
def div_2_and_5(n):
	while n % 2 == 0:
		n = n/2
	while n % 5 == 0:
		n = n/5
	return n

# cycle size for 1/n
def cycle_size(n):
	n = div_2_and_5(n)
	if n == 1:
		return 0
	size = 1
	while((10**size-1)%n != 0):
		size += 1
	return size

print [(n,cycle_size(n)) for n in range(1,1001)]

# ANS: 983