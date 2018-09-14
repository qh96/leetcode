class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t: 
            return ""
        res = str(t.val)
        if t.left:
            res += '(' + self.tree2str(t.left) + ')'
            if t.right:
                res += '(' + self.tree2str(t.right) + ')'
            
        elif t.right:
            res += '()' + '(' + self.tree2str(t.right) + ')'
        
        return res