grid=[
  [2147483647,       -1,            0,         2147483647],
  [2147483647,   2147483647,   2147483647,        -1],
  [2147483647,       -1,       2147483647,        -1],
  [    0,            -1,       2147483647,      2147483647]
]



rows,cols= len(grid),len(grid[0])

res=[]
visited=set()

def dfs(r,c,counter):
	visited.add((r,c))
	if grid[r][c]== 0:
		res.append(counter)
		return
	directions=[[0,1],[0,-1],[1,0],[-1,0]]
	for dr,dc in directions:
		row,col=r+dr,c+dc
		if row in range(rows) and col in range(cols) and grid[row][col] != -1 and (row,col) not in visited:
			dfs(row,col,counter+1)

for i in range(rows):
	for j in range(cols):
		if grid[i][j]!= -1 and grid[i][j]!= 0:
			dfs(i,j,0)
			grid[i][j]=min(res)
			res=[]
			visited.clear()

print(grid)