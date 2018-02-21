#19 ac

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def listLen(head):
    p = head
    cnt = 1
    while p.next is not None:
        p = p.next
        cnt+=1
    return cnt

#def findLastNNode(#head , n):
#    sz = listLen(head)
#    kth = sz - n
#    if kth < 0:
#        return None
#    i = 0
#    p = head
#    while p.next is not None and i < kth:
#        p = p.next
#        i+=1
#    return p
#

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        sz = listLen(head)
        kth = sz - n - 1
        if kth < 0:
            head = head.next
            return head
        i = 0
        p = head
        while p.next is not None and i < kth:
            p = p.next
            i += 1
        if p.next is not None:
            t = p.next
            del t
            p.next = p.next.next
        return head
