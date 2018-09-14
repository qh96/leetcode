# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
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
                res.append(p.val)
                p = p.left
            else:
                node = stack.pop()
                p = node.right
        return res
            