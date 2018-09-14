from itertools import combinations
class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        return [i for i in combinations(range(1,10),k) if sum(i) == n]
        