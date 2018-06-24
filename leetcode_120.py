#ac

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m = len(triangle)
        if m == 0:
            return 0
        A = []
        for i in range(m):
            tmpx =[0 for j in range(i+1)]
            A.append(tmpx)
        A[0][0] = triangle[0][0]
        for i in range(1,m):
            for j in range(i+1):
                x = []
                if(j-1>=0):
                    x.append(A[i-1][j-1])
                if(j<i):
                    x.append(A[i-1][j])
                A[i][j] = min(x) + triangle[i][j]
        return min(A[m-1])


t = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

sol = Solution()
sol.minimumTotal(t)