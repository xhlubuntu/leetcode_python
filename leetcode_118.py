#118 ac

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        rstList = []
        if numRows <= 0:
            return rstList
        #numRows >= 1
        lastList = [1]
        rstList.append(lastList)
        for i in range(1,numRows):
            curList = [1]
            for j in range(0,len(lastList)-1):
                curList.append( lastList[j]+lastList[j+1] )
            curList.append(1)
            rstList.append(curList)
            lastList = curList
        return rstList

#
import pprint
sol = Solution()
pprint.pprint(sol.generate(3))