def alphabet_score(str):
	return sum([ord(x)-64 for x in str])

f = open('pe22.txt', 'r')
names = f.read().split(',')
f.close()

# convert to numbers and sort
names = [name[1:len(name)-1] for name in names]
names.sort()

print sum([(i+1)*alphabet_score(names[i]) for i in range(len(names))])

# ANS: 871198282