class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        leng = len(bits)
        while i<leng:
            if bits[i] == 0:
                # next 2
                i=i+1
                if i == leng:
                    return True
            if bits[i] == 1:
                i=i+2
                if i == leng:
                    return False
        