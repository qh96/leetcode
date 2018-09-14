class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # multi = 1
        # l = []
        # flag = 0
        # set_nums = set(nums)
        # if 0 in set_nums: flag = 1
        # for i in nums:
        #     if i != 0:
        #         multi *= i
        # for i in nums:
        #     if flag == 1:
        #         if i == 0:
        #             l.append(multi)
        #         else:
        #             l.append(0)
        #     else:
        #         l.append(multi/i)
        # return l
    
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output
        