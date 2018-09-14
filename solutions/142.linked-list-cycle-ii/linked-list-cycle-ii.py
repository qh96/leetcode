# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast, slow = head, head
        try:
            while True:
                fast = fast.next.next
                slow = slow.next
                if fast == slow:
                    break
        except:
            return None
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow