class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        l = 0
        r = len(S)-1
        # _max = 1
        ans = []
        while l < len(S):
            _max = l
            while l <= _max:
                if S[r] != S[l]:
                    r -= 1
                else:
                    _max = max(_max, r)
                    r = len(S)-1
                    l += 1
            # l += 1
            ans.append(_max + 1)
        return [ans[0]] + [ans[i]-ans[i-1] for i in range(1, len(ans))]