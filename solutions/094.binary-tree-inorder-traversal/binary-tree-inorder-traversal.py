# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        p = root
        while stack or p:
            if p:
                stack.append(p)
                p = p.left
            else:
                node = stack.pop()
                res.append(node.val)
                p = node.right
        return res
            