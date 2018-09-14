# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            slow = head
            faster = head.next
            while slow is not faster:
                slow = slow.next
                faster = faster.next.next
            return True
        except:
            return False
        
        
            