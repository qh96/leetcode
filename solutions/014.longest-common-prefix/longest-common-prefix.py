class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        s = ""
        c = 0
        _min = len(strs[0])
        for i in strs:
            _min = min(_min,len(i))
        for i in range(_min):
            for j in strs:
                if strs[0][i] != j[i]:
                    c = i
                    for i in range(c):
                        s += strs[0][i]
                    return s
        for i in strs:
            if len(i) == _min:
                return i
        
        