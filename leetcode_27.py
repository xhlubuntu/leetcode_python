#27 ac

def swap(A,i,j):
    A[i],A[j] = A[j],A[i]

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        i = 0
        while i < length:
            if nums[i] != val:
                i+=1
            else:
                for j in range(i,length-1):
                    swap(nums,j,j+1)
                length-=1

        return length
