f = open('pe8.txt', 'r')
num = ''
for line in f:
	num += line
f.close()
num = num.replace('\n', '')
prod = 0

for i in range(len(num)-13):
	slice = num[i:i+13]
	slice_prod = 1
	for c in slice:
		slice_prod *= int(c)
	prod = max(prod, slice_prod)
print prod