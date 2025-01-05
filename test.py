def solve(s1, s2):
    s1=sorted(s1)
    s2=sorted(s2)
    j=0
    for i in range(len(s1)):
        if j <len(s2):
            if s1[i]!=s2[j]:
                print("False")
                break
            j+=1

solve("silent","listenm")