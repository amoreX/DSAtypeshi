s="anagram"
t="nagaram"
d1={}
d2={}
for i in s:
    d1[i]=d1.get(i,0)+1
for i in t:
    d2[i]=d2.get(i,0)+1
if d1==d2:
    print(True)  
