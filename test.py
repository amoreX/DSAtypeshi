import math
n=153

p=len(str(n))
n=str(n)

s=0
for i in n:
    s+=math.pow(int(i),p)
print(int(s)==int(n))