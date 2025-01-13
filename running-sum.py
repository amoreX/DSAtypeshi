nums=[1,2,3,4]
res=[]
prev=0
for i in nums:
    res.append(i+prev)
    prev+=i
print(res)