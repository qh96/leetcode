class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        d = {}
        
        if not str or not pattern:
            return False
        pattern = list(pattern)
        string = str.split()
        
        if len(pattern) != len(string):
            return False
        
        for i,j in zip(pattern, string):
            if i not in d:
                if j not in d.values():
                    d[i] = j
                else:
                    return False
            elif d[i] == j:
                continue
            else:
                return False
        return True
            
            