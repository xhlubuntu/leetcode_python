#119 ac

def update(a):
  k = len(a)
  p,q = 0,0
  for i in range(0,k):
      q = a[i]
      a[i] = p + a[i]
      p = q
  a.append(1)
  return a


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex <= 0 :
            return [1]
        rstList = [1]
        for i in range(0,rowIndex):
            rstList = update(rstList)
        return rstList


#
sol = Solution()
print sol.getRow(3)