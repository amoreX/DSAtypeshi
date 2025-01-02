
nums=[4,2,1,2,1]
p={}
for i in nums:
    p[i]=p.get(i,0)+1
print(p)
for keys in p.keys():
    if p[keys]==1:
        print(keys)