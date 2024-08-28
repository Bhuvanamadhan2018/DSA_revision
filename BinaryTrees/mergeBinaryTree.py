class TreeNode:
    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right = None
    def mergeTrees(self,root1,root2):
        if not root1:
            return root2
        elif not root2:
            return root1
        
        merged_tree = TreeNode(root1.val + root2.val)
        merged_tree.left = self.mergeTrees(root1.left,root2.left)
        merged_tree.right = self.mergeTrees(root1.right,root2.right)
        return merged_tree
    def printTree(self, node, level=0):
            if node is not None:
                self.printTree(node.right, level + 1)
                print(' ' * 4 * level + '->', node.val)
                self.printTree(node.left, level + 1)

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.right = TreeNode(4)
root1.right.left = TreeNode(6)

root2 = TreeNode(6)
root2.left = TreeNode(7)
root2.right = TreeNode(8)
root2.left.right = TreeNode(3)
root2.right.left = TreeNode(10)

result = TreeNode(0).mergeTrees(root1,root2)
TreeNode(0).printTree(result)
