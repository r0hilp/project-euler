# factorial
def fact(n):
	if (n == 1 or n == 0):
		return 1
	else:
		return n*fact(n-1)

# list of digit factorials
fact_list = [fact(n) for n in range(10)]

# sum of factorials of digits
def d_fact_sum(n):
	total = 0
	while (n != 0):
		last = n%10
		total += fact_list[last]
		n = (n-last)/10
	return total

working_lst = []
# upper bound is < 10^7
for i in range(10, 10000000):
	result = d_fact_sum(i)
	if result == i:
		working_lst.append(i)
print working_lst, sum(working_lst)

# ANS: 40730 (145 + 40585)