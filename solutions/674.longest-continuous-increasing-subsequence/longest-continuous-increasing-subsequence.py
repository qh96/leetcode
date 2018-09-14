class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0: return 0
        count = 1
        big = 1
        foo = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > foo:
                foo = nums[i]
                count += 1
                if big<count:
                    big = count
            # elif nums[i] == foo:
            #     count = 1
            #     foo = nums[i]
            else:
                count = 1
                foo = nums[i]
        return big
        