#ac

# Definition for singly-linked list.
class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution(object):
    def detectCycle(self,head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or not self.isCycle(head):
            return None
        return self.firstCycle(head)

    def isCycle(self,head):
        p = q = head
        while(p.next is not None and q.next is not None and q.next.next is not None):
            p = p.next
            q = q.next.next
            if(p == q):
                return True
        return False

    def firstCycle(self,head):
        p = head
        visitedList  = []
        while(p.next is not None):
            visitedList.append(p)
            if(p.next) in visitedList:
                return p.next
            p = p.next


