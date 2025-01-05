nums=[-2,1,-3,4,-1,2,1,-5,4]

res=0
sum=0
negsum=nums[0]

for i in nums:
    if i >0:
        negsum=0
        break
    else:
        negsum=max(i,negsum)

for i in nums:
    sum+=i
    if sum<=0:
        sum=0
    res=max(res,sum)
if negsum!=0:
    print(negsum)
else:
    print(res)