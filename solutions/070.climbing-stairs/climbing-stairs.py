class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        pre,cur = 1,2
        if n == 1: return 1
        if n == 2: return 2
        for i in range(2,n):
            i = pre + cur
            pre,cur = cur,i
        return i