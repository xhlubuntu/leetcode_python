#637
#wa

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



import Queue
import numpy as np
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        nodeq = Queue.deque()
        levelq = Queue.deque()
        if root is None:
            return [0.0]
        level = 0
        nodeq.append(root)
        levelq.append(level)
        retList = []
        tmparr = []
        curLevel = 0
        while len(nodeq) > 0:
            t = nodeq.pop()
            tl = levelq.pop()
            if t.left is not None:
                nodeq.append(t.left)
                levelq.append(tl + 1)
            if t.right is not None:
                nodeq.append(t.right)
                levelq.append(tl+1)
            if tl == curLevel:
                tmparr.append(t.val)
            if tl == curLevel + 1:
                retList.append( float(np.mean(tmparr)) )
                curLevel += 1
                tmparr = [t.val]
        retList.append( float(np.mean(tmparr)) )
        return retList




