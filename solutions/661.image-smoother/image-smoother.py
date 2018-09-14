class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(M)
        col = len(M[0])
        
        _sum = [[0 for i in range(0, col)] for j in range(0,row)]
        count = [[1 for i in range(0, col)] for j in range(0,row)]
        result = [[0 for i in range(0, col)] for j in range(0,row)]
        
        for i in range(0,row):
            for j in range (0, col):
                _sum[i][j] = M[i][j]

                if (i-1>=0): 
                    _sum[i][j] += M[i-1][j]
                    count[i][j] += 1
                if (i+1<row): 
                    _sum[i][j] += M[i+1][j]
                    count[i][j] += 1
                if (j-1>=0): 
                    _sum[i][j] += M[i][j-1]
                    count[i][j] += 1
                if (j+1<col): 
                    _sum[i][j] += M[i][j+1]
                    count[i][j] += 1
                if (i-1>=0 and j-1>=0): 
                    _sum[i][j] += M[i-1][j-1]
                    count[i][j] += 1
                if (i-1>=0 and j+1 < col): 
                    _sum[i][j] += M[i-1][j+1]
                    count[i][j] += 1
                if (i+1<row and j-1 >=0): 
                    _sum[i][j] += M[i+1][j-1]
                    count[i][j] += 1
                if (i+1<row and j+1<col): 
                    _sum[i][j] += M[i+1][j+1]
                    count[i][j] += 1
        
        for i in range(0,row):
            for j in range(0,col):
                result[i][j] = math.floor(_sum[i][j]/count[i][j])
        
        return result
                
                
        
        