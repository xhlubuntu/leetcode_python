#112 ac

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def pathSum(node,s):
    if node is not None:
        if node.left is None and node.right is None and node.val == s:
            return True
        else:
            leftResult = None
            rightResult = None
            if node.left is not None:
                leftResult = pathSum(node.left,s-node.val)
            if node.right is not None:
                rightResult = pathSum(node.right,s-node.val)
            if leftResult == True or rightResult == True:
                return True

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        rst = pathSum(root,sum)
        return rst if rst is not None else False