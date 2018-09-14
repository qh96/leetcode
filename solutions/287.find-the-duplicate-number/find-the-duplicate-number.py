class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = 0, 0
        while True:
            fast = nums[nums[fast]]
            print("fast", fast)
            slow = nums[slow]
            print("slow", slow)
            if fast == slow:
                break
        fast = 0
        print('----')
        while fast != slow:
            fast = nums[fast]
            print("fast", fast)
            slow = nums[slow]
            print("slow", slow)
        return slow
    