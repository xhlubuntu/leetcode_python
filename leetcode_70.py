#70 ac

def climb(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n ==2 :
        return 2
    else:
        return climb(n-1)+climb(n-2)

def climbx(n):
    if n == 1:
        return 1
    if n==2:
        return 2
    a= 1
    b=2
    for i in range(3,n+1):
        t = a+b
        a=b
        b=t
    return b

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #fn = fn-1 + fn-2
        return climbx(n)