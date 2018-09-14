# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = [root]
        ans = []
        count = 0
        while queue:
            values = [i.val for i in queue if i]
            if values:
                if count % 2:
                    ans.append(values[::-1])
                else:
                    ans.append(values)
            queue = [child for i in queue if i for child in (i.left, i.right)]
            count += 1
        return ans