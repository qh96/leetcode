class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        L = []
        for i in range(0,rowIndex+1):
            l = [0 for i in range(0,i+1)]
            l[0] = l[i] = 1
            for j in range(1,i):
                if i-1>=0 and j-1 >=0:
                    l[j] = L[j-1] + L[j]
            L = l
        return l