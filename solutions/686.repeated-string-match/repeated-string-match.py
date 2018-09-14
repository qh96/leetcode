class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        q = math.ceil(len(B)/len(A)) 
        # if q == 0: q = 1
        for i in range(2):
            C = A*(q+i)
            print(C)
            if B in C:
                return q+i
        return -1

        