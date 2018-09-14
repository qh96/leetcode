class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        queue = []
        row = len(grid)
        col = len(grid[0])
        count = 0
        visited = [[0 for i in range(col)] for j in range(row)]
        for x in range(row):
            for y in range(col):
                if grid[x][y] == "1" and not visited[x][y]:
                    queue.append((x,y))
                    visited[x][y] = 1
                    count += 1
                    while queue:
                        r,c = queue.pop(0)
                        for (i,j) in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                            if 0 <= i < row and 0 <= j < col:
                                if not visited[i][j] and grid[i][j] == "1":
                                    queue.append((i,j))
                                    visited[i][j] = 1
                    
        return count
                                
                                    
                    
                    
                    