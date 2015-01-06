MIN = 1
MAX = 1000000

# check if x, 2x, ... 6x all have same digits
def check_num(n):
	num_digits = len(str(n))
	if n > 10**num_digits/6:
		return False
	count = [0 for k in range(10)] # array tracking digit counts
	mults = [k*n for k in range(1,7)] # strings of all the multiples
	for num in mults:
		while num > 0:
			count[num%10] = count[num%10] + 1
			num = (num - num%10)/10

	for entry in count:
		if entry != 0 and entry != 6:
			#print "No!"
			return False

	print "Yes! " + str(n)
	return True

for i in range(MIN, MAX):
	check_num(i)