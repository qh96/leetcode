import heapq
class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)==1): return 0
        r = heapq.nlargest(2,nums)
        print(r)
        if r[0]/2 >= r[1]:
            return nums.index(r[0])
        else: return -1