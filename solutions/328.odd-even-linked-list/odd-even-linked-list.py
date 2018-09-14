# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd, even = ListNode(0), ListNode(0)
        dummy1, dummy2 = odd, even
        while head:
            odd.next = head
            even.next = head.next
            odd, even = odd.next, even.next
            head = head.next.next if even else None
        odd.next = dummy2.next
        return dummy1.next
            
            