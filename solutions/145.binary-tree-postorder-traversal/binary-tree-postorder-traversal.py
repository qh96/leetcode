# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
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
                p = p.right
            else:
                node = stack.pop()
                p = node.left

        return res[::-1]