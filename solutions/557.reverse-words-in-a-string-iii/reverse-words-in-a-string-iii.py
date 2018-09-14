class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "": return s
        i = j = 0
        s = s + ' '
        sn = ""
        while i<len(s):
            if j >= len(s): break
            while s[j] != ' ': j += 1
            if i == 0:
                sn += s[j-1::-1]
            else:
                sn += s[j:i:-1]
            i = j
            j += 1

        return sn