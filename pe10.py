MAX = 2000000

all_nums = range(1, MAX)
sieve = [0 for x in range(MAX)]

for i in range(2, MAX+1):
	temp = i*2
	while(temp <= MAX):
		sieve[temp-1] += 1
		temp += i

print sum([x+1 if sieve[x] == 0 else 0 for x in range(0, len(sieve))])-1

# ANS: 142913828922