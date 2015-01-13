from fractions import gcd

def is_digit_cancelling(num, denom):
	common_div = gcd(num,denom)
	# whether common digit is of the form ab/bc (top) or ab/ca (bottom)
	top = (num%10 == denom/10)
	bottom = (num/10 == denom%10)
	if(top and (not bottom)):
		new_num = num/10
		new_denom = denom%10
		return new_denom != 0 and float(num)/denom == float(new_num)/new_denom
	elif (bottom and (not top)):
		new_num = num%10
		new_denom = denom/10
		return new_denom != 0 and float(num)/denom == float(new_num)/new_denom
	else:
		return False

for denom in range(10, 100):
	for num in range(10, denom):
		if is_digit_cancelling(num, denom):
			print num,denom

print 64*65*95*98/gcd(16*26*19*49, 64*65*95*98)

# Numbers: 16/64, 26/65, 19/95, 49/98
# ANS: 100

