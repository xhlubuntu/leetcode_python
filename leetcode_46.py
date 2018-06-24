#46
import copy

def perm(A,i,rst):
    length = len(A)
    if i == length:
        return
    for j in range(i,length):
        A[j], A[i] = A[i], A[j]
        copyed = copy.copy(A)
        rst.append(copyed)
        perm(A,j+1,rst)
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
