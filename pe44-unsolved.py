# P_n = n(3n-1)/2
# P_m - P_n = 1/2 * (3m^2 - m - 3n^2 + n) = 1/2*(m-n)*(3m+3n-1)
# P_m + P_n = 1/2 * (3m^2 - m + 3n^2 - n)

# generate the first limit pentagonal numbers
def pent_gen(limit):
	for i in range(1, limit+1):
		yield i*(3*i-1)/2

LIMIT = 10000
pents = [i for i in pent_gen(LIMIT)]

for diff in range(0,20):
	# minus[i] = pents[i+diff] - pents[i]
	minus = [pents[i+diff]-pents[i] for i in range(0, LIMIT-diff)]
	# plus[i] = pents[i+diff] - pents[i]
	plus = [pents[i+diff]+pents[i] for i in range(0, LIMIT-diff)]
	for i in range(0, LIMIT-diff):
		if plus[i] in pents:
			print plus[i], i, diff