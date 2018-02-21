#88 ac

def swap(s,i,j):
    tmp = s[i]
    s[i] = s[j]
    s[j] = tmp

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


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        mergeArray(nums1, m, nums2, n)

n1=[1,3,5,None,None,None]
n2 = [2,4,6]

mergeArray(n1,3,n2,3)
print n1
