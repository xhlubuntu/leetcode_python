#6
## tle
import pprint
class Solution(object):
    def nextstepIsLegal(self,curx,cury,direction , nrow , ncol):
        if 0 <= curx+direction[0] < nrow and 0<= cury+direction[1] < ncol:
            return True
        else:
            return False
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        directions = [ (1,0),(-1,1) ]
        ncol = len(s)
        retList = {}
        for i in range(0,numRows):
            retList[i] = ['']*ncol
        #retList = []
        curdirectioncnt = 0
        curposx = 0
        curposy = 0
        curdirection = directions[curdirectioncnt % 2]
        for idx in range(0,len(s)):
            #print curposx,curposy
            #print s[idx]
            retList[curposx][curposy] = s[idx]
            #retList.append(s[idx])
            if not self.nextstepIsLegal(curposx,curposy,curdirection,numRows,ncol):
                curdirectioncnt += 1
            curdirection = directions[curdirectioncnt % 2]
            curposx = curposx + curdirection[0]
            curposy = curposy + curdirection[1]
        #return ''.join(retList)
        #pprint.pprint(retList)
        return ''.join([''.join( retList[i] ) for i in range(0,numRows)])


#sol = Solution()

#'AB'

#print sol.convert("PAYPALISHIRING", 3)
