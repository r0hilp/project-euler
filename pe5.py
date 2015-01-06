from fractions import gcd

def lcm(x,y):
	return x*y/gcd(x,y)

MAX = 20
LCM = 1
for i in range(1,MAX+1):
	LCM = lcm(LCM, i)

print LCM 