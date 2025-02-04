edge={}
visited=set()
n=5 # number of edges
def dfs(node,parent):
    visited.add(node)
    
    for neighbour in edge[node]:
        if neighbour not in visited:
            if dfs(neighbour,node):
                return True #cycle found
        elif neighbour != parent:
            return True # cycle found
    return False

if dfs(0,-1):
    print(False) # not a valid Tree

print(len(visited)==n) # for all nodes to be visited condition