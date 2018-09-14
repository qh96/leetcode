class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        _sum = big = sum(nums[0:k])
        i = 0
        while i+k<len(nums):
            _sum += nums[i+k]-nums[i]
            big = max(big, _sum)
            i += 1
        return big/k