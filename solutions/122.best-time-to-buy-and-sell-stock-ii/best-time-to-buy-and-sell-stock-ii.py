class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #[7, 1, 5, 3, 6, 4]
        if len(prices) == 0: return 0
        if len(prices) == 1: return 0
        if len(prices) == 2: return max(prices[1]-prices[0],0)
        _sum = 0
        for i in range(0,len(prices)):
            if i+1<len(prices):
                diff = prices[i+1]-prices[i]
                if diff > 0:
                    _sum += diff
        

        return max(_sum,0)