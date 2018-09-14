class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        S = sum(nums)
        l_sum = 0
        for i,x in enumerate(nums):
            if l_sum == S-x-l_sum:
                return i
            else:
                l_sum += x
        return -1