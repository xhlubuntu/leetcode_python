#82 ac

# Definition for singl-linked list.
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
        q = ListNode(-1)
        nhead = q
        q.next = head
        p=head
        while p is not None:
            if p.next is None:
                break
            else:
                cnt = 1
                while p.next is not None and p.next.val == p.val:
                    cnt+=1
                    p = p.next
                if cnt > 1:
                    p = p.next
                    q.next = p
                else:
                    q = q.next
                    p = p.next
        return nhead.next
