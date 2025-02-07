class TreeNode:
    def __init__ (self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right




t=TreeNode(3)
t.left=TreeNode(2)
t.right=TreeNode(2)
t.left.left=TreeNode(3)
t.left.right=TreeNode(3)
t.left.left.left=TreeNode(4)
t.left.left.right=TreeNode(4)

def height(node,h):
    if node:
        return max(height(node.left,h+1),height(node.right,h+1))
    else:
        return h-1

def rec(node):
    if node:
        if abs(height(node.left,1)-height(node.right,1))>1:
            return False
        return rec(node.left) and rec(node.right) and True
k=rec(t)
print(k)
# print(height(t.left,1))
# print(height(t.right,1))