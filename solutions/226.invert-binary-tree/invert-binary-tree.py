# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # # preorder
        # if not root: 
        #     return None
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # return root
        
        queue = [root]
        while queue:
            node = queue.pop()
            if node:
                node.left, node.right = node.right, node.left
                queue += node.left, node.right
        return root