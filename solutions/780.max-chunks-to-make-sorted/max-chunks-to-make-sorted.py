class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        #
        ma = 0
        count = 0
        for i in range(0,len(arr)):
            ma = max(ma,arr[i])
            if i == ma: count += 1
        return count 