class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        flag = 0
        for i in nums1:
            flag = 0
            index = nums2.index(i)
            for j in nums2[index:]:
                if j <= i:
                    continue
                else:
                    flag = 1
                    res.append(j)
                    break
            if flag == 0: res.append(-1)
        return res