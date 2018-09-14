# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return
        p,q = headA,headB
        count1,count2 = 0,0
        while p.next:
            p = p.next
            count1 += 1
        while q.next:
            q = q.next
            count2 += 1
        if p != q:
            return
        else:
            diff = abs(count1-count2)
            # print(count1,count2,diff)
            if count1 > count2:
                for i in range(diff):
                    headA = headA.next
            else:
                for i in range(diff):
                    headB = headB.next
            print(headA.val,headB.val)
            while headA != headB:
                headA,headB = headA.next,headB.next
            return headA
                
                    