#143

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reorder(p):
    if p is None or p.next is None:
        return None
    k = p.next
    while k.next is not None and k.next.next is not None:
        k = k.next
    q = k.next
    if q is None:
        return None
    if q is not None:
        k.next = None
        q.next = p.next
        p.next = q
        return q.next

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        p = reorder(head)
        while p:
            p = reorder(p)
