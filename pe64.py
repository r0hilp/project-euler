from fractions import gcd

def get_period(n):
	convergents = []
	# (a, b, c) represents (a*sqrt(n) + b)/c
	# 1/[(a*sqrt(n) + b)/c - f] = c/(a*sqrt(n)+b-f*c)
	# Simplifies to c*(a*sqrt(n)-b+f*c)/(a^2*n-(b-f*c)^2)
	# = (a*c*sqrt(n) - b*c - f*c^2)/(a^2*n - (b-f*c)^2)
	curr = n**0.5
	convergents.append((1,0,1))
	for i in range(10):
		floor = int(curr)
		curr = 1.0/(curr - floor)
		last_tup = convergents[len(convergents)-1]
		a = last_tup[0]*last_tup[2]
		b = -1*last_tup[1]*last_tup[2] - floor*(last_tup[2]**2)
		c = last_tup[0]**2 * n - (last_tup[1]-floor*last_tup[2])**2
		factor = gcd(gcd(a,b),c)
		a, b, c = a/factor, b/factor, c/factor
		convergents.append((a,b,c))
	print convergents

get_period(2)