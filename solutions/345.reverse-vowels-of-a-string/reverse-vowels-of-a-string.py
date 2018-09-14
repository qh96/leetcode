class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "": return s
        vo = "aeiouAEIOU"
        ls = list(s)
        l,r = 0,len(s)-1
        while True:
            while l<len(s) and ls[l] not in vo: 
                l += 1
            while r>0 and ls[r] not in vo: 
                r -= 1
            if l>=r: break
            ls[l],ls[r] = ls[r],ls[l]
            l += 1
            r -= 1
        return ''.join(ls)