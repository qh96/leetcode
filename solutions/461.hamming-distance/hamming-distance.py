class Solution:
    def intToBin(self, n):
        return [int(digit) for digit in bin(n)[2:]]
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xToBin, yToBin = self.intToBin(x), self.intToBin(y)
        leng = len(xToBin) - len(yToBin)
        if leng < 0:
            xToBin = [0 for i in range(abs(leng))] + xToBin
        else:
            yToBin = [0 for i in range(abs(leng))] + yToBin
        count = 0
        for i in range(len(xToBin)):
            if xToBin[i] != yToBin[i]:
                count += 1
        return count