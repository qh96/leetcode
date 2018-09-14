class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        https://leetcode.com/problems/sort-colors/discuss/26474/Sharing-C++-solution-with-Good-Explanation?page=2
        """
        n = len(nums)
        white, red, blue = 0, 0, n - 1
        # 注意条件，white <= blue, 不是white < n
        while white <= blue:
            if nums[white] == 0:
                nums[white], nums[red] = nums[red], nums[white]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
