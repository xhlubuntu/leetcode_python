#74 ac

def searchRow(matrix,target):
    m = len(matrix)
    if m == 1:
        return 0
    for i in range(0,len(matrix)-1):
        if target >= matrix[i][0] and target < matrix[i+1][0]:
            return i
    return m-1

def binarySearch(A,i,j,target):
    if i<=j:
        mid = (i+j)/2
        if A[mid] == target:
            return mid
        elif( A[mid] > target):
            return binarySearch(A,i,mid-1,target)
        else:#A[mid]<target
            return binarySearch(A,mid+1,j,target)

def searchCol(matrix,rowid,target):
    lst = matrix[rowid]
    return binarySearch(lst,0,len(lst)-1,target)

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        if target < matrix[0][0] or target > matrix[m-1][n-1]:
            return False
        rowid = searchRow(matrix,target)
        return True if searchCol(matrix,rowid,target) is not None else False


matrix=[[1],[3]]
searchRow(matrix,3)

sol = Solution()
print sol.searchMatrix([[1]],1)