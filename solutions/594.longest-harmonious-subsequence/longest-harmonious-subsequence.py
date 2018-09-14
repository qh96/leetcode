class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.Counter(nums)
        return max([count[i]+count[i+1] for i in count if count[i+1]] or [0])
        # for i in range(len(count.keys())-1):
        #     _max = max(count.keys()[i] + count.keys()[i+1], _max)
        
        # return _max
        # for x in count:
        #     if count[x+1]:
        #         print(count[x] + count[x+1])

        # print([count[x] + count[x+1] for x in count if count[x+1]])