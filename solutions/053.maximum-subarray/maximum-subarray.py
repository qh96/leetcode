class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #[-2,1,-3,4,-1,2,1,-5,4]
        temp = _max = nums[0]
        
        for i in nums[1:]:
            temp = max(temp+i, i)
            _max = max(_max, temp)
        
        return _max
                
        
        