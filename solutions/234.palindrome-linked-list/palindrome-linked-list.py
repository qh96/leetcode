# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return True
        count = 0
        p = head
        while p:
            p = p.next
            count += 1   
        mid = head
        for i in range(count // 2):
            mid = mid.next
        prev = None
        cur = head
        while cur != mid:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        # return all()
        if count % 2 != 0: mid = mid.next
        # print(prev.val,mid.val)
        for i in range(count // 2):
            if prev.val == mid.val:
                prev,mid = prev.next,mid.next
            else:
                return False
        return True
        