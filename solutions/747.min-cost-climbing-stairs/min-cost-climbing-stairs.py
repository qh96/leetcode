class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        #这个算法相当于每次更新min1
        f1 = f2 = 0
        for i in range(0,len(cost)):
            f1, f2 = f2, min(f1,f2)+cost[i]
        return min(f1,f2)
        
                    


            
        