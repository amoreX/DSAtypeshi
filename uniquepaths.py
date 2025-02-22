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

