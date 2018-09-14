# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def helper(root, val):
            if not root:
                return []
            if root.val == val:
                return [str(root.val)]
            res = [str(root.val) + '->' + path for path in helper(root.left, val)]
            res += [str(root.val) + '->' + path for path in helper(root.right, val)]
            return res
        def find(root, val):
            if root:
                print(root.val)
                if root.val == val:
                    return root 
                return find(root.left, val) or find(root.right, val)
                
            
        path1,path2 = helper(root, p.val)[0].split('->'), helper(root, q.val)[0].split('->')
        ele = root.val
        for i in path1:
            if i in path2:
                ele = int(i)
        return find(root, ele)
        
            
        