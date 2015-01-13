# get upper bound

n = 1
while(len(str(9**n)) == n):
	print 9**n
	n += 1

print n

BOUND = 22
total = 0
for n in range(1, BOUND+1):
	for d in range(1,10):
		if len(str(d**n)) == n:
			total += 1

print total