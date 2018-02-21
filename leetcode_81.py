#81 ac

def binarySearch(A,i,j,target):
    if i <= j:
        mid = (i+j)/2
        if A[mid] == target:
            return mid
        elif A[mid]> target:
            return binarySearch(A,i,mid-1,target)
        else:
            return binarySearch(A,mid+1,j,target)

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        length = len(nums)
        if length == 0:
            return False
        i = 0
        while i < length-1:
            if nums[i] > nums[i+1]:
                break
            else:
                i+=1
        left = binarySearch(nums,0,i,target)
        right = binarySearch(nums,i+1,length-1,target)
        return True if left is not None or right is not None else False
