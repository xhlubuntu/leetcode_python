#86 ac

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        pp,q,p=None,None,None

        if head is None or head.next is None:
            return head

        q = ListNode(0)
        q.next = head
        pp = q
        p = head
        nhead = q

        while p is not None:
            if p.val < x:
                if p == q.next:
                    pp = p
                    p = p.next
                    q = q.next
                else:
                    pp.next = p.next
                    p.next = q.next
                    q.next = p
                    q = p
                    p = pp.next
            else: #p.val >=x
                pp = p
                p = p.next
        return nhead.next