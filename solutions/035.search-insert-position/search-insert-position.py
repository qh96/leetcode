class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        if target<nums[0]: return 0
        if target>nums[len(nums)-1]: return len(nums)
        while l<=r:
            m = math.floor((l+r)/2)
            if target<=nums[m]:
                r = m-1
            else:
                l = m+1
        return l
        print(l)
        print(r)
        print(m)
            
        
        
                