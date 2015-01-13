from itertools import permutations

perms = permutations("0123456789")
count = 0
for i in perms:
	count += 1
	if count == 1000000:
		print i 

# ANS: 2783915460