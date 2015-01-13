# letters in each digit
digits = {0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4}
# letters in each special tens
tens = {10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8, \
		20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6}


# number of letters for num < 1000
def num_letter_count(num):
	hundreds_digit = num/100
	last_two = num%100
	tens_digit = last_two/10
	total = 0
	if(last_two == 0):
		total += digits[hundreds_digit] + 7
		return total
	if(hundreds_digit > 0):
		# [digit] hundred and ...
		total += digits[hundreds_digit] + 10
	if(last_two in tens):
		total += tens[last_two]
		return total
	else:
		if(tens_digit > 0):
			total += tens[tens_digit*10]
		total += digits[num%10]
		return total

print sum([num_letter_count(num) for num in range(1,1000)]) + len('onethousand')
# ANS: 21124