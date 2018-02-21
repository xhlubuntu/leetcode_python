#116 ac

# Definition for binary tree with next pointer.

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

def travel(p):
    q = p.next
    if q is not None:
        p.next = q.left
    while q:
        if q.left is not None:
            q.left.next = q.right
            if q.next is not None:
                q.right.next = q.next.left
        q = q.next
    return p



class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        p = TreeLinkNode(-1)
        p.next = root

        while p.next:
            p = travel(p)




