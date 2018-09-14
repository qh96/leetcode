class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        cU = cD = cL = cR = 0
        for i in moves:
            if i == 'U': cU += 1
            elif i == 'D': cD += 1
            elif i == 'L': cL += 1
            elif i == 'R': cR += 1
        
        
        
        if cU == cD and cL == cR: return True
        else:
            return False