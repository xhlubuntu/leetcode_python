#ac
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        binn = bin(n)[2:]
        for i in range(len(binn)):
            if i%2==0:
                if binn[i] == '0':
                    return False
            if i%2==1:
                if binn[i] == '1':
                    return False
        return True