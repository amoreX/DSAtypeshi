# import collections

# rows=3
# cols=7

# res=0


# def bfs(r,c):
# 	global res
# 	q=collections.deque()
# 	q.append((r,c))
# 	while q:
# 		r,c=q.popleft()

# 		if r == rows-1 and c == cols-1:
# 			res += 1
# 			continue

# 		directions=[[0,1],[1,0]]

# 		for dr,dc in directions:
# 			row=r+dr
# 			col=c+dc

# 			if row in range(rows) and col in range(cols) :
# 				q.append((row,col))
				
# bfs(0,0)
# print(res)

# SLOW AS FUCK COZ BFS 


row=3
col=7
mat=[[0 for _ in range(col)] for _ in range(row)]

for i in range(row-1,-1,-1):
	for j in range(col-1,-1,-1):
		if (i+1) in range(row) and (j+1) in range(col):
			mat[i][j]=mat[i+1][j]+mat[i][j+1]
		elif (i+1) not in range (row) and (j+1) not in range(col):
			mat[i][j]=1
		elif (j+1) not in range (col):
			mat[i][j]=mat[i+1][j]+0
		else:
			mat[i][j]=mat[i][j+1]+0
			
print(mat)