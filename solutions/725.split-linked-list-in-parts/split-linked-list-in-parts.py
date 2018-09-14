# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import math
class Solution:
    def splitListToParts(self, head, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """ 
        l = []
        p = head
        count = 0
        while p:
            count += 1
            p = p.next
        res = 0
        q = head
        while k:
            '''
            8/5
            6/4
            4/3
            2/2
            1/1
            '''
            res = math.ceil(count / k)

            count -= res
            k -= 1
            
            temp = q

            dummy = ListNode(0)
            dummy.next = temp
            
            i = 0
            while i < res - 1 and q:
                temp = temp.next
                q = temp.next
                i += 1
            
            if res == 1:
                q = q.next
            if res == 0:
                l.append([])
                continue
            temp.next = None
            l.append(dummy.next)
            
        return l
            
        
            
        