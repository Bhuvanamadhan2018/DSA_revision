class TreeNode:
    def __init__(self,val,left=None,Right=None):
        self.val = val
        self.left = None
        self.right = None
    def sameTree(self,p,q)-> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        elif p.val != q.val:
            return False
        return self.sameTree(p.left,q.left) and self.sameTree(p.right,q.right)
        
    
p = TreeNode(4)
p.left =TreeNode(1)   
p.right = TreeNode(5)   

q = TreeNode(5)
q.left =TreeNode(1)   
q.right = TreeNode(7)  

result=p.sameTree(p,q)
print(result)