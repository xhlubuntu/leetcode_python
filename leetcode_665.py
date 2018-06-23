import copy
#ac
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 0
        a , b = copy.copy(nums),copy.copy(nums)
        while(i<len(nums)-1):
            if(nums[i]>nums[i+1]):
                a[i+1] = a[i]
                b[i] = b[i+1]
                break
            i+=1
        anondescnt = sum([1 if a[i] > a[i + 1] else 0 for i in xrange(0, len(nums) - 1)])
        bnondescnt = sum([1 if b[i] > b[i + 1] else 0 for i in xrange(0, len(nums) - 1)])
        return True if (anondescnt == 0 or  bnondescnt == 0) else  False

sol = Solution()

nums = [3,4,2,3]
sol.checkPossibility(nums)



