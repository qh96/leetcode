class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        1->2->3->4->5->NULL
        1->2<-3-<4->5->NULL
        """
        if m == n:
            return head
        dummy = ListNode(0)
        dummy.next = head
        
        pre = dummy
        for _ in range(m-1):
            pre = pre.next #pre -> 1

        cur = pre.next
        temp = cur

        prev = None
        for _ in range(n-m+1):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        pre.next = prev
        temp.next = cur
        return dummy.next

        
            
        
        
            
        
            