#102 ac

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import Queue
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        nodeQueue = Queue.deque()
        levelQueue = Queue.deque()
        curLevel = 0

        nodeQueue.append(root)
        levelQueue.append(curLevel)

        rstMap= {}
        while len(nodeQueue) > 0:
            curNode = nodeQueue.popleft()
            curLevel = levelQueue.popleft()

            if curNode.left is not None:
                nodeQueue.append(curNode.left)
                levelQueue.append(curLevel+1)
            if curNode.right is not None:
                nodeQueue.append(curNode.right)
                levelQueue.append(curLevel+1)

            if rstMap.get(curLevel,None) is None:
                rstMap[curLevel] = [curNode.val]
            else:
                rstMap[curLevel].append(curNode.val)

        rstList = []
        for i in sorted(rstMap.keys()):
            rstList.append( rstMap[i] )
        return rstList