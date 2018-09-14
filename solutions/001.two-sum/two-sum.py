class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        set_nums = set(nums)

        for c,i in enumerate(nums):
            foo = target - i
            print(foo)
            if foo in set_nums:
                if i == foo:
                    bar = [i for i,n in enumerate(nums) if n==foo]
                    if len(bar)==1: continue
                    else: 
                        index = bar[1]
                        break
                index = nums.index(foo)
                print(index)
                break
        return [c,index]