# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [str(root.val)]
            res = [str(root.val) + path for path in helper(root.left)]
            res += [str(root.val) + path for path in helper(root.right)]
            return res
        res = helper(root)
        return sum(map(int, res))
            
            