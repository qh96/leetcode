import queue

class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        visit = [[0 for x in range(col)] for y in range(row)]
        q = queue.Queue()
        count = 0
        big = 0
        
        for x in range (0,row):
            for y in range (0,col):
                if(grid[x][y] == 1):
                    q.put({'x':x, 'y':y})
                    visit[x][y] = 1
                    count += 1
                    while (q.empty()==False):
                        r = q.get()
                        # print(r['x'])
                        x,y = r['x'],r['y']
                        print("x:",x,"y:",y)
                        if(x-1>=0 and grid[x-1][y]==1 and visit[x-1][y] !=1 ):
                            visit[x-1][y] = 1
                            count += 1
                            q.put({'x':x-1,'y':y})
                        if(x+1<row and grid[x+1][y]==1 and visit[x+1][y] !=1 ):
                            visit[x+1][y] = 1
                            count += 1
                            q.put({'x':x+1,'y':y})
                        if(y-1>=0 and grid[x][y-1]==1 and visit[x][y-1] !=1 ):
                            visit[x][y-1] = 1
                            count += 1
                            q.put({'x':x,'y':y-1})
                        if(y+1<col and grid[x][y+1]==1 and visit[x][y+1] !=1 ):
                            visit[x][y+1] = 1
                            count += 1
                            q.put({'x':x,'y':y+1})
                        
                    if big<count:
                        big = count
                    count = 0
        return big
        
        
        
        
        