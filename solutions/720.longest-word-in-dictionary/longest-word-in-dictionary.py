class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        s = set(words)
        ans = []
        for i in words:
            a = itertools.accumulate(list(i))
            if all(j in s for j in a):
                ans.append(i)
        ans.sort()
        return max(ans, key = len)
                