# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        
        if not head:
            return None
        d = {}
        m = n = head
        while m:
            d[m] = RandomListNode(m.label)
            m = m.next
        while n:
            d[n].next = d.get(n.next)
            d[n].random = d.get(n.random)
            n = n.next
        return d[head]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

#         dic = dict()
#         m = n = head
#         while m:
#             dic[m] = RandomListNode(m.label)
#             m = m.next
#         #分开写的原因是，如果dic之前未存入节点，则dic[n].next里面没有n，会报错
#         while n:
#             dic[n].next = dic.get(n.random) #n.next--->Node with label 1 was not copied but a reference to the original one.
#             dic[n].random = dic.get(n.random)
#             n = n.next
#         return dic.get(head)
            