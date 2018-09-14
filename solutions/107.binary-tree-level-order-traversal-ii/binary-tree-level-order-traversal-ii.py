# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        l = [[root]]
        for level in l:
            temp = []
            for node in level:
                if node.left: temp.append(node.left)
                if node.right: temp.append(node.right)
            if temp:
                l.append(temp)
        return [[node.val for node in level]for level in l][::-1]
                
            