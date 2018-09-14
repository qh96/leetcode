class Solution:
    def dailyTemperatures(self, tem):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        wait = [0] * len(tem)
        stack = []
        for i in range(len(tem)):
            while stack and tem[stack[-1]] < tem[i]:
                j = stack.pop()
                wait[j] = i-j
            stack.append(i)
        return wait