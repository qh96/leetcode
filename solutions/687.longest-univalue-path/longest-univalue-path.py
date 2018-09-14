# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#  https://www.youtube.com/watch?v=FXEsL2DXBKw

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def calculate(node): # 这个函数的作用就是返回一边子树的最长路径
            if not node:
                return 0
            leftCount = calculate(node.left)
            rightCount = calculate(node.right)
            #-----#
            #下面这部分就是作为判断那三种情况的
            left = leftCount + 1 if node.left and node.left.val == node.val else 0
            right = rightCount + 1 if node.right and node.right.val == node.val else 0
            self.res = max(self.res, left + right)
            #-----#
            return max(left, right)
        calculate(root)
        return self.res
            