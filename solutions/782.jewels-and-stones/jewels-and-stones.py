class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        d = {}
        for i in S:
            d[i] = 0
        for i in S:
            d[i] += 1
        _sum = 0
        s = set(S)
        for i in J:
            if i in s:
                _sum += d[i]
        return _sum