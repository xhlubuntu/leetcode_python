#138

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):

    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None
        newHead = RandomListNode(head.label)

        p = head
        q = newHead

        reverseRandomMap = {}
        orderListMap = {}
        while p is not None:
            orderListMap[p] = q
            if p.random is not None:
                if reverseRandomMap.get(p.random,None) is None:
                    reverseRandomMap[p.random] = [ q ]
                else:
                    reverseRandomMap[p.random].append(q)
            if p.next is not None:
                newNode = RandomListNode(p.next.label)
                q.next = newNode
            p = p.next
            q = q.next
        #deal with random
        for k,v in reverseRandomMap:
            for x in v:
                x.random = orderListMap[k]

        return newHead





