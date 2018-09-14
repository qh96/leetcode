from itertools import combinations
class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def area(p,q,r):
            return 0.5 * abs(p[0]*q[1]+q[0]*r[1]+r[0]*p[1]-p[0]*r[1]-q[0]*p[1]-r[0]*q[1])

        return max(area(*tri) for tri in itertools.combinations(points,3))
            