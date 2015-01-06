def reverse(str):
	return str[::-1]

def is_palindrome(n):
	str_n = str(n)
	return reverse(str_n) == str(n)

def is_lychrel(n):
	temp = n
	for i in range(50):
		temp = temp + int(reverse(str(temp)))
		if(is_palindrome(temp)):
			return False
	return True

"""
def lychrel_to_n(n):
	# tracks number of iterations until i becomes a palindrome
	lychrel_nums = [0 if is_palindrome(i) else -1 for i in range(n)]
	# loop to mark numbers with lychrel num i in [1,50]
	for i in range(1,50):
		for num in range(1, n+1):
			if(lychrel_nums[num-1] > -1):
				continue
			else:
				mod_num = num + int(reverse(str(num)))
				if(lychel_nums[mod_num] == i-1):
					lychrel_nums[num-1] = i
				continue
	print lychrel_nums
"""

print sum([1 if is_lychrel(i) else 0 for i in range(1, 10001)])