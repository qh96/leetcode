class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        # list_x = [int(i) for i in str(x)]
        # if len(list_x) == 1: return True
        # else:
        #     return True if all(list_x[i] == list_x[~i] for i in range(len(list_x) // 2)) else False
        x = str(x)
        return True if x == x[::-1] else False
            