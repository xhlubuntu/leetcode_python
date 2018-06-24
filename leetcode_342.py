
#ac

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        x = bin(num)[2:]
        if sum(map(lambda t: 1 if t == '1' else 0,x)) == 1 and len(x)%2 == 1:
            return True
        else:
            return  False