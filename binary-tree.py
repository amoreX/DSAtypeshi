from platform import node

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class Binary:
    def __init__(self,root):
        self.root=Node(root)
        self.gn=0

    def display(self):
        
        # In-order: left->Node->right
        
        # def rec(point):
        #     if(point.left):
        #         rec(point.left)
        #         print(point.value)
        #     else:
        #         print(point.value)
        #     if (point.right):
        #         rec(point.right)
        # rec(self.root)
        
        
        # Pre-order: node-> left -> right        
        
        def rec(point):
            print(point.value)
            if(point.left):
                rec(point.left)
            if(point.right):
                rec(point.right)
            else:
                return
        rec(self.root)
        
        
        #Post-order :  left->right->Node        
        
        # def rec(point):
        #     if point:
        #         rec(point.left)
        #         rec(point.right)
        #         print(point.value)
        # rec(self.root)
        
        
        # #Invert
        # def rec(point):
        #     if point is None:
        #         return point
        #     point.left,point.right=point.right,point.left
        #     rec(point.left)
        #     rec(point.right)
        # rec(self.root)
    
    def sorting(self):
    
    
        
        

        
        def depth(point,deep):
            if point is None:
                return 0  # Return 0 for nodes with no children
            return max(depth(point.left, deep + 1), depth(point.right, deep + 1)) +1
            
        k=depth(self.root,0)
        print(k)
        
    def goodnodes(self,point,li):
        if point:
            if point.value>=max(li):
                self.gn+=1
                print(point.value,"is a good node")
            else:
                print(point.value,"is not a good node")
            li.append(point.value)

            p=self.goodnodes(point.left,li)
            li.remove(point.value)
            s=self.goodnodes(point.right,li)
            return max(p,s,self.gn)
        else:
            return 1
    

tr=Binary(3)
tr.root.left=Node(1)
tr.root.left.left=Node(3)
tr.root.right=Node(4)
tr.root.right.left=Node(1)
tr.root.right.right=Node(5)



# tr.display()
l=[]
l.append(tr.root.value)

m=tr.goodnodes(tr.root,l)
print(m)
# tr.maximumdepth()
