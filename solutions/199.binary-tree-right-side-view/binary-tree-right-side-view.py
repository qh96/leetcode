# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = [root]
        ans = []
        while queue:
            values = [i.val for i in queue if i]
            if values:
                ans.append(values[-1])
            queue = [child for i in queue if i for child in (i.left, i.right)]
        return ans
        

        