from typing import List

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_nodes(self,val):
        new_node = TreeNode(val)

        if self.root is None:
            self.root = new_node
            return
        
        current_node = self.root
        while True:
            if val<current_node.val:
                if current_node.left is None:
                    current_node.left = new_node
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    break
                else:
                    current_node = current_node.right

def preOrderTraversal(root:TreeNode,result:List)-> List:
    if root:
        result.append(root.val)
        preOrderTraversal(root.left,result)
        preOrderTraversal(root.right,result)




myTree = BinaryTree()
values = [10,14,5,13,16,7,19,2]
for value in values:
    myTree.insert_nodes(value)  

node_values = []

preOrderTraversal(myTree.root,node_values)
print(node_values)
      