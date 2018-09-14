# from itertools import combinations
class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        # def func(p,q,c):
        #     return p * p + q * q == c 
        # if c < 0: return False
        # return any(func(*combi,c) for combi in itertools.combinations_with_replacement([i for i in range(int(pow(c,0.5))+1)], 2))
        # if c < 0: return False
        def is_Square(n):
            return int((n**.5))**2 == n
        return any(is_Square(c-a**2) for a in range(int(c**.5)+1))

        
        
        

            