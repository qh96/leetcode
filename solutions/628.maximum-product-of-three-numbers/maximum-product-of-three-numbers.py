class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums)==3): return nums[0]*nums[1]*nums[2]
        s1 = nums[0] #small most
        s2 = nums[1]
        if s1>s2: s1,s2 = s2,s1
            
        b1 = nums[len(nums)-1]
        b2 = nums[len(nums)-2]
        b3 = nums[len(nums)-3]
        # print(b1,b2,b3) #4,1,7
        if b1<b2: b2,b1 = b1,b2#big most 
        if b1<b3: b3,b1 = b1,b3
        if b2<b3: b3,b2 = b2,b3
        # print(b1,b2,b3)
        print(s1,s2) 

        for i in range(2,len(nums)):
            if nums[i]<s2:
                if nums[i] < s1:
                    s2 = s1
                    s1 = nums[i]
                else:
                    s2 = nums[i]
        print(s1,s2)
        # print(b1,b2,b3) #7,6,2
        for i in range(0, len(nums)-3):
            if nums[i]>b3:
                if nums[i]>b2:
                    if nums[i] > b1:
                        b3 = b2
                        b2 = b1
                        b1 = nums[i]
                    else:
                        b3 = b2
                        b2 = nums[i]
                else:
                    b3 = nums[i]
                    
        # print(b1,b2,b3)
        r_s1, r_s2 = 0, 0
        
        if s1<0 and s2<0:
            r_s1 = 0-s1
            r_s2 = 0-s2
        
        print(r_s1, r_s2, b1, b1, b2, b3)
        nums.sort()
        print (nums)
        return max(r_s1 * r_s2 * b1, b1* b2 *b3)
        
#         List = [b1,b2,b3,r_s1,r_s2]
        
        
#         List.sort()
#         print(List)
#         return List[-1] * List[-2] * List[-3]
        
        
        
        

               