class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r,l = 0,1
        _min,_max = nums[len(nums)-1], nums[0]
        for i in range(1,len(nums)):
            _min = min(_min, nums[len(nums)-i-1])
            _max = max(_max, nums[i])
            if nums[i]<_max: r = i
            if nums[len(nums)-i-1]>_min: l = len(nums)-i-1
        return r-l+1
                        
        