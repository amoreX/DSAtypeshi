class Node:
    def __init__(self,val=0,neighbors=None):
        self.val=val
        self.neighbors=neighbors if neighbors else []

def dfs(node):
    res={}
    if node in res:
        return res[node]

    copy=Node(node.val)
    res[node]=copy
    
    for n in node.neighbors:
        copy.neighbors.append(dfs(n))
    return copy

node=Node(1,[2,4])
print(dfs(node))
