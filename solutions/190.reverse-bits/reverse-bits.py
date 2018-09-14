class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        nToBin = bin(n)[2:]
        strr = ''
        for i in range(abs(32-len(nToBin))):
            strr += '0'
        
        return int(bin(n)[2:][::-1] + strr,2)