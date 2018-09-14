from itertools import combinations
class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        # if num == 0: return ["0:00"]
        l = [-1,-2,-4,-8,1,2,4,8,16,32]
        ans = []
        # print(list(combinations(l,3)))
        for comb in combinations(l,num):
            clock = ''
            hours = 0
            minutes = 0
            for i in comb:
                if i < 0:
                    hours += abs(i)
                else:
                    minutes += i
            if hours > 11: continue
            if minutes > 59: continue
            if minutes < 10: minutes = '0{}'.format(minutes)
            clock = '{}:{}'.format(hours,minutes)
            ans.append(clock)
        return ans