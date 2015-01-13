# generate the first limit triangular numbers
def tri_gen(limit):
	tot = 0
	for i in range(1, limit+1):
		tot += i
		yield tot

def score(word):
	return sum([ord(letter)-64 for letter in word])

LIMIT = 100
tri_numbers = [i for i in tri_gen(100)]

f = open('pe42.txt', 'r')
names = f.read().split(',')
names = [name[1:len(name)-1] for name in names]
f.close()

print len(filter(lambda word: score(word) in tri_numbers, names))
# ANS: 162
