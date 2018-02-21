#55 ac

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp = []
        if len(nums)<=1:
            return True
        dp.append( nums[0] )
        for i in range(1,len(nums)):
            if dp[i-1] < i:
                dp.append(0)
            else:
                dp.append( max(dp[i-1],nums[i]+i) )
        dplen = len(dp)
        return True if dp[dplen-2] >= len(nums)-1 else False