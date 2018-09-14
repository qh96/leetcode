class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 0: return [1]
        
        flag = 1
        list.reverse(digits)
        for c,i in enumerate(digits):
            if flag == 0:
                continue
            else:
                if i < 9:
                    digits[c] += 1
                    flag = 0
                else:
                    digits[c] = 0
                    flag = 1
                    if c == len(digits)-1: 
                        digits.append(1)
                        break
        list.reverse(digits)
        return digits