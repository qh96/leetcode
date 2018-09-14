# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            root = TreeNode(preorder[0])
            mid = inorder.index(preorder.pop(0))
            
            root.left = self.buildTree(preorder, inorder[0:mid])
            root.right = self.buildTree(preorder, inorder[mid+1:])
            return root