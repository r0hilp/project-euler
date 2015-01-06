# DP lattice paths pretty much

X = 21
Y = 21
grid = [[0 for j in range(Y)] for i in range(X)]
for i in range(X):
	grid[i][0] = 1
for i in range(Y):
	grid[0][i] = 1
for i in range(1, X+Y-2):
	for x in range(max(1,i-X+1), min(i,X)):
		y = i - x
		print x,y,i
		grid[x][y] = grid[x-1][y] + grid[x][y-1]
		print grid[x][y]

print grid[19][18]+grid[18][19]

# ANS: 3534263800