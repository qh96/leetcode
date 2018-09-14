class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #7,6,4,7,8,5
        pre_ma = ma = 0
        for i in nums:
            pre_ma, ma = ma, max(pre_ma + i, ma)
        return ma
        