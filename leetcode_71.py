#71 ac

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        import os.path
        return os.path.abspath(path)