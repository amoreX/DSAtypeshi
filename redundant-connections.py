# edges = [[1,2],[1,3],[2,3]]
edges=[[3,4],[1,2],[2,4],[3,5],[2,5]]

parent=[i for i in range(len(edges)+1)]
rank=[1]*(len(edges)+1)

def find(n):
    p=parent[n]
    
    while p!=parent[p]:
        parent[p]=parent[parent[p]] #idk man , makes shit faster by compressing path
        p=parent[p]
    return p

def union(n1,n2):
    p1,p2=find(n1),find(n2)
    
    if p1==p2:
        return False
    if rank[p1]>rank[p2]:
        parent[p2]=p1
        rank[p1]+=1
    else:
        parent[p1]=p2
        rank[p2]+=1
    return True
res=[]
for start,end in edges:
    if not union(start,end):
        res.append([start,end])
print(res)