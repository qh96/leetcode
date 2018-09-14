class Solution:
    def pushDominoes(self, d):
        """
        :type dominoes: str
        :rtype: str
        """
        d = 'L' + d + 'R'
        d = list(d)
        left = 0
        right = 1

        while right < len(d):
            if d[left] == 'L' and d[right] == 'L':
                for i in range(left,right):
                    d[i] = 'L'
                left = right
            elif d[left] == 'R' and d[right] == 'R':
                for i in range(left,right):
                    d[i] = 'R'
                left = right
            elif d[left] == 'R' and d[right] == 'L':
                i = 0
                while left+1+i != right-1-i and i < (right-left)//2:
                    d[left+1+i] = 'R'
                    d[right-1-i] = 'L'
                    i += 1
                left = right
            elif d[left] == 'L' and d[right] == 'R':
                print(left,right)
                left = right
                
            right += 1
        d.pop(0)
        d.pop(-1)
        return ''.join(d)
                                
                