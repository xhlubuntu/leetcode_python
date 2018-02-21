
#2 ac
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        x = (l1.val +l2.val)%10
        y = (l1.val + l2.val)/10
        p = l1
        q = l2
        l3 = ListNode(x)
        r = l3
        while(p.next is not None and q.next is not None):
            p = p.next
            q = q.next
            tmp = p.val + q.val + y
            x = tmp%10
            y = tmp/10
            nNode = ListNode(x)
            r.next = nNode
            r = nNode
        while p.next is not None:
            p = p.next
            tmp = p.val + y
            x = tmp%10
            y = tmp/10
            nNode = ListNode(x)
            r.next = nNode
            r = nNode
        while q.next is not None:
            q = q.next
            tmp = q.val + y
            x = tmp%10
            y = tmp/10
            nNode = ListNode(x)
            r.next = nNode
            r = nNode
        if y > 0:
            nNode = ListNode(y)
            r.next = nNode
            r = nNode
        return l3