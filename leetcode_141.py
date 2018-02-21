#141 ac

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def cycle(head):
    if head is None or head.next is None:
        return False
    q = head
    p = head
    while p.next is not None and q.next is not None and q.next.next is not None:
        p = p.next
        q = q.next.next
        if p == q:
            return True
    return False

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        return cycle(head)