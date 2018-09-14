# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # stack = [(root, "")]
        # res = []
        # if not root:
        #     return False
        # while stack:
        #     node, strr = stack.pop()
        #     if not node.left and not node.right:
        #         path = strr + str(node.val)
        #         temp = path.split('->')
        #         res.append(sum([int(i) for i in temp]))
        #     if node.left:
        #         stack.append((node.left, strr + str(node.val) + '->'))
        #     if node.right:
        #         stack.append((node.right, strr + str(node.val) + '->'))
        # return _sum in res
        
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        sum -= root.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
        
        
        