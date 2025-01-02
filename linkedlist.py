def rec(mystring):
    if not mystring:  # Check if mystring is empty
        return ""
    count =0
    res=""
    prev=mystring[0]
    for i in mystring:
        if i==prev:
            count+=1
        else:
            res=res+str(count)+prev
            count=1
            prev=i
    res += str(count) + prev
    return res

n=4
result="1"
for i in range(1,n):
    result=rec(result)

print(result)