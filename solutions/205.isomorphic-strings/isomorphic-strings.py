class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count1 = collections.Counter(s)
        count2 = collections.Counter(t)
        
        l1 = [count1[i] for i in s]
        l2 = [count2[i] for i in t]
        l1.sort()
        l2.sort()
        
        if l1 != l2:
            return False
            
        _set = set()
        d = {}
        for i in range(len(t)):
            if s[i] in d:
                diff = ord(s[i]) - ord(t[i])
                if diff != d[s[i]]:
                    return False
            d[s[i]] = ord(s[i]) - ord(t[i])
        return True
        