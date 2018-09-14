class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = [0 for i in range(0,len(nums)+1)]
        for i,x in enumerate(nums):
            if x == 0: 
                l[x] = 'x'
            else:
                l[x] = x
        
        for i in l:
            if i == 0:
                return l.index(i)