from collections import Counter
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # d = {}
        # d_2 = {}
        ans = {}
        set_nums2 = set(nums2)
        
        count1 = collections.Counter(nums1)
        count2 = collections.Counter(nums2)
        
#         for i in nums1:
#             d[i] = 0
#         for i in nums1:
#             d[i] += 1
        
#         for i in nums2:
#             d_2[i] = 0
#         for i in nums2:
#             d_2[i] += 1
        
        for i in count1.keys():
            if i in set_nums2:
                ans[i] = min(dict(count1)[i],dict(count2)[i])
        return list(collections.Counter(ans).elements())
        
        
            
                