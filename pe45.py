# generate the first limit triangular numbers
def tri_gen(limit):
	tot = 0
	for i in range(1, limit+1):
		tot += i
		yield tot

# generate the first limit pentagonal numbers
def pent_gen(limit):
	for i in range(1, limit+1):
		yield i*(3*i-1)/2

# generate the first limit hexagonal numbers
def hex_gen(limit):
	for i in range(1, limit+1):
		yield i*(2*i-1)

LIMIT = 200000
tri = [i for i in tri_gen(LIMIT)]
pent = [i for i in pent_gen(LIMIT)]
hexag = [i for i in hex_gen(LIMIT)]
print set(tri).intersection(set(pent), set(hexag))
# ANS: 7906276