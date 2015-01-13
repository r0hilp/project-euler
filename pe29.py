power_lst = []
for i in range(2,101):
	for j in range(2, 101):
		power_lst.append(i**j)

print len(set(power_lst))