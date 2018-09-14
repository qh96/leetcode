import collections
class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left,right,count = {},{},{}
        for i, x in enumerate(nums):
            if x not in left: 
                left[x] = i
            right[x] = i
            count[x] = count.get(x,0) + 1 
        
        big = max(count.values())
        
        s = len(nums)
        
        for i in count:
            if count[i] == big:
                r = right[i]-left[i]+1
                if s > r:
                    s = r
                    
        return s

            
            
            
        