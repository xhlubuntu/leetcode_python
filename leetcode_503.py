
#tle

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rst = []
        if len(nums) == 0:
            return []
        for i in range(len(nums)):
            tmpx = -1
            for j in xrange(i+1,i+len(nums)):
                if(nums[j%len(nums)] > nums[i]):
                    tmpx = nums[j%len(nums)]
                    break
            rst.append(tmpx)
        return rst

nums = [1,2,1]
sol = Solution()
sol.nextGreaterElements(nums)