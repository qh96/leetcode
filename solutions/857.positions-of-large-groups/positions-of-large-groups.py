class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        S += '0'
        l = 0
        r = 0
        ans = []
        while r < len(S):
            if S[r] == S[l]:
                r += 1
            else:
                if r - l >= 3:
                    ans.append([l, r - 1])
                l = r
                r += 1
        return ans