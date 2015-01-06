# Layers = (Sidelength + 1)/2
# Upper right diagonal: 1, 3, 13, 31, 56 for side lengths 1, 3, 5, 7, 9. PDs are 2 + 8*(layer-2)
# Upper left diagonal: 1, 5, 17, 37, 64 for sl 1,3,5,7,9. PDs are 4 + 8*(layer-2)
# Lower left diagonal: 1, 7, 21, 43, 73 for sl 1,3,5,7,9. PDs are 6 + 8*(layer-2)

UR_LIST = [1]
UL_LIST = [1]
LL_LIST = [1]


def UR_to_n(n):
	prev_list = [1]
	for i in range(2,n+1):
		prev_list.append(prev_list[len(prev_list)-1] + 2 + 8*(i-2))
	return prev_list

def UL_to_n(n):
	prev_list = [1]
	for i in range(2,n+1):
		prev_list.append(prev_list[len(prev_list)-1] + 4 + 8*(i-2))
	return prev_list

def LL_to_n(n):
	prev_list = [1]
	for i in range(2,n+1):
		prev_list.append(prev_list[len(prev_list)-1] + 6 + 8*(i-2))
	return prev_list

def is_prime(n):
	if(n == 1):
		return False
	for i in range(2, int(n**0.5) + 1):
		if n%i == 0:
			return False
	return True

THE_LIST = [1]
num_prime = 0
layers = 1
proportion = 1.0
while proportion >= 0.1:
	layers = layers+1
	UR = UR_LIST[len(UR_LIST)-1] + 2 + 8*(layers-2)
	UL = UL_LIST[len(UL_LIST)-1] + 4 + 8*(layers-2)
	LL = LL_LIST[len(LL_LIST)-1] + 6 + 8*(layers-2)
	UR_LIST.append(UR)
	UL_LIST.append(UL)
	LL_LIST.append(LL)
	THE_LIST.append([UR,UL,LL])
	num_prime += sum([1 if is_prime(x) else 0 for x in [UR, UL, LL]])
	proportion = num_prime/float(4*(layers-1)+1)

print 2*layers-1