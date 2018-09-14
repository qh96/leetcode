class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for i in letters:
            if target >= i:
                if target >= letters[-1]:
                    return letters[0]
                continue
            else:
                return i