#67 ac

def binaryToInt(s):
    pass
def intToBinary(i):
    pass

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        la = len(a)
        lb = len(b)
        itera = range(0,len(a))
        itera.reverse()
        iterb = range(0,lb)
        iterb.reverse()
        i = 0
        j = 0
        rst = []
        tmp = 0
        while i< la and j < lb:
            tmp = int( a[itera[i]] ) + int( b[iterb[j]] ) + tmp
            rst.append(tmp%2)
            tmp=tmp/2
            i+=1
            j+=1
        while i<la:
            tmp = int(a[itera[i]]) + tmp
            rst.append(tmp % 2)
            tmp = tmp / 2
            i += 1
        while j<lb:
            tmp = int(b[iterb[j]]) + tmp
            rst.append(tmp % 2)
            tmp = tmp / 2
            j+=1
        if tmp !=0:
            rst.append(tmp)
        rst.reverse()
        return ''.join([str(k) for k in rst])


sol = Solution()
print sol.addBinary('1','111')