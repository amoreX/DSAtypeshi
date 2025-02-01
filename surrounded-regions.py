import collections

board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"],
]

visited = set()
rows, cols = len(board), len(board[0])

island_coords={}
dont_replace_island=[]
islands=0

def bfs(r, c):
    q = collections.deque()
    q.append((r, c))
    visited.add((r, c))
    island_coords[islands]=[]
    island_coords[islands].append((r,c))
    
    if r==rows-1 or r==0 or c==0 or c==cols-1:
        dont_replace_island.append(islands)
    
    while q:
        row, col = q.popleft()

        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        for dr, dc in directions:
            r, c = row + dr, col + dc

            if (
                r in range(rows)
                and c in range(cols)
                and (r,c) not in visited
                and board[r][c]=="O"
            ):
                visited.add((r,c))
                q.append((r,c))
                island_coords[islands].append([r,c])
                
                if r==0 or r==rows-1 or c==0 or c==cols-1:
                    dont_replace_island.append(islands)

for row in range(rows):
    for col in range(cols):
        if (row,col) not in visited and board[row][col]=="O":
            bfs(row,col)
            islands+=1

for island_num in island_coords.keys():
    if island_num not in dont_replace_island:
        coords=island_coords.get(island_num)
        for r,c in coords:
            board[r][c]="X"

print(board)


