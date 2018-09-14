# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, node):
        return 0 if not node else max(self.maxDepth(node.left), self.maxDepth(node.right)) + 1
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #
        if not root:
            return True
        leftD = self.maxDepth(root.left)
        rightD = self.maxDepth(root.right)
        if abs(leftD - rightD) > 1:
        
            return False
        return True if self.isBalanced(root.left) and self.isBalanced(root.right) else False

        