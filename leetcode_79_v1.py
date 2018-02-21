#79

import numpy as np

directions = [ (0,1),(0,-1),(1,0),(-1,0) ]

def isLegal(wordMatrix , travelMatrix , i , j ,letter ,k ):
    m = len(wordMatrix)
    n = len(wordMatrix[0])
    if 0<=i<m and 0<=j<n and wordMatrix[i][j] == letter[k] and travelMatrix[i][j] == 0:
        return True
    else:
        return False

def markCurrentStep(travelMatrix,i,j):
    travelMatrix[i][j] = 1

def search(wordMatrix , travelMatrix , i , j ,letter , k ):
    if(isLegal(wordMatrix,travelMatrix,i,j,letter,k)):
        #debug:
        print "{0} move to:".format(letter[k])
        print i,j

        if(k == len(letter) - 1):
            return True
        else:
            markCurrentStep(travelMatrix,i,j)
            trueCnt = 0
            for direction in directions:
                nextI = i + direction[0]
                nextJ = j + direction[1]
                rst = search(wordMatrix,travelMatrix,nextI,nextJ,letter,k+1)
                trueCnt = trueCnt + 1 if rst == True else trueCnt
            return True if trueCnt > 0 else None

def  wordSearch(wordMatrix,letter):
    nrow = len(wordMatrix)
    ncol = len(wordMatrix[0])
    tCnt = 0
    for i in range(0,nrow):
        for j in range(0,ncol):
            if wordMatrix[i][j] == letter[0]:
                travelMatrix = np.array([[0] * ncol] * nrow)
                rst = search(wordMatrix,travelMatrix,i,j,letter,0)
                tCnt = tCnt + 1 if  rst == True else tCnt
    return True if tCnt > 0 else False

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        return wordSearch(board,word)

board = [
     ['A','B','C','E']
    ,['S','F','C','S']
    ,['A','D','E','E']
]
#print wordSearch(board,'ABCB')
#print wordSearch(board,'ABCCED')
#print wordSearch(board,'SEE')

board = ["ABCE",
         "SFES",
         "ADEE"]
print wordSearch(board,"ABCESEEEFS")



