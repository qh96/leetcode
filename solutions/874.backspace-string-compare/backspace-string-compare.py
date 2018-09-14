class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stackS, stackT = [], []
        for i in S:
            if i != '#':
                stackS.append(i)
            elif stackS:
                stackS.pop()
        for i in T:
            if i != '#':
                stackT.append(i)
            elif stackT:
                stackT.pop()
        return stackS == stackT
        