# import collections
# heights = [
#     [1, 2, 2, 3, 5],
#     [3, 2, 3, 4, 4],
#     [2, 4, 5, 3, 1],
#     [6, 7, 1, 4, 5],
#     [5, 1, 1, 2, 4],
# ]

# rows,cols=len(heights),len(heights[0])

# def bfs(r,c):
#     if (r==0 or c==0) and (r==rows-1 or c==cols-1):
#         return True
    
#     pacific=1   #not reached
#     atlantic=1  #not reached
    
#     q=collections.deque()
#     q.append((r,c))
    
#     visited=set()
#     visited.add((r,c))
    
#     while q:
#         row,col=q.popleft()
        
#         directions=[[0,1],[1,0],[0,-1],[-1,0]]
#         for dr,dc in directions:
#             r=row+dr
#             c=col+dc
            
#             if r in range(rows) and c in range(cols) and heights[r][c]<=heights[row][col] and (r,c) not in visited:
#                 q.append((r,c))
#                 visited.add((r,c))
#                 if r==0 or c==0:
#                     pacific=0 #pacific reached
#                 if r==rows-1 or c ==cols-1:
#                     atlantic=0 #atlantic reached
#     if pacific ==0 and atlantic ==0:
#         return True
#     return False

# k=bfs(4,3)
# print(k)

nums=[4,2,1,2,1]
p={}
for i in nums:
    p[i]=p.get(i,0)+1
print(p)
for keys in p.keys():
    if p[keys]==1:
        print(keys)