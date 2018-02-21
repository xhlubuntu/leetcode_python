#24 ac

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def swappq(p,q,t):
    if t is not None:
        t.next = q
    ##p->q = > q->p
    p.next = q.next
    q.next = p

#1->2->3->4 ==> 2->1->4->3
def swapp(head):
    if head is None:
        return None
    p = head
    q = head.next
    if q is None:
        return head
    newhead = q
    swappq(p,q,None)
    while(p.next is not None and p.next.next is not None):
        t = p
        q = p.next.next
        p = p.next
        swappq(p,q,t)
    return newhead

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return swapp(head)