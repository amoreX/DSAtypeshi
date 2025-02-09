s="paypalishiring"
rows=3

res=[[] for _ in range (rows)]

flag=True # True -> going down , False -> going up 

counter=0
for i in s:
	if flag:
		res[counter].append(i)
		if counter+1 == 3 :
			flag= False
			counter-=1
		else:
			counter+=1
	else:
		res[counter].append(i)
		if counter -1 == -1:
			flag = True
			counter+=1
		else:
			counter-=1
	print(res)

print(res)