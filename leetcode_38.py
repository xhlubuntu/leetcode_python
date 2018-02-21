#38 ac

def count(strs):
    length = len(strs)
    i=0
    says = ''
    while i < length:
        j = i
        while j+1 < length and strs[j+1] == strs[i]:
            j+=1
        says+=str(j-i+1)+strs[i]
        i = j+1
    return says

def sequence(n):
    rst = '1'
    for i in range(0,n):
        rst = count(rst)
    return rst

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        return sequence(n-1)

sol = Solution()
print sol.countAndSay(6)
