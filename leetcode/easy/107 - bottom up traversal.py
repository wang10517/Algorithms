# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        nodes = {}
        result = []

        if root is None:
            return result
        nodes[0] = [root]

        level = 0
        result = []
        while nodes:
            cur_level = nodes.pop(level)
            vals = []
            next_nodes = []
            for node in cur_level:
                vals.append(node.val)
                if not node.left is None:
                    next_nodes.append(node.left)
                if not node.right is None:
                    next_nodes.append(node.right)
            result.append(vals)
            level = level + 1
            if next_nodes:
                nodes[level] = next_nodes
        result.reverse()
        return result
            
            


        