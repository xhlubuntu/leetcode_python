import Queue
#TLE
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if(len(matrix)==0):
            return False
        m , n = len(matrix) , len(matrix[0])
        if(n==0):
            return False
        visited = [ [0 for tmpi in range(n)] for tmpj in range(m) ]
        q = Queue.deque()
        if(matrix[0][0] == target):
            return True
        elif matrix[0][0] > target:
            return False
        else:
            visited[0][0] = 1
            q.append( (0,0))

        while( len(q) > 0 ):
            t = q.pop()
            i , j = t[0] , t[1]
            #print matrix[i][j]
            #print visited
            if(matrix[i][j] == target):
                return True
            if(j+1<n and matrix[i][j+1] <= target and visited[i][j+1] == 0):
                visited[i][j+1] = 1
                q.append( (i,j+1) )
            if(i+1<m and matrix[i+1][j] <= target and visited[i+1][j] == 0):
                visited[i+1][j] = 1
                q.append( (i+1,j) )
        return False


matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
sol=Solution()
sol.searchMatrix(matrix,5)