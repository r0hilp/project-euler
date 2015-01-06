f = open('pe13.txt', 'r')
tot = 0
for line in f:
	tot += int(line)
f.close()
tot = str(tot)
print tot[0:10]

# ANS: 5537376230