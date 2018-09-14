# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            root = TreeNode(postorder[-1])
            mid = inorder.index(postorder.pop())
            
            root.right = self.buildTree(inorder[mid+1:], postorder)
            root.left = self.buildTree(inorder[0:mid],postorder)
            return root
            
       