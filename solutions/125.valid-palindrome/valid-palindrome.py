
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub("[^A-Za-z0-9]", "", s.lower())
        for i in range(len(s)//2):
            if s[i] != s[~i]: return False
        return True
