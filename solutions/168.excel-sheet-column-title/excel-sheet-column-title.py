class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 0: return ""
        s = ""
        print(n)
        while n != 0:
            if n%26 != 0:
                s += chr(n%26+64)
            else:
                s += 'Z'
                n -= 26
            n = n // 26
        return s[::-1]
        
        
        