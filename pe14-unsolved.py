def has_pos(lst):
	for x in lst:
		if x >= 0:
			return True
	return False

def max_chain(n):
	chain = [i+1 for i in range(n)]
	chain[0] = -1
	count = 1
	while has_pos(chain):
		temp = chain[:]
		for i in range(len(chain)):
			if chain[i] < 0:
				continue
			if chain[i]%2 == 0:
				temp[i] = chain[i]/2
				if temp[i] < len(chain):
					if chain[temp[i]-1] < 0:
						temp[i] = count*-1 + chain[temp[i]-1]
			else:
				temp[i] = 3*chain[i]+1
				if temp[i] < len(chain):
					if chain[temp[i]-1] < 0:
						temp[i] = count*-1 + chain[temp[i]-1]
		chain = temp
		count += 1
	return chain

MAX = 1000000
min_index = 0
min_len = 0
chain = max_chain(MAX)
#print chain
for i in range(len(chain)):
	if chain[i] < min_len:
		min_index = i
		min_len = chain[i]

print min_index+1
