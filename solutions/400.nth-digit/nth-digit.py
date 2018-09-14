class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0: return 0
        leng = 1
        start = 1
        count = 9
        while n > leng*count:
            n -= leng*count
            leng += 1
            start *= 10
            count *= 10
        start += (n-1) //leng 
        return int(str(start)[(n-1)%leng])