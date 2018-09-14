# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.res = float('inf')
        self.helper(root, 1)
        return self.res
    
    def helper(self, root, depth):
            if root.left:
                self.helper(root.left, depth + 1)
            if root.right:
                self.helper(root.right, depth + 1)
            if not root.left and not root.right:
                self.res = min(depth, self.res)
                
                
                
                
                