from functools import reduce
class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """       
        if num <= 0: return False
        return sum(set(reduce(list.__add__, ([i, num//i] for i in range(1, int(pow(num, 0.5) + 1)) if num % i == 0))))-num == num
        
        
        
        