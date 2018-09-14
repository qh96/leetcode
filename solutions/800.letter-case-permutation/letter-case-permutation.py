class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        l = [[i.upper(), i.lower()] if i.isalpha() else i for i in S]
        return [''.join(i) for i in itertools.product(*l)]
        
                