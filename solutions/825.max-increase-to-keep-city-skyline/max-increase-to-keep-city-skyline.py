class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        _sum = 0
        for i in range(row):
            for j in range(col):
                gridNew = min(max([x for x in grid[i]]), max([grid[y][j] for y in range(row)]))
                _sum += (gridNew - grid[i][j])
        return _sum