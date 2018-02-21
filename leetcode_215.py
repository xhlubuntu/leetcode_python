
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