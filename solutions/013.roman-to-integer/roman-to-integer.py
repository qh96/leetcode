import re
class Solution:
    def f(self,char):
        return {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
            '1':4,
            '2':9,
            '3':40,
            '4':90,
            '5':400,
            '6':900
        }.get(char,0)
    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        _sum = 0
        rep = {"IV": "1", "IX": "2", "XL": "3", "XC": "4", "CD": "5", "CM": "6"}
        rep = dict((re.escape(k), v) for k, v in rep.items())
        pattern = re.compile("|".join(rep.keys()))
        s = pattern.sub(lambda m: rep[re.escape(m.group(0))], s)
        
        for i in s:
            _sum += self.f(i)
        return _sum
        
        
        