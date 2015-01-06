def is_palindrome(n):
	return str(n)[::-1] == str(n)

MIN = 100
MAX = 999
pals = []

for i in range(MIN, MAX+1):
	for j in range(MIN, MAX+1):
		prod = i*j
		if is_palindrome(prod):
			pals.append(prod)

print max(pals)