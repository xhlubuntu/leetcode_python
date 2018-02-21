#54 ac

directions = [(0,1),(1,0),(0,-1),(-1,0)]

def isLegal(matrix,statmat,i,j):
    m = len(matrix)
    n = len(matrix[0])
    if 0<=i<m and 0<=j<n and statmat[i][j] == 0:
        return True
    else:
        return False

def travel(matrix,statmat,i,j,dir,rst):
    m=len(matrix)
    n=len(matrix[0])
    if len(rst)<m*n:
        direction = directions[dir%4]
        nextI = i+direction[0]
        nextJ = j+direction[1]
        if isLegal(matrix,statmat,nextI,nextJ):
            rst.append(matrix[nextI][nextJ])
            statmat[nextI][nextJ]=1
            travel(matrix,statmat,nextI,nextJ,dir,rst)
        else:
            dir = dir+1
            direction = directions[dir%4]
            nextI = i + direction[0]
            nextJ = j + direction[1]
            if isLegal(matrix, statmat, nextI, nextJ):
                rst.append(matrix[nextI][nextJ])
                statmat[nextI][nextJ] = 1
                travel(matrix, statmat, nextI, nextJ, dir, rst)


import numpy as np
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        statmat=np.array( [[0]*n]*m )
        i,j,dir=0,0,0
        rst = []

        statmat[i][j]=1
        rst.append(matrix[i][j])

        travel(matrix,statmat,i,j,dir,rst)

        return rst
