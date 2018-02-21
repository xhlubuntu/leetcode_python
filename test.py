import copy
import pprint
#0 1 2

maptable1 = ['0','1','8']
maptable2 = ['6','9']
class Solution:
    def dfs(self,globallist,arr,i,N):
        if N%2==0 and i == N/2 - 1:
            for j in maptable1:
                a = copy.deepcopy(arr)
                a[i] = j
                a[N-1-i]=j
                globallist.append(a)
            for j in range(len(maptable2)):
                a = copy.deepcopy(arr)
                a[i] = maptable2[j]
                a[N-1-i] = maptable2[1-j]
                globallist.append(a)
        elif N%2==1 and i == N/2:
            for j in maptable1:
                a = copy.deepcopy(arr)
                a[i] = j
                globallist.append(a)
        elif i == 0:
            for j in range(1,len(maptable1)):
                arr[i] = maptable1[j]
                arr[N-1-i]=maptable1[j]
                self.dfs(globallist,arr,i+1,N)
        else:
            for j in range(len(maptable1)):
                arr[i]=maptable1[j]
                arr[N-1-i]=maptable1[j]
                self.dfs(globallist,arr,i+1,N)
            for j in range(len(maptable2)):
                arr[i] = maptable2[j]
                arr[N-1-i] = maptable2[1-j]
                self.dfs(globallist,arr,i+1,N)

    def solve(self,N):
        gllst = []
        arr = [None]*N
        if N == 1:
            gllst = ['0','1','8']
        elif N == 2:
            gllst = ['00','11','69','88','96']
        else:
            self.dfs(gllst,arr,0,N)
        pprint.pprint(gllst)

s = Solution()
s.solve(3)