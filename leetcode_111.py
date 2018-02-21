#111 ac

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def minDepthOfTree(node,curLevel,levels):
    if node is not None:
        if node.left is None and node.right is None:
            levels.append(curLevel)
        if node.left is not None:
            minDepthOfTree(node.left , curLevel+1,levels)
        if node.right is not None:
            minDepthOfTree(node.right , curLevel+1,levels)


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        curLevel = 0
        levels = []
        if root is None:
            return 0
        minDepthOfTree(root,curLevel+1,levels)
        return min(levels)
