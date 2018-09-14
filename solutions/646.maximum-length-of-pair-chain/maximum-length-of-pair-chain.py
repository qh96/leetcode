class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        #[[-6, -2], [-5, 3], [0, 3], [-1, 4], [1, 6], [-9, 8], [-6, 9], [8, 10]]
        count = 1
        l = sorted(pairs, key = lambda i: i[1])
        print(l)
        i = 0
        while i+1<len(l):
            if l[i][1] < l[i+1][0]: 
                count += 1
                print("p1")
                i += 1
            else:
                j = i
                while i+2<len(l) and l[j][1] >= l[i+2][0]:
                    i += 1
                if (i+2 == len(l)): break
                count += 1
                print("i:",i)
                print("p2")
                i += 2

        return count
                
            
            
                
            
            