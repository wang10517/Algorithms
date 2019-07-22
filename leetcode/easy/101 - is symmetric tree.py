# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # first present a recursive solution
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        return self.isSameOppositeTree(root.left,root.right)
        
    def isSameOppositeTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and not q is None or q is None and not p is None:
            return False
        elif p is None and q is None:
            return True
        else:
            if p.val != q.val:
                return False
            
            return self.isSameOppositeTree(p.left,q.right) and self.isSameOppositeTree(p.right, q.left)

    # iteratve approach similar to BFS
        
        
        

                
