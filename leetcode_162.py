
#ac
def findpeak_aux(nums,i,j):
    if(i<=j):
        mid = int((i+j)/2)
        if(mid<0 or mid>=len(nums)):
            return None
        conditioncnt=0
        if(mid-1<0):
            conditioncnt+=1
        else:
            if(nums[mid]>nums[mid-1]):
                conditioncnt+=1
        if(mid+1>=len(nums)):
            conditioncnt+=1
        else:
            if(nums[mid]>nums[mid+1]):
                conditioncnt+=1
        if conditioncnt == 2:
            return mid
        else:
            left = findpeak_aux(nums,i,mid-1)
            right = findpeak_aux(nums,mid+1,j)
            return left if left is not None else right
    if(i>j):
        return None

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return findpeak_aux(nums,0,len(nums))


nums = [1,2,1,3,5,6,4]
findpeak_aux(nums,0,len(nums))
