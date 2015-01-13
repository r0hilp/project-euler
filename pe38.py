def pandigital_str(strng):
	return ''.join(sorted(strng)) == "123456789"

LIMIT = 100000
# gets the appropriate candidate string for n < 1000
def get_mults(n):
	strng = ''
	mult = 1
	while(len(strng) < 9):
		strng += str(n*mult)
		mult = mult+1
	return strng

print sorted(get_mults(192))
print max(filter(lambda x: pandigital_str(x), [get_mults(n) for n in range(1, LIMIT)]))
# ANS: 932718654