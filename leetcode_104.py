
#104 ac
#BFS
class TreeNode(object):
    def __int__(self,x):
        self.val=x
        self.left=None
        self.right=None


import Queue
class Solution(object):
    #bfs
    def maxDepth(self,root):
        if root is None:
            return 0
        q = Queue.deque()
        q.append(root)
        levelQ = Queue.deque()
        levelQ.append(1)
        maxLevel = 0
        while len(q) > 0:
            currentNode = q.pop()
            currentLevel = levelQ.pop()
            maxLevel = currentLevel if currentLevel > maxLevel else maxLevel
            leftNode = currentNode.left
            rightNode = currentNode.right
            if leftNode is not None:
                q.append(leftNode)
                levelQ.append(currentLevel+1)
            if rightNode is not None:
                q.append(rightNode)
                levelQ.append(currentLevel+1)
        return maxLevel