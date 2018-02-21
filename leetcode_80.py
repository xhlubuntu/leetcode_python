#80 ac

def swap(A,a,b):
    tmp = A[a]
    A[a] = A[b]
    A[b] = tmp

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length <= 1:
            return length
        j = 1
        i = 1
        while i < length:
            if nums[i] == nums[i-1]:
                j+=1
                if j <=2:
                    i+=1
                else:
                    k = i
                    while k < length-1:
                        swap(nums,k,k+1)
                        k+=1
                    length -= 1
                    j=2
            else:
                j=1
                i+=1
        return length

#sol = Solution()
#print sol.removeDuplicates([1,1,1,2,2,3])