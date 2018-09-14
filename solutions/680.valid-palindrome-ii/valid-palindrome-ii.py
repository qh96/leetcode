class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def is_pan(i,j):
            return all(s[k] == s[j-k+i] for k in range(i,j))
        for i in range(len(s)//2):
            if s[i] != s[~i]:
                j = len(s)-i-1
                return is_pan(i+1,j) or is_pan(i,j-1)
        return True
        