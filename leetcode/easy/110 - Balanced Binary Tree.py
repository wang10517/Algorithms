# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1 and self.isBalanced(root.right) and self.isBalanced(root.left)

    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1+ max(self.maxDepth(root.left) , self.maxDepth(root.right))         