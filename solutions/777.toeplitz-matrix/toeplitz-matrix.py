class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        matrix1 = [[]]
        row = len(matrix)
        col = len(matrix[0])
        matrix1 = [[0 for x in range(col)] for y in range(row)]
        print (matrix1)
        i = 0
        j = 0
        # print (matrix)
        for j in range(0,col):
            temp = matrix[0][j]
            x,y = 0,j
            count = 0
            while x < row and y < col:
                x += 1
                y += 1
                count += 1
            a,b = i,j
            for x in range(0,count):
                matrix1[a][b] = temp
                a += 1
                b += 1
        print (matrix)
        i = 0
        j = 0         
        for i in range(1,row):
            temp = matrix[i][0]
            x,y = i,0
            count = 0
            while x < row and y < col:
                x += 1
                y += 1
                count += 1
            a,b = i,j
            for x in range(0,count):
                matrix1[a][b] = temp
                a += 1
                b += 1
        print (matrix)
        if matrix1 == matrix:
            return True
        return False
                
         