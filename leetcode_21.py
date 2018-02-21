#21 ac

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        p=l1
        q=l2
        rnode = None
        if p.val < q.val:
            rnode = ListNode(p.val)
            p = p.next
        else:
            rnode = ListNode(q.val)
            q = q.next
        r = rnode
        while p and q:
            nnode = None
            if p.val < q.val:
                nnode = ListNode(p.val)
                p = p.next
            else:
                nnode = ListNode(q.val)
                q = q.next
            r.next = nnode
            r=r.next
        while p:
            nnode = ListNode(p.val)
            p = p.next
            r.next = nnode
            r=r.next
        while q:
            nnode = ListNode(q.val)
            q = q.next
            r.next = nnode
            r=r.next
        return rnode