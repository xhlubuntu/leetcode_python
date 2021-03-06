#1
class Solution(object):
    def twoSumx(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sortedNum = sorted(nums)
        retList = []
        i = 0
        while i < len(nums):
            nextNum = target - nums[i]
            if nextNum in sortedNum[i+1:]:
                retList.append(i)
                retList.append(sortedNum.index(nextNum))
            else:
                i+=1
        return retList
    def twoSum(self,nums,target):
        sortedNums = sorted(nums)
        i = 0
        j = len(nums)-1
        x,y = 0,0
        while i < j:
            if(target == sortedNums[i] + sortedNums[j]):
                x = sortedNums[i]
                y = sortedNums[j]
            elif target > sortedNums[i] + sortedNums[j]:
                i+=1
            else:
                j-=1
        return [nums.index(x) , nums.index(y)]

#2
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        x = (l1.val +l2.val)%10
        y = (l1.val + l2.val)/10
        p = l1
        q = l2
        l3 = ListNode(x)
        r = l3
        while(p.next is not None and q.next is not None):
            p = p.next
            q = q.next
            tmp = p.val + q.val + y
            x = tmp%10
            y = tmp/10
            nNode = ListNode(x)
            r.next = nNode
            r = nNode
        while p.next is not None:
            p = p.next
            tmp = p.val + y
            x = tmp%10
            y = tmp/10
            nNode = ListNode(x)
            r.next = nNode
            r = nNode
        while q.next is not None:
            q = q.next
            tmp = q.val + y
            x = tmp%10
            y = tmp/10
            nNode = ListNode(x)
            r.next = nNode
            r = nNode
        if y > 0:
            nNode = ListNode(y)
            r.next = nNode
            r = nNode
        return l3


#20 ac
import Queue
class Solution(object):
  def isValid(self,s):
    tmpStack = Queue.deque()
    for i in s:
      if(len(tmpStack) == 0 or i in ['(','[','{']):
        tmpStack.append(i)
      else:
        l = tmpStack.pop()
        if l+i not in ['()','[]','{}']:
          return False
    if len(tmpStack) >0:
        return False
    return True

sol = Solution()
print sol.isValid("(){}[{]]")


#26
class Solution(object):
    def removeDuplicates(self,s):
        if(len(s)<=0):
            return
        cnt = 1
        for i in range(1 , len(s) ):
            if(s[i]!=s[i-1]):
                cnt+=1
        return cnt

sol = Solution()
print sol.lenOfDuplicate([1])

#33 ac
def binarySearch(s,i,j,k):
    if(i>j):
        return -1
    else:
        m = (i+j)>>1
        if m >= len(s):
            return -1
        if k==s[m]:
            return m
        elif k > s[m]:
            return binarySearch(s,m+1,j,k)
        else:
            return binarySearch(s,i,m-1,k)

def findPivotIndex(s,i,j):
    if(i>j):
        return -1
    else:
        m = (i+j)>>1
        if( m+1 < len(s) and s[m] > s[m+1] ):
            return m
        else: #s[m] < s[m+1]
            l = findPivotIndex(s,i,m-1)
            r = findPivotIndex(s,m+1,j)
            return l if r == -1 else r

class Solution(object):
    def search(self,s,target):
        idx = findPivotIndex(s,0,len(s))
        l = binarySearch(s,0,idx+1,target)
        r = binarySearch(s,idx+1,len(s),target)
        return l if r == -1 else r

sol = Solution()
print sol.search([4,5,6,7,0,1,2],4)

#49 ac
class Solution(object):
    def groupAnagrams(self,strs):
        xmap = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if(xmap.get(sortedWord) is None):
                xmap[sortedWord] = [word]
            else:
                xmap[sortedWord].append(word)
        return xmap.values()

#17
def dfs(s,i,tmparr,output):
    if(i==len(s) - 1):
        for j in s[i]:
            output.append(''.join(tmparr + [j]))
    else:
        for j in s[i]:
            dfs(s , i+1 , tmparr + [j],output )

phoneNumberMap = {
     '1':'1'
     ,'2':'abc'
     ,'3':'def'
    ,'4':'ghi'
    ,'5':'jkl'
    ,'6':'mno'
    ,'7':'pqrs'
    ,'8':'tuv'
    ,'9':'wxyz'
}

class Solution(object):

    def letterCombinations(self,digits):
        output = []
        letters = [phoneNumberMap[i] for i in digits ]
        #debug
        print letters
        dfs(letters,0,[],output)
        return output

sol = Solution()
print sol.letterCombinations('23')


#78 ac
def subSetDfs(s,i,tmparr,output):
    if i < len(s):
        output.append( tmparr + [s[i]] )
    for j in range(i+1,len(s)):
        subSetDfs(s,j,tmparr + [s[i]],output)

class Solution(object):
    def subsets(self,nums):
        output = []
        output.append([])
        for i in range(0,len(nums)):
            subSetDfs(nums,i,[],output)
        return output

sol = Solution()
print sol.subSet([1,2,3])

#215 ac
def swap(s,x,y):
    t = s[x]
    s[x]=s[y]
    s[y]=t


def kthMaxAux(s,i,j,k):
  tmp = s[i]
  q = i+1
  for p in range(i+1,j):
      if s[p] >= tmp:
          swap(s,p,q)
          q+=1
  q-=1
  swap(s,i,q)
  if q == k-1:
      return s[q]
  elif q>k-1:
      return kthMaxAux(s,i,q,k)
  else:
      return kthMaxAux(s,q+1,j,k)

#
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return kthMaxAux(nums,0,len(nums),k)


#print kthMax([3,2,1,5,6,4] , 1)

#79 xxx
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
            #markCurrentStep(travelMatrix,i,j)

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
            rst = wordSearch(board,[[0]*ncol]*nrow,i,j,letter,0)
            trueCnt = trueCnt+1 if rst == True else trueCnt
        return True if trueCnt> 0 else False


sol = Solution()
board = [
     ['A','B','C','E']
    ,['S','F','C','S']
    ,['A','D','E','E']
]
#print sol.search(board,'ABCB')
#print sol.search(board,'ABCCED')
print sol.search(board,'SEE')

#104 ac
class TreeNode(object):
    def __int__(self,x):
        self.val=x
        self.left=None
        self.right=None


import Queue
class Solution(object):
    #bfs
    def maxDepth(self,root):
        if root is None:
            return 0
        q = Queue.deque()
        q.append(root)
        levelQ = Queue.deque()
        levelQ.append(1)
        maxLevel = 0
        while len(q) > 0:
            currentNode = q.pop()
            currentLevel = levelQ.pop()
            maxLevel = currentLevel if currentLevel > maxLevel else maxLevel
            leftNode = currentNode.left
            rightNode = currentNode.right
            if leftNode is not None:
                q.append(leftNode)
                levelQ.append(currentLevel+1)
            if rightNode is not None:
                q.append(rightNode)
                levelQ.append(currentLevel+1)
        return maxLevel

#88
def insertArray(s,m,k):
    idx = 0
    while idx <m and s[idx] < k:
        idx+=1
    s[m] = k
    q = m
    while q > idx:
        swap(s,q,q-1)
        q-=1
    m+=1
    return m

def mergeArray(num1,m,num2,n):
    for i in range(0,n):
        m = insertArray(num1,m,num2[i])

n1=[1,2,3,5,None,None]
n2 = [4,6]

mergeArray(n1,4,n2,2)
print n1
