#61 wa

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def listLen(head):
    p = head
    length = 0
    while p is not None:
        length+=1
        p = p.next
    return length

def kthNode(head,k):
    i = 0
    p = head
    while i<k and p is not None:
        p=p.next
        i+=1
    return p

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head
        length = listLen(head)
        if k < 0 or k >= length-1:
            return head
        p = kthNode(head,k)
        q = p.next
        p.next = None

        l = head
        head = q
        while q.next is not None:
            q=q.next
        q.next = l
        return head



