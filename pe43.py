# builds a working pandigital off a 3-digit multiple n of 17
def build_pandigital(n):
	lst = [13,11,7,5,3,2,1]
	candidates = [n] 
	for prime in lst:
		temp = [] # stores new candidates
		for x in candidates:
			temp += filter(lambda entry: (int(entry[0:3])%prime == 0), [str(d)+x for d in range(10)])
		candidates = temp
	return filter(lambda x: ''.join(sorted(x)) == "0123456789", candidates)

final_lst = build_pandigital("017") + build_pandigital("034") + build_pandigital("051") + \
			build_pandigital("068") + build_pandigital("085")
for i in range(102, 1000, 17):
	final_lst += build_pandigital(str(i))
print sum([int(i) for i in final_lst])

# ANS: 16695334890