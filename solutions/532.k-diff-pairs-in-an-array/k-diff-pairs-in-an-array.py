class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = {}
        if k<0: return 0
        if k == 0:
            for i in nums:
                count[i] = 0
            for i in nums:
                count[i] += 1
            return len([i for i in list(count.values()) if i>1])
        
        set_nums = set(nums)
        for i in range(0,len(nums)):
            nums[i] += k
        set_nums1 = set(nums)
        return len([i for i in set_nums1 if i in set_nums])