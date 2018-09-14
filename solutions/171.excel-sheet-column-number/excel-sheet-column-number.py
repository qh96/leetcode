class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        _sum = 0
        for c,i in enumerate(s):
            _sum += (ord(i)-64) * pow(26,(len(s)-1-c))
        return _sum
        