denoms = {0:1, 1:2, 2:5, 3:10, 4:20, 5:50, 6:100, 7:200}
MAX = 200

dp_array = [[0 for y in denoms.keys()] for x in range(MAX)]
dp_array[0] = [1 if x == 0 else 0 for x in denoms.keys()]
for i in range(1,MAX):
	for j in dp_array[i]:
		dp_array[i][j] = sum([dp_array[i-denoms[k]][j] for k in filter(lambda x: i - denoms[x] >= 0, range(j))])

print dp_array[199]