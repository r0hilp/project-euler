# generates up to LIMIT digits
def champ_gen(LIMIT):
	length = 0
	i = 0
	while(length < LIMIT):
		i += 1
		length += len(str(i))
		yield i

champ = ''.join([str(i) for i in champ_gen(1000000)])
print len(champ)
print champ[999999]
print int(champ[0])*int(champ[9])*int(champ[99])*int(champ[999])*int(champ[9999])*int(champ[99999])
# ANS: 210