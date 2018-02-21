#34 ac

def lowBound(A,p,q,target):
    if p<=q:
        length = len(A)
        mid = (p+q)/2
        if A[mid] == target:
            k = mid
            while k-1>=0 and A[k-1] == target:
                k-=1
            return k
        if A[mid] < target:
            if mid+1<length:
                if A[mid+1]>target:
                    return mid
                elif(A[mid+1] == target):
                    return mid+1
                else:
                    return lowBound(A,mid+1,q,target)
        else:
            return lowBound(A,p,mid-1,target)

def upBound(A,p,q,target):
    if p <= q:
        length = len(A)
        mid= (p+q)/2
        if A[mid] == target:
            k = mid
            while k+1<length and A[k+1]==target:
                k+=1
            return k
        if A[mid]>target:
            if mid - 1 > -1:
                if A[mid-1]<target:
                    return mid
                elif(A[mid-1] == target):
                    return mid-1
                else:
                    return upBound(A,p,mid-1,target)
        else:
            return upBound(A,mid+1,q,target)


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        if length == 0:
            return [-1,-1]
        if target < nums[0] or target > nums[length-1]:
            return [-1,-1]
        else:
            low = lowBound(nums,0,length,target)
            up = upBound(nums,0,length,target)
            if nums[low] == target:
                return [low,up]
            else:
                return [-1,-1]

nums = [1,5]
target = 4
sol  = Solution()
print sol.searchRange(nums,target)