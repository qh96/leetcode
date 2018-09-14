class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        S = S + '0'
        L = list(S)
        l,r = 0,1
        while r < len(S):
            if S[r] != C and S[r] != '0':
                r += 1
            elif S[r] == C:
                if l == 0 and S[l] != C:
                    for i in range(r-l):
                        L[i] = r - l - i
                    l = r
                else:
                    i = 0
                    left, right = l,r
                    while left <= right:
                        L[left], L[right] = i, i
                        left += 1
                        right-= 1
                        i += 1
                    l = r
                    r += 1
            elif S[r] == '0':
                for i in range(l, r):
                    L[i] = i-l
                break
        L.pop()
        
        return L
        # print(''.join([str(i) for i in L]))