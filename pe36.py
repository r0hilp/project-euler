# is base 2 palindrome
def bin_palindrome(n):
	binary = bin(n)[2:]
	return binary == binary[::-1]

def is_palindrome(n):
	return str(n) == str(n)[::-1]

lst = filter(lambda n: bin_palindrome(n) and is_palindrome(n), range(1, 1000000))
print lst, sum(lst)
# ANS: 872187
