# list of factorials up to n
def facts_to_n(n):
	facts = [1]
	for i in range(2, n+1):
		facts.append(i*facts[i-2])
	return facts

MAX = 100
FACTS = facts_to_n(MAX)

# find nCr for n <= MAX
def choose(n, r): 
	combs = FACTS[n-1]/(FACTS[r-1]*FACTS[n-r-1])
	#print combs
	return combs

total = 0

for n in range(1,MAX+1):
	for r in range(1,n+1):
		if choose(n,r) > 1000000:
			total = total + 1

print total