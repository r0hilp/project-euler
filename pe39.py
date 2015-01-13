# right triangle is formed by m^2+n^2, 2mn, m^2-n^2
# we require 2m^2 + 2mn = 2m(m+n) divides p

def num_solutions(p):
	sols = []
	for m in range(1, int((p/2)**0.5)+1):
		for n in range(1, m):
			total = 2*m*(m+n)
			if (total > p):
				break
			elif (p%total == 0):
				scale = p/total
				triple = set([(m*m+n*n)*scale, 2*m*n*scale, (m*m-n*n)*scale])
				if triple not in sols:
					sols.append(triple)
			else:
				continue
	return len(sols)

print max([(num_solutions(x),x) for x in range(1, 1001)])
# ANS: 840
