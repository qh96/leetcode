class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "": return 1
        c0 = c1 = 0 #count:0
        count = 0
        flag = int(s[0])
        for c,i in enumerate(s):
            if i == '0': 
                if flag == 0:
                    c0 += 1
                    if c1 > 1 and c0 <= c1:
                        count += 1
                else:
                    count += 1
                    # print("here0:",count)
                    c0 = 1
                    flag = 0
            elif i == '1': 
                if flag == 1:
                    c1 += 1
                    if c0 > 1 and c1 <= c0:
                        count += 1
                else:
                    count += 1
                    # print("here1:",count)
                    c1 = 1
                    flag = 1
            
        
        return count
            
        
        