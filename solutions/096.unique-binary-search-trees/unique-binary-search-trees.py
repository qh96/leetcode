class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
    1         3     3      2     1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
   1 n 3 2 n
   3 2 n 1 n
   3 1 n n 2
   2 1 3
   1 n 2 n 3
    dp[5] = dp[0] * dp[4] + dp[1] + dp[3] + dp[2] + dp[2] + dp[3] + dp[1] + dp[4] + dp[0]
    
        """
        dp = [0 for i in range(n+1)]
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            for j in range(i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]
        
        