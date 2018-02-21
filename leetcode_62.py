#62 ac

def paths(m,n):
    if m == 1 or n == 1:
        return 1
    else:
        return paths(m-1,n)+paths(m,n-1)

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        import numpy as np
        dp = np.array( [ [0]*(n+1) ]*(m+1) )

        for i in range(0,len(dp)):
            dp[i][1] = 1
        for j in range(0,len(dp[1])):
            dp[1][j] = 1
        for i in range(2,len(dp)):
            for j in range(2,len(dp[i])):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return int(dp[m][n])

sol = Solution()
sol.uniquePaths(1,2)