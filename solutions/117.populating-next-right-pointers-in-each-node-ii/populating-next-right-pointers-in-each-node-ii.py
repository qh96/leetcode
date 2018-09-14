# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return None
        q = [root]
        while q:
            for i in range(len(q)):
                if i < len(q)-1:
                    q[i].next = q[i+1]
                else:
                    q[i].next = None
            q = [child for i in q if i for child in (i.left, i.right) if child] #加上了if child