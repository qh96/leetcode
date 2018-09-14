# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
        dummy1 = before = ListNode(0)
        dummy1.next = head
        dummy2 = after = ListNode(0)
        dummy2.next = head
        
        p = head
        while p:
            if p.val < x:
                before.next = p
                before = before.next
                
            else:
                after.next = p

                after = after.next
            p = p.next
        before.next, after.next = None, None
        # return dummy1.next
        before.next = dummy2.next
        return dummy1.next
        
        
        
        
        
        # dummy1 = before = ListNode(0)
        # dummy1.next = head
        # before.next = head.next
        # before.next.next = head.next.next
        # before.next.next.next = None
        # return dummy1.next
        
                