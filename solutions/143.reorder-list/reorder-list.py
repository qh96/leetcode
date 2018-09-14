# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head:

            fast = slow = head
            while fast and fast.next:
                temp = fast.next #even
                pre = slow
                slow, fast = slow.next, fast.next.next

            if fast:
                pre = slow
                tail = fast
            else: #even

                tail = temp

            #reverse
            prev = None
            cur = slow
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            # 1->   2->   3->   4->   5<-   6<-   7
            #       nxt
            # head
            # print(slow.val)
            # #土法解题, head每一步都跟上head.next
    #         nxt = head.next
    #         head.next = tail
    #         head = head.next
    #         tail = tail.next
    #         head.next = nxt
    #         head = head.next

    #         nxt = head.next
    #         head.next = tail
    #         head = head.next
    #         tail = tail.next
    #         head.next = nxt
    #         head = head.next

    #         nxt = head.next
    #         head.next = tail
    #         head = head.next
    #         tail = tail.next
    #         head.next = nxt
    #         head = head.next

            nxt = None
            while head != pre:
                nxt = head.next
                head.next = tail
                head = head.next
                tail = tail.next
                head.next = nxt
                head = head.next
            
            
        