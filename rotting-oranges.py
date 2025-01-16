import collections
grid = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]

visited=set()
global minutes
minutes=0
rows,cols=len(grid),len(grid[0])
global fresh_oranges
fresh_oranges=0
rotten_oranges=[]
for row in range(rows):
    for col in range(cols):
        if grid[row][col]==2:
            rotten_oranges.append((row,col))
        if grid[row][col]==1:
            fresh_oranges+=1

def rec(r,c):
    global fresh_oranges
    global minutes
    q = collections.deque()
    q.append((r,c))
    visited.add((r,c))
    
    while q:
        level_size = len(q)  # Process all oranges at current minute
        for _ in range(level_size):  # Process all oranges at current level
            r,c = q.popleft()
            directions = [(0,1),(1,0),(-1,0),(0,-1)]
            for dr,dc in directions:
                row,col = r+dr,c+dc
                
                if row in range(rows) and col in range(cols) and (row,col) not in visited and grid[row][col]==1:
                    q.append((row,col))
                    visited.add((row,col))
                    grid[row][col]=2
                    fresh_oranges-=1
        
        if q:  # Only increment minutes if there are more oranges to process
            minutes+=1
        print(grid)
        if fresh_oranges==0:
            print(minutes)
            return

for r,c in rotten_oranges:
    if (r,c) not in visited:
        rec(r,c)

if fresh_oranges>0:
    print(-1)
