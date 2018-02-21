#101

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inOrderTravel(root,rst):
    if root is not None:
        inOrderTravel(root.left,rst)
        if root.left is None:
            rst.append(-1)
        rst.append(root.val)
        inOrderTravel(root.right,rst)
        if root.right is None:
            rst.append(-1)

import Queue
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        rstList = []
        inOrderTravel(root,rstList)
        l = len(rstList)
        for i in range(0,l):
            if rstList[i] != rstList[l - 1 -i]:
                return False
        return True
