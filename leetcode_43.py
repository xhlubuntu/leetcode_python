#43 ac

def arradd(numx,numy):
    tmp = 0
    rst = []
    lenx = len(numx)
    leny = len(numy)
    i = 0
    j = 0
    while i < lenx and j < leny:
        tmp = numx[i]+numy[j]+tmp
        rst.append(tmp%10)
        tmp/=10
        i+=1
        j+=1
    while i < lenx:
        tmp = numx[i]+tmp
        rst.append(tmp%10)
        tmp/=10
        i+=1
    while j< leny:
        tmp = numy[j]+tmp
        rst.append(tmp%10)
        tmp/=10
        j+=1
    if tmp>0:
        rst.append(tmp)
    return rst

def multi(num1,num2):
    n = len(num1)
    m = len(num2)
    a = [int( num1[n-1-i] ) for i in range(0,n)]        #reverse num1 and convert it to array[int]
    b = [int( num2[m-1-i] ) for i in range(0,m)]        #reverse num1 and convert it to array[int]

    rstList = []
    for j in range(0,m):
        tmp = 0
        x=[]
        for k in range(0, j):
            x.append(0)
        for i in range(0,n):
            tmp = b[j]*a[i]+tmp
            x.append(tmp%10)
            tmp/=10
        if tmp > 0:
            x.append(tmp)
        rstList.append(x)
    tmprst = rstList[0]
    for t in range(1,len(rstList)):
        tmprst = arradd(tmprst,rstList[t])
    return tmprst

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        tmpr = multi(num1,num2)
        tmpr.reverse()
        return ''.join( [str(i) for i in tmpr] )

sol = Solution()
print sol.multiply('98','9')