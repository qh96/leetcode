class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3: 
            return 0
        prime_list = [True] * n
        prime_list[0] = prime_list[1] = False
        for i in range(2,int(n ** 0.5)+1):
            for j in range(i * i, n, i):
                prime_list[j] = False
        return sum(prime_list)