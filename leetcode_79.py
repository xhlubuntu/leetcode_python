
#79 we
directions = [(0,1),(1,0),(-1,0),(0,-1)]

def isLegal(lM,tM,i,j,word):
    m = len(lM)
    n = len(lM[0])

    if(0<=i<m and 0<=j < n and lM[i][j] == word and tM[i][j] != 1):
        return True
    return False

def markCurrentStep(tM,i,j):
    tM[i][j] = 1

def unmarkCurrentStep(tM,i,j):
    tM[i][j] = 0

def wordSearch(letterMatrix , travelMatrix , i , j , letter , k):
    if k == len(letter) - 1:
        return True
    else:
        rstCnt = 0
        for direction in directions:
            nextI = i + direction[0]
            nextJ = j + direction[1]
            markCurrentStep(travelMatrix,i,j)

            if isLegal(letterMatrix,travelMatrix,nextI,nextJ,letter[k+1]): #try next step. move
                #debug
                print "move:"
                print nextI,nextJ
                rst =  wordSearch(letterMatrix,travelMatrix,nextI,nextJ,letter,k+1)
                rstCnt = rstCnt + 1 if rst == True else rstCnt
            #unmarkCurrentStep(travelMatrix,i,j)
        return True if rstCnt>0 else None

class Solution(object):
    def search(self,board,letter):
        wordFirst = letter[0]
        firstStep = []
        nrow = len(board)
        ncol = len(board[0])
        for i in range(0,nrow):
            for j in range(0,ncol):
                if(board[i][j] == wordFirst):
                    firstStep.append((i,j))
        #travelMatrix = [[0]*ncol]*nrow
        trueCnt = 0
        for i,j in firstStep:
            #debug
            print "start move:"
            print i,j
            trvm = {}
            for i in range(0,nrow):
                trvm[i] = [0]*ncol
            rst = wordSearch(board,trvm,i,j,letter,0)
            trueCnt = trueCnt+1 if rst == True else trueCnt
        return True if trueCnt> 0 else False


sol = Solution()
board = [
     ['A','B','C','E']
    ,['S','F','C','S']
    ,['A','D','E','E']
]
#print sol.search(board,'ABCB')
print sol.search(board,'ABCCED')
#print sol.search(board,'SEE')