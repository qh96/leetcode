class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
#         l = []
#         dic = {}
#         for i in nums:
#             dic[i] = 0
#         for i in nums:
#             dic[i] += 1

#         for k,v in dic.items():
#             if v == 2:
#                 l.append(k)
        
#         s_nums = set(nums)
#         for i in range(1,len(nums)+1):
#             if i not in s_nums:
#                 l.append(i)
        
#         return l
        correct_sum = sum(range(1,len(nums)+1))
        now_sum = sum(nums)
        set_sum = sum(set(nums))
        
        du = now_sum - set_sum
        mi = correct_sum - set_sum
        
        return [du,mi]
            