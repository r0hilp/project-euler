f = open('pe67.txt', 'r')
triangle = []
for line in f:
	row = line.split(' ')
	for i in range(len(row)):
		row[i] = int(row[i])
	triangle.append(row)
f.close()

num_rows = len(triangle)
for i in range(1,num_rows):
	curr_index = num_rows-i-1
	row = triangle[curr_index]
	next_row = triangle[curr_index+1]
	for j in range(len(row)):
		row[j] = row[j] + max(next_row[j],next_row[j+1])

print triangle[0][0]

# ANS: 7273