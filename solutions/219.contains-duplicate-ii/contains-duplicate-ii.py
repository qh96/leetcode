class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums)==0 or len(nums)==1: return False
        dict1,count = {},{}
        for i in nums:
            count[i] = 0
        diff = 0
        for c,i in enumerate(nums):
            count[i] += 1
            if count[i] >= 2:
                diff = c-dict1[i]
                dict1[i] = c
                if diff <= k:
                    return True
            else:
                dict1[i] = c
        return False