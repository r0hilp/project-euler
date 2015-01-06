f = open('pe8.txt', 'r')
num = ''
for line in f:
	num += line
f.close()
num = num.replace('\n', '')
prod = 0

for i in range(len(num)-4):
	slice = num[i:i+5]
	prod = max(prod, int(slice[0])*int(slice[1])*int(slice[2])*int(slice[3])*int(slice[4]))
print prod