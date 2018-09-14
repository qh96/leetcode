# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        def preOrder(root):
            if root:
                res.append(root.val)
                preOrder(root.left)
                preOrder(root.right)
        preOrder(root)
        s = list(set(res))
        s.sort()
        return s[1] if len(s) > 1 else -1