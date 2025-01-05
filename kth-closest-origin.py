import math
import heapq
points = [[1,3],[-2,2]]
k = 1

q=[]
d={}

for p1,p2 in points:
    dist= math.sqrt(math.pow((0-p1),2)+math.pow((0-p2),2))
    d[-dist]=[p1,p2]
    heapq.heappush(q,-dist) if len(q) <k else heapq.heappushpop(q,-dist)
print(q)
res=[]

for i in q:
    res.append(d[i])
print (res)
