class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        L = S.split()
        for index,word in enumerate(L):
            if word[0] in 'aeiouAEIOU':
                L[index] += 'ma'
            else:
                L[index] = word[1:] + word[0] + 'ma'
            for i in range(index + 1):
                    L[index] += 'a'
        return ' '.join(L)