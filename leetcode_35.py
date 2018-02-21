#35 ac

def lowerBound(A,i,j,target):
    if i <= j:
        mid = (i+j)/2
        if A[mid] == target:
            k = mid
            while k -1 >=0 and A[k-1] == target:
                k-=1
            return k
        if A[mid] > target:
            if mid - 1 >= 0:
                if A[mid-1] == target:
                    return lowerBound(A,mid-1,mid-1,target)
                if A[mid-1] < target:
                    return mid
                if A[mid-1]> target:
                    return lowerBound(A,i,mid-1,target)
        if A[mid] < target:
            if mid + 1 < len(A):
                if A[mid+1] == target:
                    return lowerBound(A,mid+1,mid+1,target)
                if A[mid+1] < target:
                    return lowerBound(A,mid+1,j,target)
                if A[mid+1]> target:
                    return mid+1

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        if target <= nums[0]:
            return 0
        if target > nums[length-1]:
            return length
        return lowerBound(nums,0,length-1,target)

#[1,3,5,6], 5  2
#[1,3,5 6], 2  1
#[1,3,5,6], 7  4
#[1,3,5,6], 0  0
nums = [1,3,5,6]
sol = Solution()
print sol.searchInsert(nums,5)
print sol.searchInsert(nums,2)
print sol.searchInsert(nums,7)
print sol.searchInsert(nums,0)