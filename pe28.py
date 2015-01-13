# SL = 2*layer - 1
# layer sum = SL^2 + SL^2 - SL + 1 + SL^2 - 2*SL + 2 + SL^2 - 3*SL + 3 = 4SL^2 - 6SL + 6

def corner_sum(layer):
	SL = 2*layer - 1
	return 4*SL*SL - 6*SL + 6

print sum([corner_sum(layer) for layer in range(2, 502)]) + 1
# ANS: 669171001