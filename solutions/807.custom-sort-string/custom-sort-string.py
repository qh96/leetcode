class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        d = {}
        set_S = set(S)
        ans = ''
        for i in T:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        # print(d)
        for i in S:
            if i in d:
                for _ in range(d[i]):
                    ans += i
        for i in T:
            if i not in set_S:
                ans += i
        return ans