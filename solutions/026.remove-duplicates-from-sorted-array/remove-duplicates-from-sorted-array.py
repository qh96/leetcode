class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        nums.append('x')
        while i+1<len(nums)-1 and nums[i+1]!='x':
            flag = nums[i]
            if nums[i+1] == nums[i]:
                i += 1
                while nums[i] == flag:
                    nums.pop(i)
            else:
                i += 1
            
                
        nums.pop(len(nums)-1)
        return len(nums)
            