class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l,r,res = 0,x,0
        while l <= r:
            m = l + (r-l)//2
            if m * m <= x:
                res = m
                l = m + 1
            else:
                r = m - 1
        return res
            
                