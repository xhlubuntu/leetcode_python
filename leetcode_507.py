
#tle
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return  True if sum( [i if num%i==0 else 0 for i in xrange(1,num)] ) == num else False