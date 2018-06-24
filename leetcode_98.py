
#ac

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def midtravel(vals,root):
    if root is not None:
        if root.left is not None:
            midtravel(vals,root.left)
        vals.append(root.val)
        if root.right is not None:
            midtravel(vals,root.right)

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        rst = []
        midtravel(rst,root)
        if len(rst) == 0 or len(rst) == 1:
            return True
        for i in range(len(rst)-1):
            if(rst[i+1] <= rst[i]):
                return False
        return True
