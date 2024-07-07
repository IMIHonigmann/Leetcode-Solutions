# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        
        def dia(node: Optional[TreeNode]) -> int:
            nonlocal diameter
            if not node:
                return 0

            # Recursive DFS to do the operations for each node
            ln = dia(node.left)
            rn = dia(node.right)

            # find the diameter of each node on traversal
            # if the current diameter is bigger than the last max found diameter then overwrite the max found diameter with the current one
            diameter = max(diameter, ln + rn)

            return 1 + max(ln, rn)

        dia(root)
        return diameter
