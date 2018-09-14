# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 想象这个过程
class Solution:
    def binaryTreePaths(self, root):
        
#         #stack
#         stack = [(root, "")] # used for pop()
#         res = []
        
#         if not root:
#             return []
        
#         while stack:
#             node, strr = stack.pop()
#             if not node.left and not node.right:
#                 res.append(strr + str(node.val))
#             if node.left:
#                 stack.append((node.left, strr + str(node.val) + '->'))
#             if node.right:
#                 stack.append((node.right, strr + str(node.val)+ '->' ))
#         return res
        
        #DFS
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        res = [str(root.val) + '->' + path for path in self.binaryTreePaths(root.left)]
        res += [str(root.val) + '->' + path for path in self.binaryTreePaths(root.right)]
        return res
        

        
        
            
        