# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def merge(left, right):
            dummy = cur = ListNode(0)
            while left and right: #left.next意味着left.val存在
                if left.val < right.val:
                    cur.next = left
                    cur = cur.next
                    left = left.next
                else:
                    cur.next = right
                    cur = cur.next
                    right = right.next
            cur.next = left or right
            
            return dummy.next
        
        # edge case
        
        if not head or not head.next:
            return head
        slow, fast, pre = head, head, None
        while fast and fast.next:
            pre = slow
            slow, fast = slow.next, fast.next.next
        pre.next = None
        return merge(self.sortList(head), self.sortList(slow))
        
        
        