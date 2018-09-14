class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return all(i == '0' for i in bin(num)[3:]) and len([i for i in bin(num)[3:]]) % 2 == 0 and bin(num)[2:][0] == '1'