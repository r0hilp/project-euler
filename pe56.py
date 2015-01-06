# Problem: Find max digit sum in a^b for 1 <= a,b <= 100

MAX = 100

def digit_sum(n):
	d_sum = 0
	while n > 0:
		d_sum = d_sum + n%10
		n = (n-n%10)/10
	return d_sum

max_sum = 0

for i in range(1, MAX+1):
	for j in range(1, MAX+1):
		d_sum = digit_sum(i**j)
		if(d_sum > max_sum):
			max_sum = d_sum

print max_sum
