#73 ac

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        p = head
        while p is not None:
            if p.next is None:
                break
            if p.next is not None:
                if p.next.val == p.val:
                    q = p.next
                    p.next = p.next.next
                    del q
                else:
                    p = p.next
        return head
