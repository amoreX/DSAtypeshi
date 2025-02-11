s="pwwkew"

left,right=0,0
res=""
d={}

result=[]
while right<len(s):
	d[s[right]]=d.get(s[right],0)+1
	p=d.get(s[right])
	
	while p>1:
		d[s[left]]-=1
		res=res[1:]
		left+=1
		p=d.get(s[right])
	res+=s[right]
	right+=1
	result.append(len(res))
	print(res)

print(result)