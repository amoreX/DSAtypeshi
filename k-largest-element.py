import heapq

class main:
    def __init__(self,k,datalist):
        self.k=k
        self.data=[]
        for i in datalist:
            self.add(i)
    def add(self,val):
        heapq.heappush(self.data,val) if len(self.data) <self.k  else heapq.heappushpop(self.data,val)
        print(self.data[0])

nums=[10,20,30]
p=main(2,nums)
p.add(40)
p.add(100)