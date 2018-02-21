
#33 ac
def binarySearch(s,i,j,k):
    if(i>j):
        return -1
    else:
        m = (i+j)>>1
        if m >= len(s):
            return -1
        if k==s[m]:
            return m
        elif k > s[m]:
            return binarySearch(s,m+1,j,k)
        else:
            return binarySearch(s,i,m-1,k)

def findPivotIndex(s,i,j):
    if(i>j):
        return -1
    else:
        m = (i+j)>>1
        if( m+1 < len(s) and s[m] > s[m+1] ):
            return m
        else: #s[m] < s[m+1]
            l = findPivotIndex(s,i,m-1)
            r = findPivotIndex(s,m+1,j)
            return l if r == -1 else r

class Solution(object):
    def search(self,s,target):
        idx = findPivotIndex(s,0,len(s))
        l = binarySearch(s,0,idx+1,target)
        r = binarySearch(s,idx+1,len(s),target)
        return l if r == -1 else r

sol = Solution()
print sol.search([4,5,6,7,0,1,2],4)