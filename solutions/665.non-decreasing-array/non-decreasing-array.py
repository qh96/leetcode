class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==1: return True
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
        
                if i-2>=0 and nums[i-2]>=nums[i]:
                    nums[i] = nums[i-1]
                else:
                    nums[i-1] = nums[i]
                break
        print(nums)
        for i in range(0,len(nums)):
            if i+1<len(nums):
                if  nums[i]>nums[i+1]:
                    return False
            
        return True