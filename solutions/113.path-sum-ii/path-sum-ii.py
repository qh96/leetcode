# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, _sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def helper(root):
            
            if not root:
                return []
            if not root.left and not root.right:
                return [str(root.val)]
            res = [str(root.val) + '->' + path for path in helper(root.left)]
            res += [str(root.val) + '->' + path for path in helper(root.right)]
            return res
        
        res = helper(root)
        newres = []
        for i in res:
            l = [int(j) for j in i.split('->')]
            newres.append(l)

        return list(filter(lambda x: sum(x) == _sum, newres))
                