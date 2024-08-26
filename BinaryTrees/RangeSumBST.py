from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert_nodes(self, val):
        new_node = TreeNode(val)
        if self.val is None:
            self.val = new_node.val
            return
        current_node = self
        while True:
            if val < current_node.val:
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

    def rangeSumBST(self, root, low, high):
        if root is None:
            return 0
        sum_of_nodes = 0
        if low <= root.val <= high:
            sum_of_nodes += root.val
        sum_of_nodes += self.rangeSumBST(root.left, low, high)
        sum_of_nodes += self.rangeSumBST(root.right, low, high)
        return sum_of_nodes

def preOrderTraversal(root: TreeNode, result: List) -> List:
    if root:
        result.append(root.val)
        preOrderTraversal(root.left, result)
        preOrderTraversal(root.right, result)
    return result

myTree = TreeNode()
values = [2, 12, 3, 14, 6, 7, 8, 10]
for value in values:
    myTree.insert_nodes(value)

node_values = []
node_values = preOrderTraversal(myTree, node_values)
print(node_values)

print(myTree.rangeSumBST(myTree, 3, 14))





