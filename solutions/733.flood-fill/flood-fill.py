class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        stack = [(sr,sc)]
        color = image[sr][sc]
        row,col = len(image), len(image[0])
        visited = [[False for i in range(col)] for j in range(row)]
        while stack:
            # p = stack.pop()
            # r,c = p[0], p[1]
            r,c = stack.pop()
            visited[r][c] = True
            image[r][c] = newColor
            for (ir,ic) in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= ir < row and 0 <= ic < col:
                    if image[ir][ic] == color and not visited[ir][ic]:
                        stack.append((ir,ic))
        return image