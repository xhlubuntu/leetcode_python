#46

def perm(A,i,rst):
    length = len(A)
    if i == length-1:
        return
    for j in range(i+1,length):
        A[i],A[j] = A[j],A[i]
        rst.append(A)
        perm(A,j,rst)
        A[i], A[j] = A[j], A[i]

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rst = []
        perm(nums,0,rst)
        return rst


sol = Solution()
print sol.permute([1,2,3])
