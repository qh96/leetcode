class Solution:
    def isPrime(self, n):
        return 2 in [n, 2**n%n]
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        count = 0
        for num in range(L, R+1):
            numOfOne = bin(num)[2:].count('1')
            if self.isPrime(numOfOne):
                count += 1
        return count
            