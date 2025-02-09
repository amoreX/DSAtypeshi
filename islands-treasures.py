import collections
grid=[
  [2147483647,       -1,            0,         2147483647],
  [2147483647,   2147483647,   2147483647,        -1],
  [2147483647,       -1,       2147483647,        -1],
  [    0,            -1,       2147483647,      2147483647]
]

rows,cols=len(grid),len(grid[0])

#append all locations of treasures to queue
q=collections.deque()
for i in range(rows):
	for j in range(cols):
		if grid[i][j]==0:
			q.append((i,j,0))

#run bfs on queue, because all treasures are appended one after another so it will go from treasure to treasure ensuring every cell is updated with the shorted distance 

directions =[[0,1],[1,0],[0,-1],[-1,0]]
while q:
	r,c,dist=q.popleft()
	for dr,dc in directions:
		row,col=r+dr,c+dc

		if row in range(rows) and col in range(cols) and grid[row][col]== 2147483647:
			grid[row][col]=dist+1
			q.append((row,col,dist+1))

print(grid)