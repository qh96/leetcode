import collections
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == []: return False
        if len(nums)!=len(set(nums)):
            return True
        return False
        