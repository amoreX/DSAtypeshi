strs=["flower","flow","flight","fling","flirt"]
shortest=min(strs,key=len)
# print(shortest[:1])
for i in strs:
	p=shortest
	k=1
	while i[:k]==p[:k] and k<len(p):
		k+=1
	if i[k-1]!=p[k-1]:
		k-=1
	shortest=shortest[:k]
print(shortest)