import collections

edge = [[1, 1, 0], [0, 1, 0], [1, 0, 1]]

visited = set()

rows, cols = len(edge), len(edge[0])


def bfs(r, c):
    q = collections.deque()
    q.append((r, c))
    visited.add((r, c))

    while q:
        row, col = q.popleft()

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for dr, dc in directions:
            r, c = row + dr, col + dc


            if (
                r in range(rows)
                and c in range(cols)
                and (r, c) not in visited
                and edge[r][c] == 1
            ):
                visited.add((r, c))
                q.append((r, c))


islands = 0
for row in range(rows):
    for col in range(cols):
        if (row,col) not in visited and edge[row][col] == 1:
            bfs(row, col)
            islands += 1

print(islands)
