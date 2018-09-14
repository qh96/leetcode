import re
class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for i in ops:
            if re.match('-?\d',i):
                stack.append(int(i))
            elif i == "C":
                stack.pop()
            elif i == "D":
                stack.append(2 * stack[-1])
            elif i == "+":
                stack.append(stack[-1] + stack[-2])
        return sum(stack)