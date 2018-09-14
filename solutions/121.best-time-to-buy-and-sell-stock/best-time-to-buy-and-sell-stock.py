class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        su = 0
        ma = 0
        for i in range(1,len(prices)):
            su = max(0,su + prices[i] - prices[i-1])
            ma = max(su,ma)
            print("su",su)
            print("ma",ma)
        return ma
            