from collections import Counter
class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        countR = Counter(ransomNote)
        countM = Counter(magazine)

        if len(countR-countM)>0: return False
        else: return True
            


        