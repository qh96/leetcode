class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        L = []
        if not numRows: return []
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1],[1,1]]
        for i in range(0,numRows):
            l = [0 for i in range(0,i+1)]
            l[0] = l[i] = 1
            for j in range(1,i):
                if i-1>=0 and j-1 >=0:
                    l[j] = L[i-1][j-1] + L[i-1][j]
            L.append(l)
        return L