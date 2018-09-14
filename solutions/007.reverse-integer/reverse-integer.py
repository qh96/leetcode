class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            n = int(str(x)[::-1])
            return n if n < 2 ** 31 else 0
        else:
            n = int('-' + str(x)[:0:-1])
            return n if n > -2 ** 31 else 0
            
            
            
        