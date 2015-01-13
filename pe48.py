# last ten digits of a^b
def last_ten(a,b):
	tot = 1
	while (b > 0):
		tot *= a
		tot = tot%10000000000
		b -= 1
	return tot

print sum([last_ten(x, x) for x in range(1, 1001)])%10000000000

# ANS: 9110846700