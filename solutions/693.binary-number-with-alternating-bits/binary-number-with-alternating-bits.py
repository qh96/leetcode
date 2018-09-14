class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s,t = '',''
        nToBin = bin(n)[2:]
        for i in range(len(nToBin)):
            if i % 2:
                s += '1'
                t += '0'
            else:
                s += '0'
                t += '1'
        return nToBin == s or nToBin == t