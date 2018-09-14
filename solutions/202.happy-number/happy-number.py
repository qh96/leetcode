class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        while n not in s:
            s.add(n)
            _sum = 0
            l = [i for i in str(n)]
            for i in l:
                _sum += pow(int(i),2)
            n = _sum
            
            if n in s: return n == 1
        