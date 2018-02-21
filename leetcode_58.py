#58 ac

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        splited = s.strip().split(' ')
        l=len(splited)
        return len( splited[l-1] )