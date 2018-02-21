#202 ac

def nextSquareSum(x):
    tmparr = []
    while x >= 10:
        tmparr.append(x%10)
        x/=10
    tmparr.append(x)
    return sum([i*i for i in tmparr])

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        tmpSet= set() # determine if it get into a cycle
        x = n
        while True:
            if x == 1:
                return True
            if x in tmpSet:
                return False
            tmpSet.add(x)
            x = nextSquareSum(x)


