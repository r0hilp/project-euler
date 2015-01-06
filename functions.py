def num_digits(n):
	return len(str(n))

def reverse(str):
	return str[::-1]

def is_palindrome(n):
	str_n = str(n)
	return reverse(str_n) == str(n)

def is_prime(n):
	if(n == 1):
		return False
	for i in range(2, int(n**0.5) + 1):
		if n%i == 0:
			return False
	return True