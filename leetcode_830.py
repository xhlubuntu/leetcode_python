
#ac
class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        rst = []
        i = 0
        while i < len(S):
            j = i+1
            while(j< len(S) and S[j]==S[i]):
                j+=1
            if(j-i>=3):
                rst.append([i,j-1])
            i = j
        return rst

S = "abbxxxxzyy"
sol = Solution()
sol.largeGroupPositions(S)