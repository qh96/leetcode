# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        l = []
        def preOrder(root):
            if root:
                
                preOrder(root.left)
                l.append(root.val)
                preOrder(root.right)
        preOrder(root)
        print(l)
        return all(l[i-1] < l[i] for i in range(1, len(l)))
            